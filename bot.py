import pyautogui
import time
import keyboard

import win32api, win32con

#Maping the game window
#Click on the 4 colums of tiles so the bot knows where they are
x_pos_list=[]
while len(x_pos_list) < 4:
   cursor_pos = pyautogui.position()
   if keyboard.is_pressed('w') == True:
      y=cursor_pos[1]
      if cursor_pos[0] not in x_pos_list:
         x_pos_list.append(cursor_pos[0])
      #print(x_pos_list)

def click(x,y):
   win32api.SetCursorPos((x,y))
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
   time.sleep(0.1)
   win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
   print('click')

while keyboard.is_pressed('q') == False:

   x=x_pos_list[0]
   if pyautogui.pixel(x,y)[0] == 0:
      click(x,y)

   x=x_pos_list[1]
   if pyautogui.pixel(x,y)[0] == 0:
      click(x,y)

   x=x_pos_list[2]
   if pyautogui.pixel(x,y)[0] == 0:
      click(x,y)

   x=x_pos_list[3]
   if pyautogui.pixel(x,y)[0] == 0:
      click(x,y)
