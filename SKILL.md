---
name: handdrawn-svg-icon
description: Create or restyle standalone editable SVG icons and coherent icon sets in a clean hand-drawn academic style with dark rounded outlines and restrained pastel fills. Use for small icons in research figures, slides, diagrams, and visual systems; use an architecture-figure skill for the surrounding full diagram and a plotting tool for quantitative charts.
metadata:
  short-description: Draw consistent hand-drawn SVG icons
---

# Hand-drawn SVG Icon

Create compact vector icons that feel illustrated by one hand but remain clean enough for a paper figure. The target is controlled imperfection, not sketch noise.

## Output contract

- Deliver one editable `.svg` per semantic icon. Do not rasterize the source.
- Use SVG primitives and paths only. Do not embed PNG/JPEG assets, filters, or generated raster art.
- Default to a transparent `96 × 96` canvas with `viewBox="0 0 96 96"` unless the caller supplies an established icon grid.
- Include explicit `width`, `height`, `viewBox`, `<title>`, `<desc>`, `role="img"`, and `aria-labelledby`.
- Keep visual labels outside the icon. Avoid `<text>` inside icons; letterforms render inconsistently at small size.
- When producing a set, keep canvas, ink color, stroke hierarchy, fill palette, optical scale, and detail density consistent across every file.

## Required style

Read [references/style-spec.md](references/style-spec.md) before creating a new icon or restyling an icon set. Use [assets/icon-template.svg](assets/icon-template.svg) as the structural starting point when no source SVG exists.

The essential look is:

- one deep blue-gray outline rather than pure black;
- round line caps and joins;
- a strong outer contour with finer internal details;
- low-saturation paper-like fills;
- slight asymmetry introduced through deliberate curves or small skews;
- no duplicate jitter strokes, scribble filters, fake pencil texture, gradients, or shadows.

The five files under `assets/style-reference/` are approved examples of people, actions, selection, containers, and task flow. Inspect only the examples relevant to the requested semantics; adapt their grammar, not their literal objects.

## Semantic compression

Before drawing, reduce the request to:

1. **Primary noun or action** — the silhouette that must remain recognizable at 32–48 px.
2. **One supporting cue** — the smallest secondary object that disambiguates the meaning.
3. **State accent, if needed** — a check, cross, arrow, sparkle, lock, or small colored card.

Do not illustrate the whole sentence. Prefer one dominant object plus one cue. If the icon needs a caption to be understood, simplify or change the metaphor.

## Drawing workflow

1. Inspect any existing icon family before drawing. Preserve its canvas and optical scale when the user asks for a match.
2. Choose a familiar visual metaphor and a dominant silhouette. Reserve roughly 8 SVG units of safety margin.
3. Draw back-to-front: large fill shapes, main outline, internal details, then one state accent.
4. Make geometry lightly imperfect with a few quadratic curves, unequal radii, or 1–3 unit skews. Keep functional alignments deliberate.
5. Use at most three colored fills plus warm white in an ordinary icon. Reuse color by semantic role across a set.
6. Preview a single icon at 96 px and at 40 px. For a set, also compare all icons side by side.
7. Run `python scripts/validate_icon_set.py <svg-or-directory>`. Repair errors before delivery; review warnings visually.

## Matching an existing set

Treat the existing set as the source of truth. Sample its actual outline color, common stroke widths, color roles, safe area, and average object scale. Do not mix a new illustration system into an old set merely because it is attractive in isolation.

When replacing icons inside a larger SVG, preserve the surrounding figure and replace only the icon references or icon groups. Confirm that the icon remains legible at the figure's final publication size.

## Acceptance gate

Do not finish until all of the following are true:

- the silhouette reads without a caption at small size;
- no stroke or marker touches the canvas edge;
- outer and inner stroke weights have a visible hierarchy;
- repeated motifs use the same grammar across the set;
- the icon looks hand-drawn without looking dirty or unstable;
- fills remain distinguishable in grayscale by outline and shape;
- every SVG parses successfully and contains no raster or filter dependency;
- filenames are short, lowercase, semantic, and hyphenated.

For a batch, deliver the individual SVG files and a preview/contact sheet when visual comparison materially helps review. For use inside a full research architecture figure, combine this skill with the figure's own layout workflow rather than expanding this skill into diagram composition.
