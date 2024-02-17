import time
import pyautogui


# i=0
# for i in range (50):
# pyautogui.write("Hi")
# time.sleep(0.2)
# pyautogui.press("enter")
# custom specific resolutions so need to be changed based on one's own resolutions to auto-navigate to whatsapp and message on it own
# Be responsible with pyautogui and always remember to fail-stop
time.sleep(2)
pyautogui.moveTo(1243,1078,0.2) # x=1243, y=1041 (to task manager)
time.sleep(1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(255,389,0.2) #Point(x=255, y=389)
time.sleep(1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(846,1035,0.2) # Point(x=846, y=1035)
time.sleep(1)
pyautogui.leftClick()
time.sleep(1)
pyautogui.write("Hello, Welcome to the Bot's world!",0.2)
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("I navigated myself through here",0.2)
time.sleep(1)
pyautogui.press("enter")