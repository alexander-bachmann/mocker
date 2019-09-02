"""
GUI

buttons to add:
pig latin -  Igpay Atinlay
text-box to paste/type into

create default to_mock.png and use that when program opens
reset (to fix if to_mock.png breaks)

separate into multiple class files
instead of one large single .py file


add to README.md
    packages/modules install commands
    screen shots of program working
    explanation and thought process behind program
    why certain modules are used and for what



random # generating the mocked sentence
pyperclip # to add to clipboard
from PIL import Image
pyautogui # to take screenshot
pytesseract # image to string
pynput.mouse import Listener # to listen to mouse clicks
tkinter for gui
"""

from mocker import Mocker
from gui import GUI
import tkinter as tk


if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Mock by Bok")
    GUI(gui)
    gui.mainloop()
