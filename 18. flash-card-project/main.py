from tkinter import *
import pandas as pd
from random import *

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = "French"
LANGUAGE_FILE = "./data/french_words.csv"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
TIMER = None
top_word = None
reps = 0

# Getting language data
try:
    words_df = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words_df = pd.read_csv(LANGUAGE_FILE)
finally:
    words_dict = {row[LANGUAGE]: row.English for (item, row) in words_df.iterrows()}


def front_card():
    global top_word, flip_timer
    window.after_cancel(flip_timer)
    top_word = choice(list(words_dict))
    canvas.itemconfig(top_text, text=top_word, fill='black')
    canvas.itemconfig(top_card, image=card_front_img)
    canvas.itemconfig(language_text, text=LANGUAGE, fill='black')
    flip_timer = window.after(3000, func=back_card)


def back_card():
    back_word = words_dict[top_word]
    canvas.itemconfig(top_card, image=card_back_img)
    canvas.itemconfig(top_text, text=back_word, fill='white')
    canvas.itemconfig(language_text, text='English', fill='white')


def correct_answer():
    words_dict.pop(top_word)
    # print(len(words_dict))
    with open("./data/words_to_learn.csv", "w") as to_learn:
        to_learn.write(f"{LANGUAGE},English\n")
        for key in words_dict.keys():
            to_learn.write("%s, %s\n" % (key, words_dict[key]))


# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=back_card)

# images
card_back_img = PhotoImage(file="./images/card_back.png")
card_front_img = PhotoImage(file="./images/card_front.png")
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
top_card = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=0, row=0, columnspan=2)

# Texts
language_text = canvas.create_text(400, 150, text="", fill="black", font=LANGUAGE_FONT)
top_text = canvas.create_text(400, 263, text="", fill="black", font=WORD_FONT)

# Buttons
button_right = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=lambda: [correct_answer(), front_card()])
button_right.grid(column=1, row=1)

button_wrong = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                      command=front_card)
button_wrong.grid(column=0, row=1)

# Running app
front_card()

window.mainloop()
