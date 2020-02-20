from apscheduler.schedulers.blocking import BlockingScheduler
import psutil
from datetime import datetime
from reload import *
from actions import *
from reboot import *

count = 0


def combine():
    global count
    wow_process = None
    count += 1
    datetime_now = datetime.now()
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(3)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    for process in psutil.process_iter(['pid', 'name']):
        if process.name() == 'World of Warcraft Classic':
            wow_process = process
    if wow_process is not None:
        if count % 10 is 0:
            print('reload at: {0}, count={1}'.format(datetime_now, count))
            print('***')
            reload()
        elif count % 180 is 0:
            print('relaunch at: {0}, count={1}'.format(datetime_now, count))
            print('^^^')
            wow_process.kill()
            time.sleep(30)
            reboot()
        else:
            print('random actions at: {0}, count={1}'.format(datetime_now, count))
            print('---')
            random_actions()
    else:
        print('reboot at: {0}, count={1}'.format(datetime_now, count))
        print('###')
        reboot()


scheduler = BlockingScheduler()
scheduler.add_job(combine, 'interval', seconds=180)

try:
    print('scheduler started')
    scheduler.start()
except (KeyboardInterrupt, SystemExit):
    pass
