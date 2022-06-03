import usb_hid
import time

from adafruit_hid.keyboard import Keyboard
from constants import *
from keyboard_handler import KeyboardHandler
from command_handler import CommandHandler

payload = HELLO_WORLD
keyboard = Keyboard(usb_hid.devices)
time.sleep(0.3)

keyboard_handler = KeyboardHandler(keyboard)
command_handler = CommandHandler(keyboard_handler, TARGET_MACOS)

print("Opening up terminal")
command_handler.open_commandline()

print("Running script " + payload)
command_handler.execute_command(payload)