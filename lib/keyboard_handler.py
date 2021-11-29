from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from key_mappings import *
from command_names import TERMINAL
from time import sleep

is_special_char = lambda x: x in special_characters.values()
is_letter = lambda x: (x >= 97 and x<= 122) or (x >= 65 and x<= 90)
is_uppercase_letter = lambda x: x == x.upper()

class KeyboardHandler:
    
    def __init__(self, keyboard, device):
        self.keyboard = keyboard
        self.device = device
    
    def open_terminal(self):
        if self.device == 'MAC':
            self.keyboard.send(key_strokes['COMMAND'], key_strokes['SPACE'])
            for char in TERMINAL:
                self.press_key(char.upper())
            self.press_key('ENTER')
            sleep(.5)
        else:
            print ('Not implemented')
        
    def type_command(self, command):
        for char in command:
            if is_special_char(char):
                self.press_shift_key(self.convert_special_char(char))
            elif is_letter(ord(char)) and is_uppercase_letter(char):
                self.press_shift_key(char.upper())
            else:
                self.press_key(char.upper())
        self.press_key('ENTER')
        sleep(.5)
    
    def convert_special_char(self, special_char):
        return list(special_characters.keys())[list(special_characters.values()).index(special_char)][0]
        
    def press_key(self, key):
        self.keyboard.send(key_strokes[key])
        
    def press_shift_key(self, key):
        self.keyboard.send(key_strokes['SHIFT'], key_strokes[key])
        