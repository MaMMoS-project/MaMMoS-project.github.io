/* Crystal structure viewer and temperature charts for the materials pages. */
"use strict";

const MATTERVIZ = new URL("vendor/matterviz/matterviz.js", document.currentScript.src);

/** Load matterviz and show the crystal structure from the embedded CIF. */
function initStructure() {
  const el = document.querySelector(".mammos-structure");
  if (!el) return;
  const { cif } = JSON.parse(document.getElementById("mammos-material-data").textContent);
  const script = document.createElement("script");
  script.src = MATTERVIZ;
  script.onload = () => mattervizShow(el, cif);
  document.head.append(script);
}

/** Draw a section's Bokeh charts in the site's light or dark theme and redraw them when it changes. */
function initCharts(el) {
  const items = JSON.parse(el.nextElementSibling.textContent);
  let theme = null;
  // Redraws run one after another, so a quick double toggle cannot leave two sets of charts.
  let views = Promise.resolve([]);
  const draw = () => {
    const t = document.documentElement.dataset.theme === "dark" ? "dark" : "light";
    if (t === theme) return;
    theme = t;
    views = views.then((old) => {
      for (const v of old) v.remove();
      return Bokeh.embed.embed_item(items[t], el);
    });
  };
  draw();
  new MutationObserver(draw).observe(document.documentElement, { attributeFilter: ["data-theme"] });
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".mammos-charts").forEach(initCharts);
  // matterviz.js is large and takes a while to run: start it after the page has been drawn.
  requestAnimationFrame(() => setTimeout(initStructure));
});
