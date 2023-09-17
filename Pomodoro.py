from tkinter import *
import math

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
counter = None


# ---------------------------- TIMER ------------------------------- #
def timers():
    global reps
    reps += 1
    if reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    elif reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    else:
        timer.config(text="Work Time", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- RESET MECHANISM ------------------------------- #
def reset_timer():
    window.after_cancel(counter)
    canvas.itemconfig(timer_text,text="00:00")
    checker.config(text="")
    timer.config(text="Timer")
    global reps
    reps=0

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, counter
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        counter = canvas.after(1000, count_down, count - 1)
    else:
        timers()
        marks = ""
        work_session = math.floor(reps / 2)
        for i in range(work_session):
            marks += "✔"
        checker.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=120, pady=50, bg=YELLOW)
canvas = Canvas(width=300, height=324, bg=YELLOW, highlightthickness=0)
photo = PhotoImage(file="tomato.png")
canvas.create_image(150, 162, image=photo)
timer_text = canvas.create_text(150, 180, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

# labels
timer = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW)
timer.config(fg=GREEN, pady=10)
timer.grid(column=1, row=0)

checker = Label(fg=GREEN, bg=YELLOW)
checker.grid(column=1, row=2)

# Buttons
start = Button(text="Start", command=timers)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()
