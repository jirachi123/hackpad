import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.extensions.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

PINS = [board.D1, board.D2, board.D3, board.D4]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# encoder 
encoder = EncoderHandler()
encoder.pins = (
    (board.D6, board.D7),  # left encoder
)
keyboard.extensions.append(encoder)

def handle_encoder_0(index, direction):
    if direction == 1:
        keyboard.send(KC.VOLU)  # volume up
    elif direction == -1:
        keyboard.send(KC.VOLD)  # volume down

encoder.handlers = [handle_encoder_0]

keyboard.keymap = [
    [KC.AUDIO_MUTE, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP, KC.MEDIA_NEXT_TRACK]
]

if __name__ == '__main__':
    keyboard.go()