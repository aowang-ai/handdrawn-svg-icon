# Clean hand-drawn SVG style specification

Use this specification to reproduce the approved icon family consistently. It is intentionally more constrained than a general illustration guide.

## 1. Canvas and optical scale

- Default canvas: `96 × 96`, `viewBox="0 0 96 96"`.
- Safe area: keep ordinary strokes within approximately `x/y = 7…89`. Heavy round caps may require more room.
- Main silhouette: typically 58–72 SVG units in its longer dimension.
- Supporting cue: typically 18–32 units and subordinate to the main silhouette.
- Judge scale optically, not only by bounding box. Thin objects often need to be larger than solid objects to carry equal visual weight.
- Center the perceived mass. A handle, arrow, or document corner can extend farther on one side without making the icon feel off-center.

## 2. Ink and stroke hierarchy

Primary ink is `#233746`, a deep blue-gray. Avoid pure black.

| Role | Typical width | Use |
|---|---:|---|
| Silhouette | `3.4–3.8` | outer contour and dominant object |
| Main line | `3.0–3.3` | structural edges and connectors |
| Fine line | `2.2–2.5` | internal marks, page lines, facial cues |
| Emphasis | up to `8`, underlaid | rare handles or bold stems with a colored line over them |

Use `stroke-linecap="round"` and `stroke-linejoin="round"`. A filled silhouette may have its own explicit stroke rather than relying on a shared `.ink` class.

Do not:

- draw a second offset outline to simulate hand motion;
- apply turbulence, displacement, blur, shadow, or pencil filters;
- vary stroke width randomly;
- allow dense internal hatching at icon scale.

## 3. Approved palette

Use the palette by semantic role, not as decoration.

| Role | Color |
|---|---|
| Deep outline | `#233746` |
| Warm paper white | `#FFFDF6` |
| Primary blue | `#7DB6CF` |
| Pale blue | `#D7EAF2` or `#D7E8F1` |
| Golden yellow | `#F2C76C` |
| Pale yellow | `#F6E3AC` |
| Warm orange | `#E59A7C` |
| Sage green | `#90B58D` |
| Pale green | `#DDEAD9` |
| Pale violet | `#E8DFF0` |
| Pale rose | `#F4DEDD` |
| Blue accent | `#5A91AE` |
| Green confirmation | `#5D8B67` |
| Muted red rejection | `#A85B5B` |

Ordinary icons should use two or three colored fills plus warm white. Let the deep outline unify the family. Avoid large saturated areas.

Suggested semantics:

- blue: tools, information, retrieval, neutral system state;
- yellow: attention, candidate evidence, human role accent;
- orange: people, writing, intervention;
- green: accepted, retained, successful, selected;
- rose/red: rejected, conflict, warning;
- violet: synthesis or memory when differentiation is necessary.

## 4. Controlled imperfection

The icon should appear drawn rather than manufactured, but all important relationships must remain readable.

Use two or three of these techniques per icon:

- replace a rigid rectangle with a four-point path whose corners differ by 1–3 units;
- use `Q` curves instead of perfect arcs for paper edges, heads, bags, clouds, and containers;
- make paired elements slightly unequal in size or angle;
- tilt a card, page, or handle by a few degrees through its coordinates;
- let a contour bow gently rather than remain ruler-straight;
- offset internal lines slightly while preserving their shared direction.

Do not distort every edge. Baselines, grids, selection gates, and semantic connectors should still look intentional. The target is an illustrator's hand, not unstable geometry.

## 5. Shape hierarchy

Build icons in three visual layers:

1. **Dominant silhouette**: the concept's main object.
2. **Semantic cue**: one document, lens, arrow, lock, card, or status mark.
3. **Micro-detail**: two or three short lines or highlights that add character without becoming necessary for recognition.

Keep at least 3–5 units between unrelated outlined shapes. Avoid tangencies where two outlines almost touch; either separate them clearly or overlap them deliberately.

## 6. Metaphor patterns

### Person or agent

Use a warm face or torso fill and one occupational cue: headset, pencil, clipboard, badge, or small board. Do not add full anatomy. Keep the face nearly featureless when rendered below 64 px.

### Tool or action

Use the tool as the silhouette and add one action cue. Examples: globe plus lens for web search; document plus eye for reading; document plus check for extracted evidence.

### Process or routing

Show a small number of inputs, one transformation object, and one or two outcomes. Avoid miniature flowcharts. Selection is better represented by cards entering a gate than by several labeled boxes.

### Container or memory

Use overlapping cards plus a folder, tray, archive, or box. Vary card angles slightly. A check mark indicates selected content; a lock indicates persistent or controlled content.

### Abstract technical concept

Start from the operation rather than the term. Ask what enters, what changes, and what leaves. Encode that transformation with familiar objects. Use mathematical symbols only when they are already the community's standard iconography.

## 7. Small-size legibility

Check at both 96 px and 40 px:

- the main silhouette must remain obvious at 40 px;
- gaps must not collapse;
- fine lines may disappear without destroying meaning;
- state accents must not be mistaken for noise;
- color cannot be the only carrier of selection, success, or rejection.

If an icon fails at 40 px, remove details before increasing stroke weight globally.

## 8. Common failures and repairs

| Failure | Repair |
|---|---|
| Looks like generic flat UI art | replace perfect geometry with a few controlled curves/skews; retain one clean outline |
| Looks dirty or shaky | remove duplicate strokes and filters; restore one consistent contour |
| Too many tiny objects | select one silhouette and one cue; move explanation to the surrounding figure |
| Inconsistent set | normalize canvas, optical scale, ink color, stroke hierarchy, and palette roles |
| Cute but academically weak | reduce facial detail and decoration; emphasize the technical object or action |
| Meaning depends on color | add a check, cross, arrow, gate, or distinct silhouette |
| Icon becomes a mini-diagram | keep only the transformation metaphor; let the surrounding architecture figure carry the flow |

## 9. SVG structure

Use a structure similar to:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96"
     viewBox="0 0 96 96" role="img" aria-labelledby="title desc">
  <title id="title">Semantic icon name</title>
  <desc id="desc">A concise description of the visible icon.</desc>
  <style>
    .ink{fill:none;stroke:#233746;stroke-width:3.2;stroke-linecap:round;stroke-linejoin:round}
    .fine{fill:none;stroke:#233746;stroke-width:2.3;stroke-linecap:round;stroke-linejoin:round}
  </style>
  <g id="icon">…</g>
</svg>
```

Keep each semantic object in a `<g>` when that improves later editing. Prefer readable coordinates over minified path data. Do not convert the icon to one opaque compound path.
