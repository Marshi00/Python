from tkinter import *
from tkinter import messagebox
import random
import pandas

# ----------------------------Variables------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
file_okay = False
# ---------------------------- File Control ------------------------------- #
try:
    data = pandas.read_csv("words_to_learn.csv")
    to_learn = data.to_dict(orient="records")
    file_okay = True
except FileNotFoundError:
    try:
        original_data = pandas.read_csv("data/french_words.csv")
        to_learn = original_data.to_dict(orient="records")
        file_okay = True
    except FileNotFoundError:
        messagebox.showinfo(title="missing", message="The french_words file doesn't exist ")
        file_okay = False


# ---------------------------- CARD GENERATOR ------------------------------- #

def right():
    try:
        to_learn.remove(current_card)
        save_data = pandas.DataFrame(to_learn)
        save_data.to_csv("data/words_to_learn.csv")
    except ValueError:
        print("...")
    next_card()


def wrong():
    next_card()


def flip_card():
    try:
        canvas.itemconfig(card_title, text="English", fill="white")
        canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    except KeyError:
        messagebox.showinfo(title="missing", message="There is no current card ")
    else:
        canvas.itemconfig(canvas_img, image=card_back_img)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    try:
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_title, text="French", fill="black")
    except KeyError:
        messagebox.showinfo(title="missing", message="There is no current card ")
    else:
        canvas.itemconfig(canvas_img, image=card_front_img)
        flip_timer = window.after(3000, func=flip_card)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(height=800, width=900, bg=BACKGROUND_COLOR, highlightthickness=0)
window.minsize(height=800, width=900)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
canvas_img = canvas.create_image(400, 300, image=card_front_img)
canvas.place(x=0, y=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="Word", font=("Ariel", 60, "bold"))
# calls start_timer() when pressed
button_right = Button(command=right, image=right_img, highlightthickness=0)
button_right.place(x=200, y=600)

# calls start_timer() when pressed
button_wrong = Button(command=wrong, image=wrong_img, highlightthickness=0)
button_wrong.place(x=500, y=600)
next_card()
window.mainloop()
