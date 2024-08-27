from tkinter import *
from tkinter.ttk import *

from time import strftime

root=Tk()
root.title("Clock")
root.geometry("400x400")
root.config(bg="black")


def time():
    string=strftime('%I:%M %p')
    date_string= strftime('%A, %B %d, %y')
    label.config(text=string)
    date_label.config(text=date_string)
    label.after(1000,time)

label = Label(root, font=("ds-digital", 80), background="black", foreground="red" )
label.pack(anchor="center")
date_label = Label(root, font=("ds-digital", 100), background="black", foreground="red")
date_label.pack(anchor="center")
quit_button = Button(root, text="Quit", command=root.destroy, style="TButton")
quit_button.pack(side='bottom', pady=20)

time()

mainloop()  