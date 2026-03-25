"""
Recolor club illustrations for dark backgrounds: black/neutral ink -> site cream
(--white), preserve orange/yellow accent pixels. Keeps alpha for smooth edges.

Run from repo root: python scripts/recolor_illustrations_dark_bg.py
"""
from __future__ import annotations

import colorsys
from pathlib import Path

from PIL import Image

# Match index.html :root
LINE = (240, 236, 224)  # --white #f0ece0


def recolor_rgba(r: int, g: int, b: int, a: int) -> tuple[int, int, int, int]:
    if a == 0:
        return (0, 0, 0, 0)

    rf, gf, bf = r / 255.0, g / 255.0, b / 255.0
    h, s, v = colorsys.rgb_to_hsv(rf, gf, bf)

    # Very dark pixels: black strokes and their anti-aliasing (not mid orange fills)
    if v < 0.12:
        return (*LINE, a)

    # Muted grays along black strokes (low saturation)
    if s < 0.12 and v < 0.55:
        return (*LINE, a)

    # Default: orange family and mid/dark warm tones stay as authored
    return (r, g, b, a)


def process_png(path: Path) -> None:
    im = Image.open(path).convert("RGBA")
    pixels = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            pixels[x, y] = recolor_rgba(*pixels[x, y])
    im.save(path, optimize=True)
    print(f"OK {path.name}")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    images = root / "images"
    for path in sorted(images.glob("ALESCLUB_ILU_02-*.png")):
        process_png(path)


if __name__ == "__main__":
    main()
