from pynput import keyboard
import pyautogui

def on_press(key):
    try:
        print("Alphanumeric key pressed: {0} ".format(key.char))
        if key.char == 'f':
            pyautogui.keyDown('f');
            print("f key pressed")
    except AttributeError:
        print("special key pressed: {0}".format(key))


def on_release(key):
    print("Key released: {0}".format(key))
    if key == keyboard.Key.esc:
        pyautogui.keyUp('f')
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
