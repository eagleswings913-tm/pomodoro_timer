import tkinter as tk

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
    app_label.config(text="Timer", fg=GREEN)
    tracker_label.config(text="")
    canvas.itemconfig(timer_text, text='00:00')
    window.after_cancel(timer)
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in [1,3,5,7]:
        app_label.config(text="Time to Work", fg=GREEN)
        count_down(int(work_sec))
    elif reps in [2,4,6]:
        app_label.config(text="Short Break", fg=PINK)
        count_down(int(short_break_sec))
    elif reps == 8:
        app_label.config(text="Long Break", fg=RED)
        count_down(int(long_break_sec))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = count // 60
    count_seconds = count % 60
    if count_minutes <10:
        count_minutes = '0' + str(count_minutes)
    if count_seconds <10:
        count_seconds = '0' + str(count_seconds)
    canvas.itemconfig(timer_text, text=f'{count_minutes}:{count_seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        checkmark = '✓'
        if reps % 2 == 0:
            if reps // 2 == 1:
                tracker_label.config(text=checkmark)
            elif reps // 2 == 2:
                tracker_label.config(text=checkmark + checkmark)
            elif reps // 2 == 3:
                tracker_label.config(text=checkmark + checkmark + checkmark)
            else:
                tracker_label.config(text=checkmark + checkmark + checkmark + checkmark)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

app_label = tk.Label(window, text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
app_label.grid(row=0, column=1)

canvas = tk.Canvas(window, width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(row=1, column=1)

start_button = tk.Button(highlightthickness=0, command=start_timer)
start_button["text"] = "Start"
start_button.config(font=(FONT_NAME, 14, "normal"))
start_button.grid(row=2, column=0)

tracker_label = tk.Label(window, bg=YELLOW, fg=GREEN)
tracker_label.config(font=(FONT_NAME, 14, "normal"))
tracker_label.grid(row=3, column=1)

reset_button = tk.Button(highlightthickness=0,command=reset_timer)
reset_button["text"] = "Reset"
reset_button.config(font=(FONT_NAME, 14, "normal"))
reset_button.grid(row=2, column=2)



window.mainloop()