from apscheduler.schedulers.blocking import BlockingScheduler
from pynput.keyboard import Key, Controller
import random
import time
import psutil
from datetime import datetime

count = 0

keyboard = Controller()

def combine():
    global count
    count += 1
    if count % 9 is 0:
        keyboard.press('x')
        keyboard.release('x')
    elif count % 10 is 0 or count % 11 is 0 or count % 12 is 0 or count % 13 is 0:
        keyboard.press('=')
        keyboard.release('=')
    else:
        keyboard.press('s')
        time.sleep(0.5)
        keyboard.release('s')
        time.sleep(0.5)
        keyboard.press('z')
        keyboard.release('z')


scheduler = BlockingScheduler()
scheduler.add_job(combine, 'interval', seconds=5)

try:
    print('scheduler started')
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
