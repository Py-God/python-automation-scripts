#! python3
# a script to nudge your mouse cursor slightly every ten seconds.

import time, pyautogui

def busyMouse():
    tim = 0
    while tim < 10:
        time.sleep(1)
        tim += 1
    pyautogui.moveRel(2, 2)

for i in range(1000):
    busyMouse()
