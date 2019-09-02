"""
GUI

buttons:
spongebob mock - SpONgEbOB
vaporwave - V A P O R  W A V E
pig latin -  Igpay Atinlay
reverse - esrever
text-box to paste/type into

create default to_mock.png and use that when program opens
reset (to fix if to_mock.png breaks)


screenshot button to take screen shot


"""

import random # generating the mocked sentence
import pyperclip # to add to clipboard
from PIL import Image
import pyautogui # to take screenshot
import pytesseract # image to string
from pynput.mouse import Listener # to listen to mouse clicks
import tkinter as tk # gui

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

class Mocker:
    def __init__(self):
        self.top_left_x = 0
        self.top_left_y = 0
        self.bot_right_x = 0
        self.bot_right_y = 0
        self.click_x = 0
        self.click_y = 0
        self.sentence = pytesseract.image_to_string("to_mock.png")

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.click_x = x
            self.click_y = y
        if not pressed:
            return False


    def listen(self):
        with Listener(on_click=self.on_click) as listener:
            listener.join()
        return


    def get_screenshot_coordinates(self):
        self.listen()
        self.top_left_x = self.click_x
        self.top_left_y = self.click_y
        self.listen()
        self.bot_right_x = self.click_x
        self.bot_right_y = self.click_y

    def take_screenshot(self):
        width = self.bot_right_x - self.top_left_x
        height = self.bot_right_y - self.top_left_y
        screenshot = pyautogui.screenshot(region=(self.top_left_x, self.top_left_y, width, height))
        screenshot.save("to_mock.png")
        self.sentence = pytesseract.image_to_string("to_mock.png")
        return screenshot

    # changes the self.sentence for every type of mock
    def spongebob_mock(self):
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
        pyperclip.copy(mocked_sentence)
        self.sentence = mocked_sentence
        return mocked_sentence


    def vaporwave_mock(self):
        mock_sentence = pytesseract.image_to_string("to_mock.png")

        mock_sentence = mock_sentence.upper()
        mocked_sentence = list(mock_sentence)
        mocked = []

        for i in range(len(mock_sentence)):
            mocked += mock_sentence[i]
            mocked += " "

        mocked_sentence = "".join(mocked)

        pyperclip.copy(mocked_sentence)
        self.sentence = mocked_sentence
        return mocked_sentence


    def reverse_mock(self):
        mock_sentence = pytesseract.image_to_string("to_mock.png")
        mocked_sentence = list(mock_sentence)
        mocked_sentence.reverse()

        mocked_sentence = "".join(mocked_sentence)

        pyperclip.copy(mocked_sentence)
        self.sentence = mocked_sentence
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

        self.screenshot_button = tk.Button(self.master, text="Screenshot (right click NW and SE)", command=combine_funcs(self.mocker.get_screenshot_coordinates, self.mocker.take_screenshot, self.update_labels))
        self.screenshot_button.pack(side="bottom")

        self.spongebob_button = tk.Button(self.master, text="SpONgEbOB", command=combine_funcs(self.mocker.spongebob_mock, self.update_labels))
        self.spongebob_button.pack(side="top")

        self.vaporwave_button = tk.Button(self.master, text = "V A P O R  W A V E", command=combine_funcs(self.mocker.vaporwave_mock, self.update_labels))
        self.vaporwave_button.pack(side="top")

        self.reverse_button = tk.Button(self.master, text = "esreveR", command=combine_funcs(self.mocker.reverse_mock, self.update_labels))
        self.reverse_button.pack(side="top")

        self.screenshot_label.pack()

        collected_text = tk.StringVar()
        self.collected_text_label = tk.Label(self.master, textvariable=collected_text)
        collected_text.set(self.mocker.sentence)
        self.collected_text_label.pack()


# BREAK UP INTO MULTIPLE UPDATES
    def update_labels(self):

        # update current screenshot
        self.current_screenshot = tk.PhotoImage(file="to_mock.png")
        self.screenshot_label.pack_forget()
        self.screenshot_label = tk.Label(self.master, image=self.current_screenshot)
        self.screenshot_label.pack(side="top")

        # updates text
        self.collected_text_label.pack_forget()
        collected_text = tk.StringVar()
        self.collected_text_label = tk.Label(self.master, textvariable=collected_text)
        collected_text.set(self.mocker.sentence)
        self.collected_text_label.pack()




if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Mock by Bok")
    GUI(gui)
    gui.mainloop()
