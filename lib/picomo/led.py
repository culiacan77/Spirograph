# SPDX-FileCopyrightText: 2024 Jacques Supcik
#
# SPDX-License-Identifier: Apache-2.0

"""
`led`
=======================================================================

Interface to Picomo RGB LED

* Author(s): Jacques Supcik <jacques.supcik@hefr.ch>

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
* Adafruit RGB LED library:
  https://github.com/adafruit/Adafruit_CircuitPython_RGBLED
"""

import adafruit_rgbled
import board
import pwmio


class RGBLed:
    def __init__(self, frequency=4000):
        r = pwmio.PWMOut(board.LED_R, frequency=frequency, duty_cycle=0)
        g = pwmio.PWMOut(board.LED_G, frequency=frequency, duty_cycle=0)
        b = pwmio.PWMOut(board.LED_B, frequency=frequency, duty_cycle=0)
        self._led = adafruit_rgbled.RGBLED(r, g, b)

    def set(self, color):
        self._led.color = color

    def off(self):
        self._led.color = (0, 0, 0)
