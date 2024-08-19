import os
import time
try:
    import pydirectinput
    import pyautogui
    # pip install opencv-python
except ImportError:
    os.system("pip install pyautogui")
    os.system("pip install opencv-python")
    os.system("pip install pydirectinput")

autoMove = False # Automatically moves for multi hatch
timeOut = 0
while True:
    buy = pyautogui.locateCenterOnScreen('buy.png', confidence=0.725)
    buy2 = pyautogui.locateCenterOnScreen('buy2.png', confidence=0.725)
    buy3 = pyautogui.locateCenterOnScreen('buy3.png', confidence=0.725)

    if buy or buy2 or buy3:
        x, y = buy or buy2 or buy3
        pydirectinput.moveTo(x, y)
        pydirectinput.move(5, None)
        pyautogui.mouseDown()
        pydirectinput.click()
        pyautogui.click(clicks=1)
        time.sleep(0.1)
        pyautogui.mouseUp()
        pydirectinput.click()
        pyautogui.click(clicks=1)
        print(f"Clicked buy button on {x, y}")
        timeOut += 0.1
    if timeOut >= 30:
        timeOut = 0
        pydirectinput.keyDown('s')
        time.sleep(1.2)
        pydirectinput.keyUp('s')
        time.sleep(0.1)
        pydirectinput.keyDown('w')
        time.sleep(1.2)
        pydirectinput.keyUp('w')
    
    timeOut += 0.2
    print(timeOut)
    time.sleep(0.1)
