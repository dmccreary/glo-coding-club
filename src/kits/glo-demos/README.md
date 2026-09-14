# glo-demos Kit (GLO / Griffins Logos on GC9B72)

A Raspberry Pi Pico wired to a 2.1" round GC9B72 SPI display, showing the
[GLO logo](../../../docs/img/glo-logo-white.png) and the
[Groves Griffins circle badge](../../../docs/img/griffins-circle-logo.png).
The wiring, driver, and `config.py` are adapted from the `sw-gc9b72` /
`thinking-spot-demos` kits in the sibling `thinking-spot-demos` repo -- same
board, same GC9B72 driver, same fonts.

Two logos ship, each flattened onto its own solid background: the GLO
wordmark on white, and the Griffins circle badge on black (so the
transparent corners outside the circle blend into the display's bezel).

## Files

| File | Purpose |
|---|---|
| `convert_logo.py` | Host-side tool (needs Pillow). Flattens each source PNG's alpha channel onto a solid background, resizes to 360x360, and dumps it as raw RGB565 pixels. Run this on your computer, not the Pico. |
| `glo-logo.rgb565` | The GLO wordmark, flattened onto white, resized to 360x360 RGB565 -- 259,200 bytes, checked in so the kit works without re-running the converter. |
| `griffins-logo.rgb565` | The Griffins circle badge, flattened onto black, same size, also checked in. |
| `01-glo-logo.py` | Reads `glo-logo.rgb565` back a few rows at a time and blits it to the display, white background. |
| `02-griffins-logo.py` | Same as `01-glo-logo.py` but reads `griffins-logo.rgb565` and fills the screen black first instead of white. |
| `demo.py` | Multi-mode showcase (both logos plus a rainbow title, color wheel, gauge, and watch/weather mockups) -- button A/B cycle through modes. |
| `config.py`, `lib/` | GC9B72 driver, pin config, and fonts for the Pico + round display. |
| `upload-code.sh` | Uploads everything above (except `convert_logo.py`, which never runs on the Pico) to a connected Pico via `mpremote`. |

Rename whichever lab you want to run automatically to `main.py` before
uploading -- MicroPython always runs `main.py` a few seconds after
power-on.

## How the logos are flattened

Both `docs/img/glo-logo-white.png` and `docs/img/griffins-circle-logo.png`
have an alpha channel (transparent outside the artwork), which the GC9B72
can't display -- every pixel needs a solid RGB value. `convert_logo.py`
pastes each PNG onto a solid background (white for GLO, black for
Griffins) using its own alpha channel as the paste mask, pads it onto a
square canvas of the same background color if it isn't already square (the
GLO wordmark is wider than tall), then resizes to 360x360.

## Why the image is streamed instead of loaded whole

The Pico's RP2040 has 264 KB of RAM total. A full 360x360 RGB565 frame is
259,200 bytes -- 98% of every byte on the chip, before MicroPython's own
interpreter and heap take their share. Neither lab holds the whole image
in memory: each reads `ROWS_PER_CHUNK` rows (14,400 bytes) from its
`.rgb565` file at a time and blits each chunk before reading the next, so
memory use stays small and constant regardless of image size.

## Regenerating the logo assets

If `docs/img/glo-logo-white.png` or `docs/img/griffins-circle-logo.png`
change, regenerate both on-device assets:

```bash
pip install pillow
python3 convert_logo.py
```

## Running it

```bash
./upload-code.sh
```

Then, on the Pico (via Thonny or `mpremote run 01-glo-logo.py` /
`mpremote run 02-griffins-logo.py`), run whichever lab you want.
