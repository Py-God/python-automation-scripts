import pyautogui, time

def commentAfterDelay():
    pyautogui.click(100, 400)
    pyautogui.typewrite('In IDLE, Alt-3 comments out a line.')
    time.sleep(2)
    pyautogui.hotkey('alt', '3')
commentAfterDelay()