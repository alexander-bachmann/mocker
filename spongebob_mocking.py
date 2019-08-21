"""
GUI
take screenshot - notification copied to clipboard

display screenshot that was taken
display text that was generated


"""

import random # generating the mocked sentence
import pyperclip # to add to clipboard
from PIL import Image
import pyautogui # to take screenshot
import pytesseract # image to string
from pynput.mouse import Listener # to listen to mouse clicks
import tkinter as tk # gui

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

class Mocker:
    def __init__(self):
        self.top_left_x = 0
        self.top_left_y = 0
        self.bot_right_x = 0
        self.bot_right_y = 0

        self.click_x = 0
        self.click_y = 0

    def on_click(self, x, y, button, pressed):
        if pressed:
            # print ('Clicked ({0}, {1})'.format(x, y))
            self.click_x = x
            self.click_y = y

        if not pressed:
            return False


    def listen(self):
        with Listener(on_click=self.on_click) as listener:
            listener.join()
        return
        # print("Finished listening")


    def get_screenshot_coordinates(self):
        # print("To take screenshot: right click top left and bottom right of area")
        self.listen()
        self.top_left_x = self.click_x
        self.top_left_y = self.click_y
        self.listen()
        self.bot_right_x = self.click_x
        self.bot_right_y = self.click_y
        # print("Top left: x = " + str(self.top_left_x) + " y = " + str(self.top_left_y))
        # print("Bot right: x = " + str(self.bot_right_x) + " y = " + str(self.bot_right_y))


    def take_screenshot(self):
        width = self.bot_right_x - self.top_left_x
        height = self.bot_right_y - self.top_left_y
        screenshot = pyautogui.screenshot(region=(self.top_left_x, self.top_left_y, width, height))
        screenshot.save("to_mock.png")
        # print("screenshot saved")

        return screenshot


    def mock(self):
        mock_sentence = pytesseract.image_to_string("to_mock.png")

        mock_sentence = mock_sentence.lower()
        mock_sentence = list(mock_sentence)
        mocked = []

        for i in range(len(mock_sentence)):
            up_low_rand = random.randint(0, 1)

            if up_low_rand == 1:
                mocked += mock_sentence[i].upper()
            else:
                mocked += mock_sentence[i]

            if i > 1:
                if mocked[i].islower() and mocked[i - 1].islower() and mocked[i - 2].islower():
                    mocked[i] = mocked[i].upper()

                elif mocked[i].isupper() and mocked[i - 1].isupper() and mocked[i - 2].isupper():
                    mocked[i] = mocked[i].lower()

        mocked_sentence = "".join(mocked)
        # adding to clipboard
        pyperclip.copy(mocked_sentence)
        return mocked_sentence


def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func


class GUI:
    def __init__(self, master):
        self.master = master
        self.mocker = Mocker()
        self.current_screenshot = tk.PhotoImage(file="to_mock.png")
        self.screenshot_label = tk.Label(self.master, image=self.current_screenshot)
        self.screenshot_label.pack()
        self.screenshot_button = tk.Button(self.master, text="SCREENSHOT (right click NW and SE)", command=combine_funcs(self.mocker.get_screenshot_coordinates, self.mocker.take_screenshot, self.mocker.mock, self.update_labels))
        self.screenshot_button.pack(side="bottom")

    def update_labels(self):
        self.screenshot_label.pack_forget()
        self.current_screenshot = tk.PhotoImage(file="to_mock.png")
        self.screenshot_label = tk.Label(self.master, image=self.current_screenshot)
        self.screenshot_label.pack()


gui = tk.Tk()
gui.title("Spongebob Mocker")
GUI(gui)
gui.mainloop()
