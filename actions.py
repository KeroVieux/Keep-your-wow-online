import random
from reboot import *

keyboard = Controller()

randomLetter = ['q', 'w', 'e', 'a', 's', 'd', 'f', 'z', 'x']


def random_actions():
    time.sleep(random.randint(5, 30))
    will_type = randomLetter[random.randint(0, len(randomLetter) - 1)]
    keyboard.press(will_type)
    keyboard.release(will_type)

    random_event = random.randint(0, 10)
    if random_event > 1 or random_event < 5:
        time.sleep(random.randint(5, 10))
        second_will_type = randomLetter[random.randint(0, len(randomLetter) - 1)]
        keyboard.press(second_will_type)
        keyboard.release(second_will_type)

    if random_event > 5:
        time.sleep(random.randint(5, 10))
        third_will_type = randomLetter[random.randint(0, len(randomLetter) - 1)]
        keyboard.press(third_will_type)
        keyboard.release(third_will_type)

    if random_event < 8:
        time.sleep(random.randint(5, 10))
        keyboard.press(Key.space)
        keyboard.release(Key.space)


