from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
REPS = 0
TIMER = None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global REPS
    count_min = math.floor(count/60)
    count_sec = count % 60
    if int(count_sec) < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_txt, text = f"{count_min}.{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    else:
        start()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += "✓"
            process_tracker.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
def start():
    global REPS
    REPS += 1
    if REPS % 8 == 0:
        header.config(text="Break-20 mins")
        count_down(20 * 60)

    elif REPS % 5 == 0:
        header.config(text="Break-5 mins")
        count_down(1 * 60)
    else:
        header.config(text="Work-25 mins")
        count_down(25*60)

def reset():
    window.after_cancel(TIMER)
    header.config(text="TIMER")
    process_tracker.config(text="")
    canvas.itemconfig(timer_txt, text= "00.00")
    global REPS
    REPS = 0

window = Tk()
window.minsize(500,400)
window.config(padx=50,pady=50, bg=YELLOW)
window.title("Pomodoro App")

header = Label(text= "   TIMER   ", font=("Times New Roman", 30),fg= GREEN, bg= YELLOW)
header.grid(row=0, column= 1)

canvas =Canvas(width=220, height= 223, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(105,112,image=tomato)
timer_txt = canvas.create_text(105,130,text="25.00",fill= "white", font=("Times New Roman", 30, "bold"))
canvas.grid(row=1,column=1)


start_button = Button(text= "Start",font=("Times New Roman", 12, "bold"), command=start,bg=GREEN, fg= "red",width=8, height=2)
start_button.grid(row=2, column=0)

reset_button =Button(text="Reset",font=("Times New Roman", 12, "bold"), command=reset,bg=GREEN, fg= "red",width=8, height=2)
reset_button.grid(row=2, column=2)

process_tracker = Label(text= "",font=("Times New Roman", 20, "bold"), bg= YELLOW, fg= "green")
process_tracker.grid(row=3, column=1)



window.mainloop()
