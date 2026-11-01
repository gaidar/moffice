// Page toolbar: Copy text fetches the raw markdown from GitHub and puts it on the clipboard.
// If that fails, it opens the raw file so the reader can copy it by hand.
(function () {
  function setStatus(button, message) {
    var status = button.parentNode.querySelector(".toolbar-status");
    if (status) status.textContent = message;
  }

  async function copyRaw(button) {
    var url = button.getAttribute("data-raw-url");
    setStatus(button, "Copying...");
    try {
      // The clipboard write must stay tied to the click, so the fetch runs inside a ClipboardItem where supported.
      if (window.ClipboardItem && navigator.clipboard && navigator.clipboard.write) {
        var blob = fetch(url).then(function (response) {
          if (!response.ok) throw new Error("HTTP " + response.status);
          return response.blob().then(function (b) {
            return new Blob([b], { type: "text/plain" });
          });
        });
        await navigator.clipboard.write([new ClipboardItem({ "text/plain": blob })]);
      } else {
        var response = await fetch(url);
        if (!response.ok) throw new Error("HTTP " + response.status);
        await navigator.clipboard.writeText(await response.text());
      }
      setStatus(button, "Copied.");
    } catch (error) {
      setStatus(button, "Could not copy. Opening the raw file, copy it from there.");
      window.open(url, "_blank", "noopener");
    }
  }

  document.addEventListener("click", function (event) {
    var button = event.target.closest && event.target.closest(".office-copy");
    if (button) copyRaw(button);
  });

  // Copy prompt: the first code block under "How to run it" or "How to invoke".
  var promptButton = document.querySelector(".office-copy-prompt");
  if (promptButton) {
    promptButton.addEventListener("click", function () {
      var heading = document.getElementById("how-to-run-it") || document.getElementById("how-to-invoke");
      var node = heading ? heading.nextElementSibling : null;
      while (node && !node.querySelector("pre") && node.tagName !== "PRE") node = node.nextElementSibling;
      var code = node ? node.querySelector("code") || node : null;
      if (!code) return;
      navigator.clipboard.writeText(code.textContent.trim()).then(function () {
        setStatus(promptButton, "Prompt copied. Paste it into your AI tool.");
      });
    });
  }

  // A Copy button on each code block, because most of them are text to paste.
  document.querySelectorAll(".doc-body pre").forEach(function (pre) {
    var button = document.createElement("button");
    button.type = "button";
    button.className = "code-copy";
    button.textContent = "Copy";
    button.addEventListener("click", function () {
      var code = pre.querySelector("code");
      navigator.clipboard.writeText((code || pre).textContent).then(function () {
        button.textContent = "Copied";
        setTimeout(function () { button.textContent = "Copy"; }, 1500);
      });
    });
    pre.insertBefore(button, pre.firstChild);
  });

  // Filter on the skills page.
  var filter = document.querySelector(".filter");
  if (filter) {
    var rows = document.querySelectorAll(".doc-body tr[data-skill]");
    filter.addEventListener("input", function () {
      // Match on any word of three letters or more, so "pipeline down" and "leads are bad" still find something.
      var words = filter.value.toLowerCase().split(/\s+/).filter(function (w) {
        return w.length > 2 && ["are", "the", "and", "our", "for", "not", "why", "how", "next", "month"].indexOf(w) === -1;
      });
      var shown = 0;
      function haystack(row) {
        return (row.textContent + " " + (row.getAttribute("data-keywords") || "")).toLowerCase();
      }
      function has(row, w) {
        return haystack(row).indexOf(w.replace(/s$/, "")) !== -1;
      }
      // Rows that match every word come first. Only if there are none, show rows that match any word.
      var strict = Array.prototype.some.call(rows, function (row) {
        return words.length > 0 && words.every(function (w) { return has(row, w); });
      });
      rows.forEach(function (row) {
        var hit = words.length === 0 || (strict
          ? words.every(function (w) { return has(row, w); })
          : words.some(function (w) { return has(row, w); }));
        row.hidden = !hit;
        if (hit) shown += 1;
      });
      document.querySelectorAll(".skill-group").forEach(function (group) {
        group.hidden = !group.querySelector("tr[data-skill]:not([hidden])");
      });
      var empty = document.querySelector(".filter-empty");
      if (empty) empty.hidden = shown !== 0;
    });
  }
})();
