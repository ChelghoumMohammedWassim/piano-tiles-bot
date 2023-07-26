from pyautogui import *
import pyautogui
import time
import keyboard
import win32api,win32con

y=900

rows_positions=[
    1276,
    1380,
    1480,
    1580
]

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

print('bot started')


while keyboard.is_pressed('*')==False:
    
    for row in rows_positions:
        if pyautogui.pixel(row,y)[0]==0:
            click(row,y)
            print('mouse clicked  in row:'+str(rows_positions.index(row)))

#game:  https://www.primarygames.com/arcade/music/pianotiles/mobile/
#run mouseScanner.py to update y and rows