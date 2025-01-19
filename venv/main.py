#this is a financial management app programmed by Nikhila and Sharvika.

#importing all the necessary libraries
#importing matplotlib --- This would be used for graphing data (to review b/c error)
#import matplotlib.pyplot as plt

#importing tkinter --- it would be used for creating a GUI
import tkinter as tk
from tkinter import *
from tkinter import ttk #apparently this is useful to style the tk widgets like how css is used to style


#creating another window to store the SQL commands
def database_display_window():
    database_window = tk.Toplevel(root)
    database_window.title("Your transaction history")
    database_window.geometry("800x600")


    close_button = tk.Button(database_window, text="Close", command=database_window.destroy)
    close_button.grid(row=0, column=0, pady=10)

#root is root window which will contain *everything*
#Setting up the root window
root = tk.Tk()
root.title("Home Page")
root.geometry("800x600")
#root.attributes('-fullscreen', True) #causing the problem w/ the desktop


def onceClicked():
    label = Label(root, text = "i clicked the thing")
    label.grid(row = 3, column = 0)


#label examples 4 reference
tl1 = Label(root, text= "welcome")
tl1.grid(row = 0, column = 0)
tl2 = Label(root, text= "test label 2")
tl2.grid(row = 1, column = 0)

#button examples 4 reference
#command is basically what action happens once the button is clicked. you can make a function for that and you can use that function as a command. this timee it was teh onceClicked function
tb1 = Button(root, text = "test button1", padx = 20, pady = 50, command = onceClicked)
tb1.grid(row = 2, column = 0)


open_button = tk.Button(root, text="Open Database", command=database_display_window)
open_button.grid(row=4, column=0, pady=20)

root.mainloop()