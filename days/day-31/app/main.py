from tkinter import *  # type: ignore
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
TITLE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")

# Data

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/german_words.csv")

words_dict = data.to_dict(orient="records")
current_card = {}

# functions


def save_data():
    words_to_learn = pandas.DataFrame(words_dict)
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)


def get_new_card() -> dict:
    return random.choice(words_dict)


def next_card():
    global current_card, timer

    window.after_cancel(timer)
    current_card = get_new_card()

    canvas.itemconfig(card_img,  image=front_card_img)
    canvas.itemconfig(language, text="German", fill="black")
    canvas.itemconfig(word, text=current_card["German"], fill="black")
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(card_img,  image=back_card_img)


def correct():
    words_dict.remove(current_card)
    save_data()
    next_card()


def wrong():
    next_card()


# App Window
window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, flip_card)

# Card
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=530,)
card_img = canvas.create_image(400, 265)

language = canvas.create_text(400, 150, font=TITLE_FONT, fill="black")
word = canvas.create_text(400, 263, font=WORD_FONT, fill="black")

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Correct btn
right_btn_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_btn_image,
                      highlightthickness=0, command=correct)
right_button.grid(row=1, column=1)

# Worng btn
wrong_btn_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_btn_image,
                      highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
