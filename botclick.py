from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


time.sleep(4)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (255, 219, 195)

while keyboard.is_pressed('q') == False:

    pic = pyautogui.screenshot(region=(592,142,1730,1210))

    width, height = pic.size

    for x in range(0,1730,5):
        for y in range(0,1210,5):

            r,g,b = pic.getpixel((x,y))

            if b == 195:
                click(x+592,y+142)
                time.sleep(0.06)
                break