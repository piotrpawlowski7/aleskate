"""
Map illustration ink from site cream (#f0ece0) back to black for light backgrounds.
Orange pixels unchanged. Inverse of recolor_illustrations_dark_bg.py output.

Run from repo root: python scripts/recolor_illustrations_light_bg.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

LINE = (240, 236, 224)


def to_black_ink(r: int, g: int, b: int, a: int) -> tuple[int, int, int, int]:
    if a == 0:
        return (0, 0, 0, 0)
    if (
        abs(r - LINE[0]) <= 4
        and abs(g - LINE[1]) <= 4
        and abs(b - LINE[2]) <= 4
    ):
        return (0, 0, 0, a)
    return (r, g, b, a)


def process_png(path: Path) -> None:
    im = Image.open(path).convert("RGBA")
    pixels = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            pixels[x, y] = to_black_ink(*pixels[x, y])
    im.save(path, optimize=True)
    print(f"OK {path.name}")


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    images = root / "images"
    for path in sorted(images.glob("ALESCLUB_ILU_02-*.png")):
        process_png(path)


if __name__ == "__main__":
    main()
