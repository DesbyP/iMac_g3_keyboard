print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.LED import LED
from kmk.extensions.led import AnimationModes

keyboard = KMKKeyboard()

keyboard.col_pins = (  # left to right
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP12,  # wiring error, 11 and 12 are interverted
    board.GP11,
    board.GP13,
    board.GP14,
    board.GP15,
    board.GP16,
    board.GP17,
    board.GP18,
)
keyboard.row_pins = (  # top to bottom
    board.GP27,
    board.GP26,
    board.GP22,
    board.GP21,
    board.GP20,
    board.GP19,
)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        # ROW
        KC.ESC,
        KC.F1,
        KC.F2,
        KC.NO,
        KC.F3,
        KC.F4,
        KC.F5,
        KC.F6,
        KC.F7,
        KC.F8,
        KC.F9,
        KC.F10,
        KC.F11,
        KC.F12,
        KC.NO,
        KC.DEL,
        KC.HOME,
        KC.END,
        KC.PGUP,
        KC.PGDOWN,
        # ROW
        KC.GRV,
        KC.N1,
        KC.N2,
        KC.N3,
        KC.N4,
        KC.N5,
        KC.N6,
        KC.N7,
        KC.N8,
        KC.N9,
        KC.N0,
        KC.MINS,
        KC.EQL,
        KC.BSPC,
        KC.NUMLOCK,
        KC.KP_SLASH,
        KC.KP_ASTERISK,
        KC.KP_MINUS,
        # ROW
        KC.TAB,
        KC.Q,
        KC.NO,
        KC.W,
        KC.E,
        KC.R,
        KC.T,
        KC.Y,
        KC.U,
        KC.I,
        KC.O,
        KC.P,
        KC.LBRC,
        KC.RBRC,
        KC.BSLS,
        KC.KP_7,
        KC.KP_8,
        KC.KP_9,
        KC.KP_PLUS,
        # ROW
        KC.CAPS,  # not sending any signal?
        KC.A,
        KC.NO,
        KC.S,
        KC.D,
        KC.F,
        KC.G,
        KC.H,
        KC.J,
        KC.K,
        KC.L,
        KC.SCLN,
        KC.QUOT,
        KC.NO,
        KC.ENT,
        KC.KP_4,
        KC.KP_5,
        KC.KP_6,
        KC.NO,
        # ROW
        KC.LSFT,
        KC.NO,
        KC.Z,
        KC.X,
        KC.C,
        KC.V,
        KC.B,
        KC.N,
        KC.M,
        KC.COMM,
        KC.DOT,
        KC.SLSH,
        KC.NO,
        KC.UP,  # RSFT
        KC.UP,
        KC.KP_1,
        KC.KP_2,
        KC.KP_3,
        KC.KP_ENTER,
        # ROW
        KC.LCTL,
        KC.LGUI,
        KC.LALT,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.SPC,
        KC.NO,
        KC.NO,
        KC.NO,
        KC.RALT,
        KC.NO,
        KC.LEFT,
        KC.DOWN,
        KC.RIGHT,
        KC.NO,
        KC.KP_0,
        KC.KP_DOT,
    ]
]

# LED
led = LED(
    led_pin=[board.GP28],
    #brightness=100,
    #brightness_step=5,
    #brightness_limit=100,
    # breathe_center=3,
    animation_mode=AnimationModes.BREATHING,
    animation_speed=0.1,
)
keyboard.extensions.append(led)

if __name__ == '__main__':
    keyboard.go()