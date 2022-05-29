from distutils import text_file
from tkinter import *


# ---------------------------- CONSTANTS and global variables ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
CUTE_RED = "#FF8080"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WEIRD_BLUE = "#1C658C"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
symbol = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def timer_reset():

    global symbol, reps
    symbol, reps = "", 0

    window.after_cancel(timer)          # This will stop the timer by cancelling the after() method
    canvas.itemconfig(timer_text, text= "00:00")        #Changes timer back to 00:00

    timer_label.config(text= "TIMER ⏰", fg= WEIRD_BLUE , font=(FONT_NAME, 35, "bold"))      #Changes the activity display text back to original

    symbol_label.config(text= symbol)          # Remove all the task finished symbols once reset

    start_button.config(state= NORMAL)         # Makes the start button usable again



# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer_start():                    #Creatin a function to bind it to the Start button
    global reps
    global symbol

    reps += 1
    print("reps", reps)
    
    if reps % 8 == 0:                   # Condition for Long break time
        count_down(LONG_BREAK_MIN)    
        timer_label.config(text= "BREAK 🛌🏻", fg= RED)

    elif reps % 2 == 0:                 # Condition of Working time
        count_down(SHORT_BREAK_MIN)
        timer_label.config(text= "BREAK 🛌🏻", fg= PINK)

        symbol += "🎯"
        symbol_label.config(text= symbol, fg= CUTE_RED)

    
    else:                               # Condition for Short break time
        count_down(WORK_MIN)
        timer_label.config(text= "WORK 👩🏻‍💻", fg= GREEN)    


    # Adding functionality to limit Start button press to only 1, until reset 
    start_button.config(state= DISABLED)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# Using after() method to schedule an action after a timeout has elapsed.
def count_down(min, sec = 0):
    global timer

    if sec > 0:
        timer = window.after(1000, count_down, min ,sec-1)     #1st argument is time(ms), 2nd is function name, 3rd is the argument for the called function
        print(sec)

        # We use itemconfig() method to update a particular canvas item as we can have multiple items created with a canvas
        canvas.itemconfig(timer_text, text= f"{min:02d}:{sec:02d}")      #string format :02d bsically allows 2 digit integer.

    else:
        if min <= 0:
            timer_start()
        else:
            min -= 1
            count_down(min, 60)

        
    # We use itemconfig() method to update a particular canvas item as we can have multiple items created with a canvas
        canvas.itemconfig(timer_text, text= f"{min:02d}:{sec:02d}")      #string format :02d bsically allows 2 digit integer.

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg= YELLOW)



# CANVAS - The Canvas widget lets us display various graphics on the application. It can be used to draw simple shapes to complicated graphs

canvas = Canvas(width=250 , height= 250, bg= YELLOW, highlightthickness= 0)

#Widget do not accept image file path directly, hence we need to create an image object first then use it as the argument.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(125, 125, image = tomato_img)           #first 2 arguments are coords


# We can use canvas widget to display objects on top of previous objects.
timer_text = canvas.create_text(125, 150, text= "00:00", fill = 'black', font=(FONT_NAME, 28, 'bold'))              # Creating text on top of our image with coords specified


canvas.grid(row=1, column=1)


# Timer text label
timer_label = Label(text= "TIMER ⏰", bg= YELLOW, fg= WEIRD_BLUE , font=(FONT_NAME, 35, "bold"))
timer_label.grid(row=0, column=1)

#Buttons
start_button = Button(text= "Start", font=("Arial", 10, "bold"), width=10, bg= None, fg= None, command= timer_start)
start_button.grid(row= 2, column= 0)

reset_button = Button(text= "Reset", font=("Arial", 10, "bold"), width=10, bg= None, fg= None, command= timer_reset)
reset_button.grid(row= 2, column= 2)


#Completion mark
symbol_label = Label(text= None , bg= YELLOW, fg= CUTE_RED , font=1)
symbol_label.grid(row= 3, column= 1)

window.mainloop()