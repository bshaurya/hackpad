#Uses KMK on a Seeed XIAO RP2040 with 4 keys + 2 SK6812 LEDs

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.extensions.rgb import RGB, AnimationModes

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

"""
SW1 -> D3
SW2 -> D4
SW3 -> D2
SW4 -> D1
LED DIN (first SK6812) -> D5
"""
PINS = [board.D3, board.D4, board.D2, board.D1]
LED_PIN = board.D5
NUM_LEDS = 2

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

#rgb
rgb = RGB(
    pixel_pin=LED_PIN,
    num_pixels=NUM_LEDS,
    val_limit=255,
    val_default=40,
    animation_mode=AnimationModes.BREATHE,
)
keyboard.extensions.append(rgb)

#e.x. macro: Save (Cmd+S on Mac; swap LCTRL for LCMD on Windows)
SAVE_MACRO = KC.MACRO(
    Press(KC.LCMD),
    Tap(KC.S),
    Release(KC.LCMD),
)
"""
Keymap:
SW1 = Play/Pause
SW2 = Next Track
SW3 = Toggle LEDs on/off
SW4 = Cycle RGB modes (solid → rainbow → breathe)
"""
keyboard.keymap = [
    [
        KC.MPLY,#SW1
        KC.MNXT,#SW2
        KC.RGB_TOG,#SW3
        KC.RGB_MODE_RAINBOW,#SW4 (press repeatedly to cycle modes)
    ]
]

if __name__ == "__main__":
    keyboard.go()
