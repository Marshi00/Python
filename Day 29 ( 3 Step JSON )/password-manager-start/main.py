from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)
    password = ''.join(password_list)

    entry_3.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- Search PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            new_data = json.load(data_file)
            website = entry_1.get()
    except FileNotFoundError:
        messagebox.showinfo(title="missing", message="The JSON record file doesn't exist ")
    else:
        if website in new_data:
            email = new_data[website]["email"]
            password = new_data[website]["password"]
            messagebox.showinfo(title="Record", message=f"These are the record found for {website}: \n "
                                                        f"{email}\n {password} \n ")
        else:
            messagebox.showinfo(title="missing", message="Couldn't find any related record")
    finally:
        entry_1.delete(0, END)
        entry_3.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="missing", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.showinfo(title=website, message=f"These are the details entered: \n "
                                                           f"{email}\n {password} \n Is it ok to save?")
        if is_ok:
            new_json_dict = {
                website: {
                    "email": email,
                    "password": password

                }
            }
            try:
                with open("data.json", "r") as data_file:
                    # Reading old data
                    new_data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_json_dict, data_file, indent=4)
            else:
                # Updating old data with new data
                updated_data = new_data.update(new_json_dict)
                # Saving new data
                with open("data.json", "w") as data_file2:
                    json.dump(updated_data, data_file2, indent=4)
            finally:
                entry_1.delete(0, END)
                entry_3.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("GUI")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
# Labels
label_1 = Label(text="Website:")
label_1.grid(row=1, column=0)

label_2 = Label(text="Email/Username:")
label_2.grid(row=2, column=0)

label_3 = Label(text="Password:")
label_3.grid(row=3, column=0)

# Buttons


# calls start_timer() when pressed
button_1 = Button(text="Generate Password", command=generate_password)
button_1.grid(row=3, column=2, sticky="EW")

# calls start_timer() when pressed
button_2 = Button(text="Add", command=save, width=36)
button_2.grid(row=4, column=1, columnspan=2, sticky="EW")

button_3 = Button(text="Search", command=find_password, bg="yellow")
button_3.grid(row=1, column=2, sticky="EW")

# Entries
entry_1 = Entry()
entry_1.grid(row=1, column=1, sticky="EW")
entry_1.focus()

entry_2 = Entry(width=35)
entry_2.grid(row=2, column=1, columnspan=2, sticky="EW")
entry_2.insert(0, "idk@gmail.com")

entry_3 = Entry(width=21)
entry_3.grid(row=3, column=1, sticky="EW")
window.mainloop()
