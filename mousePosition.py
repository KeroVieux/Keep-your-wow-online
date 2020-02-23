from pynput.mouse import Button, Controller as MouseController

mouse = MouseController()
launch_x, launch_y = 2973.2890625, 1018.0859375
login_x, login_y = 3427.703125, 504.42578125

print('The current pointer position is {0}'.format(
    mouse.position))
