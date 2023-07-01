from tkinter import *
from tkinter import messagebox
#Concept to review in this program: How count_down recalls itself, and the window.after effect
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
check = ""
clock = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global clock
    window.after_cancel(clock)
    global reps
    global check
    reps = 0
    check = ""
    timer.config(text = "Timer")
    canvas.itemconfig(timer_text, text = "00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global check
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text = "LONG BREAK", fg = RED)
        check += "✓"
        checks.config(text = check)
        messagebox.showinfo(title="Big Break", message = "Long break achieved")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text = "SHORT BREAK", fg = RED)
        check += "✓"
        checks.config(text = check)
        messagebox.showinfo(title="Short Break", message = "Short break achieved")
    else:
        count_down(work_sec)
        timer.config(text = "WORK", fg = GREEN)
        messagebox.showinfo(title="Work Time", message = "Get yo ass back to work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global clock
    minutes = count // 60
    seconds = round(count%60, 2)
    if seconds <= 9:
        seconds = "0" + str(seconds)
    canvas.itemconfig(timer_text, text = f"{minutes}:{seconds}")
    if count > 0:
        clock = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()

#DYNAMIC TYPING NOTES
#Dynamic typing is the ability to change a datas datatype (int, str, etc. ) based on the contents of that string. Example: a = 3 .....(few lines later) a = "hello"



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
#Padding needed to add extra room, or else the image will be the whole window
window.config(padx = 100, pady = 50)
window.config(background= YELLOW)

window.after(1000)

photo = PhotoImage(file="Day 28/pomodoro-start/tomato.png")
canvas = Canvas(width=200, height=224, background= YELLOW, highlightthickness= 0)
canvas.create_image(100, 112, image = photo)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start = Button(text="Start", command= start_timer)
start.grid(column= 0, row = 2)

reset = Button(text="reset", command=reset)
reset.grid(column= 2, row= 2)


checks = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 12, 'bold'))
checks.grid(column= 1, row = 3)

timer = Label(text = "Timer", fg = GREEN, font = (FONT_NAME, 35, 'bold'), bg = YELLOW)
timer.grid(row= 0, column= 1)

window.mainloop()