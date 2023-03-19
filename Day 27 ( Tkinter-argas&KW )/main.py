from tkinter import *

# window = tkinter.Tk()
window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
"""
# Label
label_1 = tkinter.Label(text="I am label", font=("Arial", 24, "bold"))
label_1.place(x=100, y=25)
label_1.config(text="new Text")
label_1["text"] = "huh"
label_2 = tkinter.Label(text="I am label 2", font=("Arial", 24, "bold"))
label_2.pack(side="left")
# Button


def button_1_clicked():
    label_1["text"] = button_1["text"]
    label_2.config(text=input_1.get())


button_1 = tkinter.Button(text="click", command=button_1_clicked)
# coordinating for responsive location based on row / col
# button_1.grid(column=0, row=0)
button_1.pack()


# Entry

input_1 = tkinter.Entry()
input_1.get()
input_1.pack()
"""
"""
def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(2, 4, 5, 6, 7))


class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make", "toyota")
        self.model = kwargs.get("model")


my_car = Car(makee="Nissan", model="GT-R")
print(my_car.make)
"""
# Entries
entry_1 = Entry(width=10)
# Add some text to begin with
entry_1.insert(END, string="0")
entry_1.grid(row=0, column=1)

# Labels
label_1 = Label(text="Miles")
label_1.grid(row=0, column=2)

label_2 = Label(text="is equal to")
label_2.grid(row=1, column=0)

label_3 = Label(text="KM")
label_3.grid(row=1, column=2)

label_4 = Label(text="0")
label_4.grid(row=1, column=1)


# Buttons
def action():
    result = round(float(entry_1.get()) * 1.609344, 2)
    label_4.config(text=result)


# calls action() when pressed
button_1 = Button(text="Calculate", command=action)
button_1.grid(row=2, column=1)

window.mainloop()
