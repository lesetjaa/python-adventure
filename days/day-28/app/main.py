from tkinter import *  # type: ignore
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
timer = None

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps

    # reset Label
    timer_label.config(text="Timer")

    # reset time
    window.after_cancel(timer)  # type: ignore
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

    # reset checks
    completion_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN * 60)
        timer_label.config(text="BREAK", foreground=RED,)

    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN * 60)
        timer_label.config(text="BREAK", foreground=PINK,)
    else:
        countdown(WORK_MIN * 60)
        timer_label.config(text="WORK", foreground=GREEN,)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # rewrite the time
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        # calls parent function to write the time after 1 sec
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()  # recall timer to begin next session
        marks = ""
        for _ in range(math.floor(reps / 2)):  # number of work sessions
            marks += "✅"
        completion_label.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=60, bg=YELLOW)

# Label
timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"),
                    foreground=GREEN, background=YELLOW)
timer_label.grid(column=1, row=0)

# Image and Timer
# about the same size as our image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")  # image location
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(
    FONT_NAME, 35, "bold"))  # default text
canvas.grid(column=1, row=1)

# Start & Reset Buttons
start_button = Button(text="Start", bg=YELLOW,
                      highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW,
                      highlightthickness=0, borderwidth=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Completion Label
completion_label = Label(bg=YELLOW)
completion_label.grid(column=1, row=3)

window.mainloop()
