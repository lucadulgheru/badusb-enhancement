from constants import TARGET_WINDOWS, TARGET_MACOS, TARGET_LINUX, TERMINAL, CMD
from time import sleep

class CommandHandler:
    
    def __init__(self, keyboard_handler, device):
        self.keyboard_handler = keyboard_handler
        self.device = device
    
    def execute_command(self, command):
        self.keyboard_handler.type_command(command)
    
    def open_commandline(self):
        self.open_search_bar()
        if self.device == TARGET_WINDOWS:
            self.open_shell(CMD)
        elif self.device == TARGET_LINUX or self.device == TARGET_MACOS:
            self.open_shell(TERMINAL)

    def open_shell(self, shell):
        for char in shell:
            self.keyboard_handler.press_key(char.upper())
        self.keyboard_handler.press_key("ENTER")
        sleep(.3)

    def open_search_bar(self):
        if self.device == TARGET_LINUX or self.device == TARGET_WINDOWS:
            self.keyboard_handler.press_key("GUI")
        elif self.device == TARGET_MACOS:
            self.keyboard_handler.simultaneous_press("COMMAND", "SPACE")
        
        