// Bundle entry.js and matterviz into one classic script for the materials pages.
import * as esbuild from "esbuild";
import sveltePlugin from "esbuild-svelte";

await esbuild.build({
  entryPoints: ["entry.js"],
  bundle: true,
  format: "iife",
  minify: true,
  outfile: "../../source/_static/vendor/matterviz/matterviz.js",
  conditions: ["svelte", "browser"],
  mainFields: ["svelte", "browser", "module", "main"],
  // Svelte injects component styles into the document the component is mounted in, here the shadow root.
  plugins: [sveltePlugin({ compilerOptions: { css: "injected" } })],
  loader: { ".wasm": "binary", ".json": "json", ".css": "text" },
  logLevel: "warning",
});
