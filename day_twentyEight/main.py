from tkinter import *
import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "MS Serif"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_tim():
    window.after_cancel(timer)
    canva.itemconfig(timer_text, text = "00:00")
    tittie_label.config(text="Time")
    global mark
    global reps 
    reps = 0
    mark = 0
    prog_label.config(text="")
    



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_tim():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        tittie_label.config(text="Long Break",fg=PINK)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        tittie_label.config(text="Short Break", fg=RED)
    else:
        count_down(work_sec)
        tittie_label.config(text="⚒️", fg=GREEN)
        
   

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <= 9:
        count_sec = f"0{count_sec}"   
    if count_min <= 9:
        count_min = f"0{count_min}" 
    canva.itemconfig(timer_text, text = f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_tim()
        mark = ""
        work_sessions = math.floor(reps /2)
        for _ in range(work_sessions):
            mark += "✔️"
            prog_label.config(text=mark)
            
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady=50, bg=YELLOW)


tittie_label = Label(text="Time", bg=YELLOW, fg=GREEN, font=(FONT_NAME,53, "bold"))
tittie_label .grid(column=1, row=0 )


prog_label = Label(bg=YELLOW, fg=GREEN)
prog_label.grid(column=1, row=3)

canva = Canvas(width=200, height= 224, bg=YELLOW, highlightthickness=0)

img = PhotoImage(file = "tomato.png")
canva.create_image(100, 112, image=img )

timer_text = canva.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME,25, "bold"))
canva.grid(column=1, row=1)

start_butt = Button(text="Start",highlightthickness=0, command=start_tim)
start_butt.grid(column=0, row=2)

reset_butt = Button(text="Reset", highlightthickness= 0, command=reset_tim)
reset_butt.grid(column=2, row=2)

window.mainloop()


