# Calls the tkinter package and ALL
# of its contents and method with (*) for creating python GUIs.
from tkinter import *

# Calls the time package and ALL
# of its contents and method with (*) for representing date/time in codes.
from time import *

# Function update_time where calls the command block below,
# which utilizes strftime method in calling dates and times in programming syntaxes.
# Link: https://strftime.org

def update_time():
    date_update = strftime("%B %d, %Y")
    date_label.config(text=date_update)

    day_update = strftime("%A")
    day_label.config(text=day_update)

    time_update = strftime(" %I:%M:%S %p ")
    time_label.config(text=time_update)

    window.after(1000, update_time)

# tk is a python package that can be used to create a GUI.
window = Tk()

# resizable method is to use whether the tk window can be moved or not.
# window.resizable(Width = True/False, Height = True/False)
window.resizable(False, False)

# title = can write text in string that will appear in the title bar of the window.
window.title("Real-Time Clock-Time")

# Label() = tkinter widget that used to implement display boxes such as
# images or texts that can be manipulated
# .pack() = organizes widgets in blocks before displaying in the parent widget(window)

date_label = Label(window, font=("Futura PT Book", 35))
date_label.pack()

day_label = Label(window, font=("Futura PT Book", 25))
day_label.pack()

time_label = Label(window, font=("Arial", 50),
                   fg="green",
                   bg="black",
                   relief="ridge",
                   border=25)
time_label.pack()

# calls the update_time function
update_time()

window.mainloop()

