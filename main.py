import os
import time

try:
    import pydirectinput
    import pyautogui
except ImportError:
    os.system("pip install pyautogui opencv-python pydirectinput")

auto_move = False  # Automatically moves for multiple dice hatch

timeout = 0

image_files = ['buy.png', 'buy2.png', 'buy3.png', 'buy4.png', 'ok.png', 'ok2.png']

while True:
    button_clicked = False
    
    for image_file in image_files:
        confidence_level = 0.7
        if image_file in ['ok.png', 'ok2.png']:
            confidence_level = 0.8
        button_location = pyautogui.locateCenterOnScreen(image_file, confidence=confidence_level)
        if button_location:
            x, y = button_location
            pydirectinput.moveTo(x, y)
            pydirectinput.move(5, None)
            pyautogui.mouseDown()
            pydirectinput.click()
            pyautogui.click(clicks=1)
            print(f"Clicked button at ({x}, {y})")
            button_clicked = True
            if auto_move:
                timeout += 0.1
            break

    if auto_move:
        if timeout >= 30:
            timeout = 0
            pydirectinput.keyDown('s')
            time.sleep(1)
            pydirectinput.keyUp('s')
            time.sleep(0.1)
            pydirectinput.keyDown('w')
            time.sleep(1)
            pydirectinput.keyUp('w')
        else:
            timeout += 0.2
            print(timeout)
    
    time.sleep(0.1)
