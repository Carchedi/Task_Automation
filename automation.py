import pyautogui
import pyperclip

pyautogui.hotkey("alt", "tab")
pyautogui.hotkey("ctrl", "t")
pyautogui.PAUSE = 2 
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
pyautogui.moveTo(220, 320)
pyautogui.click()
pyperclip.copy("carchedi.ufjf@gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy("Email de teste")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy("Enviando o primeiro email automatizado com o python!!!")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyautogui.hotkey("enter")