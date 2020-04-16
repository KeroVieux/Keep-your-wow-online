import random
from reboot import *

keyboard = Controller()


# letters = ['a', 'd', 'f', 'z', 'x', '6', '7', '8']
letters = ['1', '2', '3', '4', '5', '6', '7', '8']


def random_actions():
    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)
    # time.sleep(1)
    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)
    # time.sleep(3)
    random.shuffle(letters)
    keyboard.press(letters[0])
    keyboard.release(letters[0])

    random_event = random.randint(0, 10)
    if 1 < random_event < 5:
        time.sleep(3)
        keyboard.press(letters[1])
        keyboard.release(letters[1])

    if random_event > 5:
        time.sleep(3)
        keyboard.press(letters[2])
        keyboard.release(letters[2])

    if random_event < 8:
        time.sleep(3)
        keyboard.press(Key.space)
        keyboard.release(Key.space)


random_actions()