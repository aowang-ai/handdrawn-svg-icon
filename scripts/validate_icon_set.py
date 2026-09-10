#!/usr/bin/env python3
"""Validate structural invariants for clean hand-drawn SVG icons."""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


FORBIDDEN_TAGS = {"image", "filter", "foreignObject", "text"}
SHAPE_TAGS = {"path", "rect", "circle", "ellipse", "line", "polyline", "polygon"}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def numeric_size(value: str | None) -> float | None:
    if not value:
        return None
    match = re.fullmatch(r"\s*([0-9]+(?:\.[0-9]+)?)\s*(?:px)?\s*", value)
    return float(match.group(1)) if match else None


def icon_paths(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(path for path in target.rglob("*.svg") if path.is_file())


def validate(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    try:
        root = ET.parse(path).getroot()
    except (ET.ParseError, OSError) as exc:
        return [f"cannot parse SVG: {exc}"], warnings

    if local_name(root.tag) != "svg":
        errors.append("root element is not <svg>")
        return errors, warnings

    view_box = root.get("viewBox", "").split()
    if len(view_box) != 4:
        errors.append("missing or invalid viewBox")
    else:
        try:
            x, y, width, height = (float(part) for part in view_box)
            if width <= 0 or height <= 0 or abs(width - height) > 1e-6:
                errors.append("viewBox must be positive and square")
            if (x, y, width, height) != (0.0, 0.0, 96.0, 96.0):
                warnings.append("recommended viewBox is 0 0 96 96")
        except ValueError:
            errors.append("viewBox contains non-numeric values")

    width = numeric_size(root.get("width"))
    height = numeric_size(root.get("height"))
    if width is None or height is None:
        errors.append("explicit numeric width and height are required")
    elif abs(width - height) > 1e-6:
        errors.append("width and height must be equal")

    child_names = [local_name(child.tag) for child in root]
    if "title" not in child_names or "desc" not in child_names:
        errors.append("top-level <title> and <desc> are required")
    if root.get("role") != "img":
        errors.append('root must declare role="img"')
    aria_ids = set(root.get("aria-labelledby", "").split())
    if not {"title", "desc"}.issubset(aria_ids):
        errors.append('aria-labelledby must reference "title desc"')

    tags = [local_name(element.tag) for element in root.iter()]
    forbidden = sorted(set(tags) & FORBIDDEN_TAGS)
    if forbidden:
        errors.append(f"forbidden elements present: {', '.join(forbidden)}")

    shape_count = sum(tag in SHAPE_TAGS for tag in tags)
    if shape_count < 3:
        errors.append("icon has fewer than three visible vector shapes")
    elif shape_count > 45:
        warnings.append(f"high detail density: {shape_count} vector shapes")

    serialized = ET.tostring(root, encoding="unicode")
    if "#233746" not in serialized.upper():
        errors.append("approved deep outline #233746 is missing")
    if "stroke-linecap:round" not in serialized and 'stroke-linecap="round"' not in serialized:
        errors.append("rounded line caps are missing")
    if "stroke-linejoin:round" not in serialized and 'stroke-linejoin="round"' not in serialized:
        errors.append("rounded line joins are missing")

    external_hrefs = re.findall(r"(?:href|xlink:href)=['\"]([^#][^'\"]*)", serialized)
    if external_hrefs:
        errors.append("external resource references are not allowed")

    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="SVG file or directory containing SVG icons")
    args = parser.parse_args()

    paths = icon_paths(args.target)
    if not paths:
        print(f"No SVG icons found at {args.target}", file=sys.stderr)
        return 2

    failed = False
    for path in paths:
        errors, warnings = validate(path)
        status = "FAIL" if errors else "OK"
        print(f"[{status}] {path}")
        for warning in warnings:
            print(f"  warning: {warning}")
        for error in errors:
            print(f"  error: {error}")
        failed = failed or bool(errors)

    print(f"Checked {len(paths)} icon(s); {'errors found' if failed else 'all structural checks passed'}.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
