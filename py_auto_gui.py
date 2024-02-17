#import relevant modules

import time
import pyautogui

# give python file some time before continuing
# time.sleep(1) 
# Mouse functions
# print(pyautogui.size()) # to print display resolution of the screen
# print(pyautogui.displayMousePosition())
# print(pyautogui.position())# prints the current position of the mouse

# pyautogui.moveTo(28,365)

# to draw automatic square circle in the pait app given the time sleep 2 to navigate to paint

time.sleep(3)
distance = 503
while distance>1:
    pyautogui.dragRel(distance,0,1,button = 'left')
    pyautogui.dragRel(0,distance,1,button = 'left')
    distance -=20
    pyautogui.dragRel(-distance,0,1,button = 'left')
    pyautogui.dragRel(0,-distance,1,button = 'left')
    distance -=20
    time.sleep(0)