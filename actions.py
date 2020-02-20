import random
from reboot import *

keyboard = Controller()

letters = ['a', 'd', 'f', 'z', 'x', '6', '7', '8']


def random_actions():
    time.sleep(random.randint(5, 30))
    letters_shuffle = random.shuffle(letters)
    keyboard.press(letters_shuffle[0])
    keyboard.release(letters_shuffle[0])

    random_event = random.randint(0, 10)
    if random_event > 1 or random_event < 5:
        time.sleep(random.randint(5, 10))
        keyboard.press(letters_shuffle[1])
        keyboard.release(letters_shuffle[1])

    if random_event > 5:
        time.sleep(random.randint(5, 10))
        keyboard.press(letters_shuffle[2])
        keyboard.release(letters_shuffle[2])

    if random_event < 8:
        time.sleep(random.randint(5, 10))
        keyboard.press(Key.space)
        keyboard.release(Key.space)


