BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

window = Tk()
window.minsize(900, 700)
window.config(padx=50, pady=0, bg=BACKGROUND_COLOR)
window.title("Flashy")
# ------------------------------ACCESSING THE FILES IN THE CSV FILE----------------------------------------------------
data_list = {}
current_word = {}
try:
    data = pandas.read_csv("data/to_be_learned.csv")
except FileNotFoundError:
    file = pandas.read_csv("data/french_words.csv")
    data_list = file.to_dict(orient="records")
    print(data_list)

else:
    data_list = data.to_dict(orient="records")
    print(data_list)


def french_word():
    global current_word
    current_word = random.choice(data_list)
    canvas.itemconfig(card, image=front_photo)
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=current_word["French"])
    canvas.after(3000, reveal_back)


# ----------------------------THE BACK OF THE CARD-------------------------------------------------------------

def reveal_back():
    eng_word = current_word["English"]
    canvas.itemconfig(card, image=back_photo)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=eng_word)


# --------------------------remove words that are already known---------------------------
def is_known():
    if current_word:
        data_list.remove(current_word)
    to_be_learned = pandas.DataFrame(data_list)
    to_be_learned.to_csv("data/to_be_learned.csv", index=False)
    french_word()


# ------------------------the interface of the program-------------------------------
front_photo = PhotoImage(file="images/card_front.png")
back_photo = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=600, highlightthickness=0, bg=BACKGROUND_COLOR)
card = canvas.create_image(400, 300, image=front_photo)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 300, text="Word", font=("Ariel", 60, "italic"))

canvas.grid(column=0, row=0, columnspan=2)

# -----------------------the right and wrong buttons---------------------------------
x_image = PhotoImage(file="images/wrong.png")
button1 = Button(width=400, height=100, image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0,
                 activebackground=BACKGROUND_COLOR, command=french_word)
button1.grid(column=0, row=1)

r_image = PhotoImage(file="images/right.png")
button2 = Button(width=400, height=100, image=r_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0,
                 activebackground=BACKGROUND_COLOR, command=is_known)
button2.grid(column=1, row=1)

window.mainloop()
