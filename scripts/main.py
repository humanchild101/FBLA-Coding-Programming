# this is a financial management app programmed by Nikhila and Sharvika.

# importing all the necessary libraries
# importing matplotlib --- This would be used for graphing data (to review b/c error)
# import matplotlib.pyplot as plt

import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox + lines
from tkinter import messagebox
import login
from login import *
import root_window

# main function that runs all pages starting with login page
def main():
    login.show()
    root.mainloop()


if __name__ == "__main__":
    main()
