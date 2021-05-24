window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};

MathJax.Hub.Config({
  TeX: {extensions: ["cancel.js"]}
});

document$.subscribe(() => {
  MathJax.typesetPromise()
})
