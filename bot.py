import time
import pyautogui


def SpamSender():
    time.sleep(5)
    text = open("shrek.txt")
    for each_line in text:
        pyautogui.typewrite(each_line)
        pyautogui.press("enter")


SpamSender()
