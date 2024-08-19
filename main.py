import os
try:
    import pydirectinput
    import pyautogui, time
    # pip install opencv-python
except ImportError:
    os.system("pip install pyautogui")
    os.system("pip install opencv-python")
    os.system("pip install pydirectinput")



while True:
    buy = pyautogui.locateCenterOnScreen('buy.png', confidence=0.725)
    if buy:
        x, y = buy
        pydirectinput.moveTo(x, y)
        pydirectinput.move(5, None)
        pyautogui.mouseDown()
        pydirectinput.click()
        pyautogui.click(clicks=1)
        time.sleep(0.1)
        pyautogui.mouseUp()
        pydirectinput.click()
        pyautogui.click(clicks=1)
        print(f"Clicked buy button on {buy}")
    time.sleep(0.1)
    