from pynput.keyboard import Key, Controller
import time
from mousePosition import *

keyboard = Controller()


def reboot():
    time.sleep(10)
    mouse.position = (login_x, login_y)
    time.sleep(3)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(3)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(3)
    mouse.position = (launch_x, launch_y)
    time.sleep(30)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(30)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

