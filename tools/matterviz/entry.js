// Expose mattervizShow(target, cif, props), which mounts a matterviz Structure viewer for CIF text.
import { mount } from "svelte";
import { Structure } from "matterviz";
import { parse_structure_file } from "./node_modules/matterviz/dist/structure/parse.js";
import { set_moyo_wasm_source } from "./node_modules/matterviz/dist/symmetry/analyze.js";
import moyoWasm from "@spglib/moyo-wasm/moyo_wasm_bg.wasm";
import appCss from "matterviz/app.css";

// The bundle has no URL to load the WASM or its worker from, so symmetry runs from the embedded bytes.
set_moyo_wasm_source(moyoWasm);

// A shadow root keeps matterviz's stylesheet, which also styles body, main and tables, off the host page.
// Some of its theme variables are declared on :root only, which a shadow root does not match.
window.mattervizShow = (target, cif, props = {}) => {
  const root = target.attachShadow({ mode: "open" });
  const style = document.createElement("style");
  style.textContent = appCss.replace(/:root\s*\{/g, ":host {");
  const host = document.createElement("div");
  root.append(style, host);
  mount(Structure, { target: host, props: { structure: parse_structure_file(cif, "structure.cif"), ...props } });
};
