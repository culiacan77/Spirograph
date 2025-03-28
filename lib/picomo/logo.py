# SPDX-FileCopyrightText: 2024 Jacques Supcik
#
# SPDX-License-Identifier: Apache-2.0

"""
`logo`
=======================================================================

Picomo logo

* Author(s): Jacques Supcik <jacques.supcik@hefr.ch>

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

import re

import displayio


class Logo(displayio.TileGrid):
    def __init__(self):
        file_name = re.sub(r"(.*)\.m?py", r"\1.bmp", __file__)
        self._bitmap = displayio.OnDiskBitmap(file_name)
        super().__init__(self._bitmap, pixel_shader=self._bitmap.pixel_shader)
