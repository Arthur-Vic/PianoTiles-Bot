from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tile1 Position: x=600 y=600
#tile1 Position: x=690 y=600
#tile1 Position: x=780 y=600
#tile1 Position: x=870 y=600

def click(x,y):
   win32api.SetCursorPos((x,y))
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
   time.sleep(0.1)
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
   print('click')

y=500
while keyboard.is_pressed('q') == False:
   if pyautogui.pixel(600,500)[0] == 0:
      x=600
      click(x,y)

   if pyautogui.pixel(690,500)[0] == 0:
      x=690
      click(x,y)

   if pyautogui.pixel(780,500)[0] == 0:
      x=780
      click(x,y)

   if pyautogui.pixel(870,500)[0] == 0:
      x=870
      click(x,y)