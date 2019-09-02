"""
GUI

buttons to add:
pig latin -  Igpay Atinlay
text-box to paste/type into

create default to_mock.png and use that when program opens
reset (to fix if to_mock.png breaks)

add comments to each function that isn't easily readable

combine_funcs - maybe remove or find better way for buttons

add to README.md
    packages/modules install commands
    screen shots of program working
    explanation and thought process behind program
    why certain modules are used and for what


Modules and their use:
    random - used in randomizing the capitalization in the spongebob mock
    pyperclip - adds the mocked text to the user's clipboard
    pyautogui - take screenshot of sentence user is wishing to mock
    pytesseract - converts text from screenshot into useable string
    pynput.mouse's Listener - listen to mouse clicks for screenshot dimensions
    tkinter - graphical user interface
"""


from mocker import Mocker
from gui import GUI
import tkinter as tk


if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Mock by Bok")
    GUI(gui)
    gui.mainloop()
