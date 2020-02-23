from pynput.keyboard import Key, Controller
import time

keyboard = Controller()


def reload():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(3)
    keyboard.type('/camp')
    time.sleep(3)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(50)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


