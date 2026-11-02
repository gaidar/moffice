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

  // Places that scroll sideways get a visible cue, and keyboard users can reach them.
  var scrollers = [];
  function addScrollCue(box, text) {
    var cue = document.createElement("p");
    cue.className = "scroll-cue";
    cue.textContent = text;
    box.insertAdjacentElement("afterend", cue);
    scrollers.push(box);
  }
  function markWide() {
    scrollers.forEach(function (box) {
      var wide = box.scrollWidth > box.clientWidth + 1;
      box.classList.toggle("is-wide", wide);
      if (wide) {
        box.tabIndex = 0;
        box.setAttribute("role", "region");
        box.setAttribute("aria-label", box.classList.contains("scroll") ? "Diagram that scrolls sideways" : "Table that scrolls sideways");
      } else {
        box.removeAttribute("tabindex");
        box.removeAttribute("role");
        box.removeAttribute("aria-label");
      }
    });
  }

  // On a phone, tables with sentences in them become labeled fields. Tables of short values keep their columns and scroll.
  document.querySelectorAll(".doc-body table").forEach(function (table) {
    var heads = Array.prototype.map.call(table.querySelectorAll("thead th"), function (th) { return th.textContent.trim(); });
    var wordy = Array.prototype.some.call(table.querySelectorAll("tbody td"), function (td) { return td.textContent.trim().length > 32; });
    if (wordy && heads.length) {
      table.classList.add("stack");
      // Display changes can remove table meaning from assistive technology, so state it.
      table.setAttribute("role", "table");
      table.querySelectorAll("thead, tbody").forEach(function (part) { part.setAttribute("role", "rowgroup"); });
      table.querySelectorAll("tr").forEach(function (row) { row.setAttribute("role", "row"); });
      table.querySelectorAll("th").forEach(function (th) { th.setAttribute("role", "columnheader"); });
      table.querySelectorAll("tbody tr").forEach(function (row) {
        Array.prototype.forEach.call(row.children, function (cell, index) {
          cell.setAttribute("role", "cell");
          cell.setAttribute("data-label", heads[index] || "");
          if (cell.textContent.trim() === "") cell.classList.add("is-empty");
        });
      });
    }
    // Above phone width a stacked table is still a table, and can still be too wide for the page.
    var box = document.createElement("div");
    box.className = "table-scroll";
    table.parentNode.insertBefore(box, table);
    box.appendChild(table);
    addScrollCue(box, "Scroll sideways to see the whole table.");
  });

  // On a phone, diagrams fold away, because the text around them says the same thing.
  var phone = window.matchMedia("(max-width: 760px)");
  var folds = [];
  document.querySelectorAll("figure > .scroll").forEach(function (scroll) {
    if (!scroll.querySelector(".dg")) return;
    var fold = document.createElement("details");
    fold.className = "fig-fold";
    var label = document.createElement("summary");
    fold.appendChild(label);
    scroll.parentNode.insertBefore(fold, scroll);
    fold.appendChild(scroll);
    addScrollCue(scroll, "Scroll sideways to see the whole diagram.");
    function setLabel() { label.textContent = fold.open ? "Hide diagram" : "Show diagram"; }
    fold.addEventListener("toggle", function () { setLabel(); markWide(); });
    fold.open = !phone.matches;
    setLabel();
    folds.push(fold);
  });
  phone.addEventListener("change", function () {
    folds.forEach(function (fold) { fold.open = !phone.matches; });
  });
  window.addEventListener("resize", markWide);
  markWide();

  // On this page: a list of the page's sections, for long guides, playbooks and office documents.
  var longPage = document.querySelector(".doc-body[data-contents]");
  if (longPage) {
    var sections = longPage.querySelectorAll(":scope > h2[id]");
    if (sections.length >= 4) {
      var contents = document.createElement("details");
      contents.className = "toc";
      var contentsLabel = document.createElement("summary");
      contentsLabel.textContent = "On this page";
      var contentsList = document.createElement("ul");
      sections.forEach(function (heading) {
        var item = document.createElement("li");
        var link = document.createElement("a");
        link.href = "#" + heading.id;
        link.textContent = heading.textContent;
        item.appendChild(link);
        contentsList.appendChild(item);
      });
      contents.append(contentsLabel, contentsList);
      var before = document.querySelector(".lead-figure") || longPage;
      before.parentNode.insertBefore(contents, before);
    }
  }

  // One filter on the skills page, over the situations and the full list.
  var filter = document.querySelector(".filter");
  if (filter) {
    var rows = document.querySelectorAll(".skill-group tbody tr");
    var filterCount = document.querySelector(".filter-count");
    var filterClear = document.querySelector(".filter-clear");
    function plural(number, word) { return number + " " + word + (number === 1 ? "" : "s"); }
    if (filterClear) {
      filterClear.addEventListener("click", function () {
        filter.value = "";
        filter.dispatchEvent(new Event("input"));
        filter.focus();
      });
    }
    filter.addEventListener("input", function () {
      // Match on any word of three letters or more, so "pipeline down" and "leads are bad" still find something.
      var words = filter.value.toLowerCase().split(/\s+/).filter(function (w) {
        return w.length > 2 && ["are", "the", "and", "our", "for", "not", "why", "how", "next", "month"].indexOf(w) === -1;
      });
      var shown = 0;
      var shownSkills = 0;
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
        if (hit) {
          shown += 1;
          if (row.hasAttribute("data-skill")) shownSkills += 1;
        }
      });
      document.querySelectorAll(".skill-group").forEach(function (group) {
        group.hidden = !group.querySelector("tbody tr:not([hidden])");
      });
      var empty = document.querySelector(".filter-empty:not(.filter-partial)");
      if (empty) empty.hidden = shown !== 0;
      // A partial match is not a full answer, so say so.
      var partial = document.querySelector(".filter-partial");
      if (partial) partial.hidden = strict || shown === 0 || words.length === 0;
      if (filterClear) filterClear.hidden = filter.value === "";
      if (filterCount) {
        var parts = [];
        if (shown - shownSkills > 0) parts.push(plural(shown - shownSkills, "situation"));
        if (shownSkills > 0) parts.push(plural(shownSkills, "skill"));
        filterCount.textContent = words.length > 0 && shown > 0 ? parts.join(" and ") + " shown." : "";
      }
    });
  }
})();
