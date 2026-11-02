// Page toolbar: Copy full text fetches the raw markdown from GitHub and puts it on the clipboard.
// If that fails, it opens the raw file so the reader can copy it by hand.
(function () {
  function setStatus(button, message) {
    var status = button.parentNode.querySelector(".toolbar-status");
    if (status) status.textContent = message;
  }

  // A browser can block the pop-up, so the page always shows a real link to the raw file as well.
  function offerRawLink(element, before, url, after) {
    var status = element.parentNode.querySelector(".toolbar-status");
    if (!status) {
      status = document.createElement("span");
      status.className = "toolbar-status";
      status.setAttribute("role", "status");
      element.insertAdjacentElement("afterend", status);
      element.insertAdjacentText("afterend", " ");
    }
    var link = document.createElement("a");
    link.href = url;
    link.target = "_blank";
    link.rel = "noopener";
    link.textContent = "open the raw file";
    status.textContent = "";
    status.append(before + " ", link, " " + after);
    window.open(url, "_blank", "noopener");
  }

  // The clipboard is missing on insecure pages and can refuse a write, so failure must always show.
  function copyText(text) {
    if (!navigator.clipboard) return Promise.reject(new Error("No clipboard"));
    return navigator.clipboard.writeText(text);
  }

  function selectText(node) {
    var selection = window.getSelection();
    if (node && selection) selection.selectAllChildren(node);
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
      offerRawLink(button, "Could not copy, so", url, "and copy it from there.");
    }
  }

  document.addEventListener("click", function (event) {
    var button = event.target.closest && event.target.closest(".office-copy");
    if (button) copyRaw(button);
  });

  // Links to a raw file on GitHub save the file under its own name in one click.
  // GitHub stays the only copy. If the fetch fails, the link opens the raw file as usual.
  document.querySelectorAll('a.office-download, .doc-body a[href^="https://raw.githubusercontent.com/"]').forEach(function (link) {
    if (link.closest(".toolbar") && !link.classList.contains("office-download")) return;
    link.addEventListener("click", function (event) {
      event.preventDefault();
      var url = link.href;
      fetch(url).then(function (response) {
        if (!response.ok) throw new Error("HTTP " + response.status);
        return response.blob();
      }).then(function (blob) {
        var save = document.createElement("a");
        save.href = URL.createObjectURL(new Blob([blob], { type: "text/plain" }));
        save.download = url.split("/").pop();
        document.body.appendChild(save);
        save.click();
        save.remove();
        setTimeout(function () { URL.revokeObjectURL(save.href); }, 1000);
      }).catch(function () {
        offerRawLink(link, "Could not download, so", url, "and save it from there.");
      });
    });
  });

  // On skill pages, fold the sections written for the model. The source and Copy full text keep them.
  var inputs = document.querySelector(".doc-body.is-skill > #inputs");
  var checklist = document.querySelector(".doc-body.is-skill > #quality-checklist");
  if (inputs && checklist) {
    var fold = document.createElement("details");
    fold.className = "for-model";
    var label = document.createElement("summary");
    label.textContent = "What the model follows: inputs, procedure and output format";
    fold.appendChild(label);
    inputs.parentNode.insertBefore(fold, inputs);
    while (fold.nextSibling && fold.nextSibling !== checklist) fold.appendChild(fold.nextSibling);
    var hash = location.hash ? document.getElementById(location.hash.slice(1)) : null;
    if (hash && fold.contains(hash)) fold.open = true;
    // Folded content does not count toward CSS counters, so number the headings directly.
    document.querySelectorAll(".doc-body.is-skill h2").forEach(function (heading, index) {
      heading.style.counterSet = "sec " + (index + 1);
    });
  }

  // Copy prompt: the first code block under "How to run it" or "How to invoke".
  var promptButton = document.querySelector(".office-copy-prompt");
  if (promptButton) {
    promptButton.addEventListener("click", function () {
      var heading = document.getElementById("how-to-run-it") || document.getElementById("how-to-invoke");
      var node = heading ? heading.nextElementSibling : null;
      while (node && !node.querySelector("pre") && node.tagName !== "PRE") node = node.nextElementSibling;
      var code = node ? node.querySelector("code") || node : null;
      if (!code) return;
      copyText(code.textContent.trim()).then(function () {
        setStatus(promptButton, "Prompt copied. Paste it into your AI tool.");
      }).catch(function () {
        selectText(document.querySelector(".prompt-preview code") || code);
        setStatus(promptButton, "Could not copy. The prompt is selected, so press Ctrl or Cmd and C.");
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
      copyText((code || pre).textContent).then(function () {
        button.textContent = "Copied";
        setTimeout(function () { button.textContent = "Copy"; }, 1500);
      }).catch(function () {
        selectText(code || pre);
        button.textContent = "Press Ctrl or Cmd and C";
        setTimeout(function () { button.textContent = "Copy"; }, 4000);
      });
    });
    pre.insertBefore(button, pre.firstChild);
  });

  // One filter on the skills page, over the situations and the full list.
  var filter = document.querySelector(".filter");
  if (filter) {
    var rows = document.querySelectorAll(".skill-group tbody tr");
    filter.addEventListener("input", function () {
      // Match on any word of three letters or more, so "pipeline down" and "leads are bad" still find something.
      var words = filter.value.toLowerCase().split(/\s+/).filter(function (w) {
        return w.length > 2 && ["are", "the", "and", "our", "for", "not", "why", "how", "next", "month"].indexOf(w) === -1;
      });
      var shown = 0;
      function haystack(row) {
        return (row.textContent + " " + (row.getAttribute("data-keywords") || "")).toLowerCase();
      }
      // Match from the start of a word, so "new" finds "new company" and not "renewal".
      function has(row, w) {
        var stem = w.replace(/s$/, "").replace(/[^a-z0-9-]/g, "");
        return stem !== "" && new RegExp("(^|[^a-z0-9])" + stem).test(haystack(row));
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
        group.hidden = !group.querySelector("tbody tr:not([hidden])");
      });
      var empty = document.querySelector(".filter-empty:not(.filter-partial)");
      if (empty) empty.hidden = shown !== 0;
      // A partial match is not a full answer, so say so.
      var partial = document.querySelector(".filter-partial");
      if (partial) partial.hidden = strict || shown === 0 || words.length === 0;
    });
  }
})();
