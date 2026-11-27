Builds `source/_static/vendor/matterviz/matterviz.js`, the structure viewer of the
materials pages. Rebuild after changing `entry.js` or the matterviz version:

    cd tools/matterviz
    pixi run npm ci
    pixi run node build.mjs

matterviz is pinned to a commit on `main` (it has no release with the WebGL2
fallback yet), and npm builds its `dist/` on install. Its dependency
svelte-widgets comes from a tarball upstream overwrites on every build, so
`npm ci` fails its integrity check once that changes; `npm install` then
refreshes the lockfile.
