window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    tags: "ams",
  },
  svg: { fontCache: "local" },
  options: {
    processHtmlClass: "math-inline|math-display",
    skipHtmlTags: ["script", "noscript", "style", "textarea", "pre", "code"],
    enableMenu: false,
  },
};
