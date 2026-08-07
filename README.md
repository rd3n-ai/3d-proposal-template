# 3D Proposal Template

A single self-contained HTML file for quoting mechanical/automation equipment
fast: confirmed requirements, the technical solution (each decision tagged
confirmed vs. engineering judgment), system flow, and an embedded, rotatable
3D model — no build step, no server, no dependencies beyond one CDN script tag
for [`<model-viewer>`](https://modelviewer.dev/).

**[Live example →](example.html)** (open locally, or view the rendered version
via the repo's GitHub Pages / raw file)

## Why

Quoting equipment usually means static renders in a PDF, or worse, no visual
at all until the design is "final." A viewer the client can actually rotate
and zoom — dropped straight into the same document as the spec table — closes
that gap without extra tooling. Every confirmed-vs-judgment row is inherited
from the [`mechanical-concept-brief`](https://github.com/rd3n-ai/claude-code-mechanical-concept)
Claude Code skill: nothing here should read as more settled than it actually is.

## Use it

1. Copy `template.html`, fill in the `{{PLACEHOLDER}}` fields.
2. Export your CAD model to `.glb`/`.gltf` (FreeCAD, Onshape, SolidWorks via a
   converter, or any tool that supports glTF export) and drop it in `model/`.
3. Open the file in a browser, or host it — it's a static page.

`example.html` is filled in with a real concept (a machine-vision wheel
identification conveyor, see [the full write-up](https://github.com/rd3n-ai/machine-vision-tire-id-conveyor)):
the actual proposed geometry as static renders, plus a placeholder 3D model
in the viewer section to demonstrate the interactive feature — swap
`model/sample.glb` for a real export to show the actual design there instead.

## About

Mechanical design engineer (SolidWorks, 11 years, 100+ projects).

## License

MIT.
