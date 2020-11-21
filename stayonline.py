import pyautogui
# how many pixels you want your mouse to move by
pixel = 20
while True:
    pixel *= -1
    pyautogui.moveRel(0, pixel, duration=.2)
