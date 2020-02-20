import random
from reboot import *

keyboard = Controller()


def knuth_shuffle(list):
    for i in range(len(list) - 1, 0, -1):
        p = random.randrange(0, i + 1)
        list[i], list[p] = list[p], list[i]
    return list


letters = ['a', 'd', 'f', 'z', 'x', '6', '7', '8']


def random_actions():
    time.sleep(random.randint(5, 30))
    letters_shuffle = knuth_shuffle(letters)
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


