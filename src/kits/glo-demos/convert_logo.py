#!/usr/bin/env python3
# Converts docs/img/glo-logo-white.png and docs/img/griffins-circle-logo.png
# into raw RGB565 pixel dumps the GC9B72 driver can stream straight to the
# display.
#
# Run this on your computer (needs Pillow), not the Pico -- MicroPython has
# no PNG decoder. It produces two files:
#
#   glo-logo.rgb565       the GLO wordmark, flattened onto white -- 01-glo-logo.py
#   griffins-logo.rgb565  the Griffins circle badge, flattened onto black --
#                          02-griffins-logo.py
#
# Both source PNGs carry an alpha channel (transparent outside the artwork),
# so each is flattened onto a solid background before conversion -- white
# for the GLO wordmark (it's designed to sit on white), black for the
# Griffins badge (its circle nearly fills the frame, so black lets it blend
# into the display's bezel). The GLO wordmark is also wider than it is
# tall, so it's padded onto a square canvas (centered, same background
# color) before resizing -- otherwise it would stretch.
#
#   pip install pillow
#   python3 convert_logo.py

import struct
from pathlib import Path

from PIL import Image

KIT_DIR = Path(__file__).resolve().parent
IMG_DIR = KIT_DIR / ".." / ".." / ".." / "docs" / "img"

# Matches config.WIDTH / config.HEIGHT for the GC9B72 panel.
DISPLAY_SIZE = 360


def rgb565(r, g, b):
    """Same packing as gc9b72.color565() and its big-endian wire format:
    5 bits red, 6 bits green, 5 bits blue, sent MSB-first (">H")."""
    return (r & 0xF8) << 8 | (g & 0xFC) << 3 | b >> 3


def image_to_rgb565(image, background):
    """Flattens the image's alpha channel onto a solid background, pads it
    onto a square canvas if it isn't one already, resizes to the display's
    resolution, and packs it as raw RGB565 bytes."""
    rgba = image.convert("RGBA")
    flat = Image.new("RGB", rgba.size, background)
    flat.paste(rgba, mask=rgba.getchannel("A"))

    w, h = flat.size
    side = max(w, h)
    square = Image.new("RGB", (side, side), background)
    square.paste(flat, ((side - w) // 2, (side - h) // 2))

    square = square.resize((DISPLAY_SIZE, DISPLAY_SIZE), Image.LANCZOS)
    pixels = square.load()
    out = bytearray(DISPLAY_SIZE * DISPLAY_SIZE * 2)
    i = 0
    for y in range(DISPLAY_SIZE):
        for x in range(DISPLAY_SIZE):
            r, g, b = pixels[x, y]
            struct.pack_into(">H", out, i, rgb565(r, g, b))
            i += 2
    return out


def write_variant(source_name, background, out_name):
    image = Image.open(IMG_DIR / source_name)
    data = image_to_rgb565(image, background)
    out_path = KIT_DIR / out_name
    out_path.write_bytes(data)
    print(f"Wrote {out_path} ({len(data):,} bytes, "
          f"{DISPLAY_SIZE}x{DISPLAY_SIZE} RGB565)")


def main():
    write_variant("glo-logo-white.png", (255, 255, 255), "glo-logo.rgb565")
    write_variant("griffins-circle-logo.png", (0, 0, 0), "griffins-logo.rgb565")


if __name__ == "__main__":
    main()
