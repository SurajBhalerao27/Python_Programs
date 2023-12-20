import pyautogui
import time
time.sleep(10)
count=0
while(count<=500):
    pyautogui.typewrite("suraj is the best..."+str(count))
    pyautogui.press("enter")
    count += 1
# words = open("word", 'r')
# for word in words:
#     pyautogui.typewrite(word)
#     pyautogui.press("enter")
