import pyautogui
import pyperclip

def sending_email(to, subject, message):
    pyautogui.hotkey("alt", "tab")
    pyautogui.hotkey("ctrl", "t")
    pyautogui.PAUSE = 2 
    pyperclip.copy("www.gmail.com")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("enter")
    pyautogui.moveTo(150, 230)
    pyautogui.click()
    pyperclip.copy(to)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("tab")
    pyperclip.copy(subject)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("tab")
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.hotkey("tab")
    pyautogui.hotkey("enter")

sending_email('lcarchedi@hotmail.com', 'email to hotmail', 'if this message arrives, it works!')