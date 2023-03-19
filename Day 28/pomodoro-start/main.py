import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    button_1.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        label_1.config(text="Long Break")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_1.config(text="Short Break")
    else:
        count_down(work_sec)
        label_1.config(text="Work")


def reset_timer():
    global reps
    window.after_cancel(timer)
    label_1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label_2.config(text="")
    reps = 0
    button_1.config(state="normal")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ""
        start_timer()
        work_sessions = math.floor(reps / 2)
        for sessions in range(work_sessions):
            marks += "✔"
        label_2.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("GUI")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150, 170, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.place(x=50, y=50)

# Labels
label_1 = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
label_1.place(x=130, y=10)

label_2 = Label(font=(FONT_NAME, 25, "bold"), fg=GREEN)
label_2.place(x=180, y=350)

# Buttons

# calls start_timer() when pressed
button_1 = Button(text="Start", command=start_timer)
button_1.place(x=50, y=320)

# calls reset_timer() when pressed
button_2 = Button(text="Reset", command=reset_timer)
button_2.place(x=310, y=320)

window.mainloop()
