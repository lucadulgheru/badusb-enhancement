from adafruit_hid.keyboard import Keyboard
from command_names import *
from keyboard_handler import *

import usb_hid
import time

payload = HELLO_WORLD

keyboard = Keyboard(usb_hid.devices)
time.sleep(0.5)

keyboard_handler = KeyboardHandler(keyboard, 'MAC')

print('Opening up terminal')
keyboard_handler.open_terminal()

print('Running script HELLO_WORLD')
keyboard_handler.type_command(payload)