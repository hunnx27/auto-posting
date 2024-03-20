
import pyautogui
import pyperclip
import time

class AutoGpt:

    def __init__(self):
        print('init')

    def searchGPT(self, text):
        pyautogui.hotkey("alt", "tab")
        pyperclip.copy(text)
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(1)
        pyautogui.hotkey("enter")
        time.sleep(20)
        pyautogui.hotkey("ctrl", "shift", "c")
        paste = pyperclip.paste()
        print(paste)
        return paste