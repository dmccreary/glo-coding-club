# Lab 02: The Groves Griffins Circle Logo
# Same idea as 01-glo-logo.py, but streams griffins-logo.rgb565: the
# Groves Griffins circle badge, flattened onto a black background so the
# transparent corners outside the circle blend into the display's bezel
# instead of showing as white.
#
# convert_logo.py builds this from docs/img/griffins-circle-logo.png --
# see image_to_rgb565() there for how the alpha channel is flattened.
#
# Rename this file to main.py (instead of 01-glo-logo.py) and copy it
# (plus config.py, lib/, and griffins-logo.rgb565) to the board's root to
# have this logo appear a few seconds after power-on with no computer
# attached.

import config

ROWS_PER_CHUNK = 20  # 360 * 20 * 2 = 14,400 bytes per chunk
ROW_BYTES = config.WIDTH * 2

display = config.init_display()
display.fill(config.BLACK)

with open("griffins-logo.rgb565", "rb") as logo:
    y = 0
    while y < config.HEIGHT:
        rows = min(ROWS_PER_CHUNK, config.HEIGHT - y)
        chunk = logo.read(ROW_BYTES * rows)
        display.blit_buffer(chunk, 0, y, config.WIDTH, rows)
        y += rows
