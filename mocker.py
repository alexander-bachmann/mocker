import random
import pyautogui
import pytesseract
import pyperclip
import speech_recognition as sr
from pynput.mouse import Listener


class Mocker:
    def __init__(self):
        self.top_left_x = 0
        self.top_left_y = 0
        self.bot_right_x = 0
        self.bot_right_y = 0
        self.click_x = 0
        self.click_y = 0
        self.mock_image = True
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
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


    def microphone_listen(self):
        self.mock_image = False

        r = sr.Recognizer()
        with sr.Microphone() as source:
            # print("Say something!")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            # print("Google Speech Recognition thinks you said " + text)
            self.sentence = text

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))



    def get_screenshot_coordinates(self):
        self.listen()
        self.top_left_x = self.click_x
        self.top_left_y = self.click_y
        self.listen()
        self.bot_right_x = self.click_x
        self.bot_right_y = self.click_y


    def take_screenshot(self):
        self.mock_image = True
        width = self.bot_right_x - self.top_left_x
        height = self.bot_right_y - self.top_left_y
        screenshot = pyautogui.screenshot(region=(self.top_left_x, self.top_left_y, width, height))
        screenshot.save("to_mock.png")
        self.sentence = pytesseract.image_to_string("to_mock.png")
        return screenshot


    # changes the self.sentence for every type of mock
    def spongebob_mock(self):
        if self.mock_image == True:
            mock_sentence = pytesseract.image_to_string("to_mock.png")
        else:
            mock_sentence = self.sentence

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
        if self.mock_image == True:
            mock_sentence = pytesseract.image_to_string("to_mock.png")
        else:
            mock_sentence = self.sentence

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
        if self.mock_image == True:
            mock_sentence = pytesseract.image_to_string("to_mock.png")
        else:
            mock_sentence = self.sentence

        mocked_sentence = list(mock_sentence)
        mocked_sentence.reverse()

        mocked_sentence = "".join(mocked_sentence)

        pyperclip.copy(mocked_sentence)
        self.sentence = mocked_sentence
        return mocked_sentence
