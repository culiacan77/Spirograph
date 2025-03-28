# SPDX-FileCopyrightText: 2024 Jacques Supcik
#
# SPDX-License-Identifier: Apache-2.0

"""
`buzzer`
=======================================================================

Interface to Picomo buzzer

* Author(s): Jacques Supcik <jacques.supcik@hefr.ch>

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases
"""

import time

import board
import pwmio


class Buzzer:
    def __init__(self, frequency=4000):
        self._buzzer = pwmio.PWMOut(board.BUZZER, frequency=frequency, duty_cycle=0)

    def play(self, duration=0.1):
        self._buzzer.duty_cycle = 2**15
        time.sleep(duration)
        self._buzzer.duty_cycle = 0
