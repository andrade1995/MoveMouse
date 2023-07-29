import pyautogui as pgui
import time

while(True):
    pgui.moveTo(100,100, duration=1)
    pgui.moveTo(200,100, duration=1)
    pgui.moveTo(300,100, duration=1)
    pgui.press('left')