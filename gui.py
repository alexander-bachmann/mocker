from mocker import Mocker
import tkinter as tk


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
