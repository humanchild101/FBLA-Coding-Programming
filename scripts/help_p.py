import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox + lines
from tkinter import messagebox
import root_window
from root_window import *
import datetime
import PIL
from PIL import Image
import menu_bar

root = root_window.root_init()
help_page = ctk.CTkFrame(root, fg_color="#BEE9E8")

top_nav = ctk.CTkFrame(help_page, fg_color="#33739A", height=70, corner_radius=0)
top_nav.configure(fg_color="#33739A")
welcome_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx=20, height=80, width=500, text="")
user_label = ctk.CTkLabel(welcome_label, text="Welcome, usr123!  ", fg_color="#1B4965", font=("Arial", 20, "bold"), text_color="#BEE9E8", padx=20, height=70)

# I WILL CHANGE THE FILE PATHS LATER ONCE WE GET RID OF VENV
face1 = ctk.CTkImage(light_image=Image.open("faces/very_happy.png"), size=(70,70))
face2 = ctk.CTkImage(light_image=Image.open("faces/happy.png"), size=(70,70))
face3 = ctk.CTkImage(light_image=Image.open("faces/neutral.png"), size=(70,70))
face4 = ctk.CTkImage(light_image=Image.open("faces/sad.png"), size=(70,70))
face5 = ctk.CTkImage(light_image=Image.open("faces/very_sad.png"), size=(70,70))

status_area = ctk.CTkLabel(user_label, text="", image=face1, fg_color="#1B4965", font=("Arial", 20, "bold"), text_color="#BEE9E8", padx=20, height=70, width = 80)

help_frame = ctk.CTkFrame(help_page, fg_color="#62B6CB", width=1175, height=860, corner_radius=20)
help_box = ctk.CTkScrollableFrame(help_frame, width=1095, height=800,corner_radius=10, fg_color="#1B4965")

def hide():
    help_page.forget()

def show():
    root.configure(fg_color="#BEE9E8")

    import login
    import create_account
    import home_page
    import inputs
    import view

    login.hide()
    create_account.hide()
    home_page.hide()
    inputs.hide()
    view.hide()

    help_page.pack(fill="both", expand=True)  # #62B6CB
    top_nav.grid(row = 0, column = 0, columnspan =4, sticky ="nw")

    side_menu = menu_bar.menu_init(help_page)
    side_menu.forget()
    menu_bar.animate_backward()

    # welcome and user sign
    welcome_label.grid(row = 0, column = 0)
    user_label.grid(row = 0, column = 0, sticky ="w", padx = 2)
    status_area.grid(row = 0, column = 1, sticky = "w", padx = 2)

    # view tab name
    inputs_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx = 20, height = 80, width =200, text = "")
    inputs_label.grid(row=0, column = 1, padx = 12)
    tab_label = ctk.CTkLabel(inputs_label, text="USAGE MANUAL", font=("Arial", 20, "bold"), text_color="#BEE9E8", padx = 20, height = 70, width = 100)
    tab_label.grid(row = 0, column = 0, padx = 2, sticky = "w")

    #Add inputs icon here ^

    #this is for other icons like settings and menu bar to open side navigation menu (nav menu will also include home, tab 1, tab 2, log out, and poossibly settings)
    icon_label = ctk.CTkFrame(top_nav, fg_color="#1B4965", height=70, width=550, corner_radius=0)
    icon_label.grid(row=0, column=2, ipadx=28, ipady = 5)

    # button for nav menu
    sidenav_button = ctk.CTkButton(icon_label, text="Menu", font=("Arial", 20, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=190, height=50, corner_radius=5, command = menu_bar.animate)
    sidenav_button.grid(row=0, column=0, padx=15, pady=10, sticky="w")
    # button for logout
    logoutbutton = ctk.CTkButton(icon_label, text="Log Out", font=("Arial", 20, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=190, height=50, corner_radius=5, command=login.show)
    logoutbutton.grid(row=0, column=2, padx=15, pady=10, sticky="e")

    help_frame.place(relx = 0.01, rely = 0.1)
    help_box.place(relx = 0.02, rely = 0.03)

    home_t = ctk.CTkLabel(help_box, text="Home Page", text_color="white", font=("Arial", 30, "bold"),
                          fg_color="#1B4965", corner_radius=15)
    home_t.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    home1 = ctk.CTkLabel(help_box, text="The home page contains the following features: \n\n    - Your 3 most recent transactions\n    - Your 3 most recent deposits\n    - Your 2 biggest purposes for transactions\n    - Your 2 biggest sources for deposits\n    - Your total balance\n    - Money usage info for the month\n    - An area for your notes\n    - An option to choose your status",
                         text_color="white", font=("Arial", 15),
                         fg_color="#1B4965", corner_radius=15,anchor="w", justify="left")
    home1.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    home2 = ctk.CTkLabel(help_box, text = "Note: You can edit your notes by clicking the edit button and save your notes with the save button. You can edit your status by clicking on your desired emoji \nfrom the 5 given options on the status bar",
                         text_color="white", font=("Arial", 15),
                         fg_color="#1B4965", corner_radius=15, anchor="w", justify="left")
    home2.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    update_t = ctk.CTkLabel(help_box, text="Update Inputs Page", text_color="white", font=("Arial", 30, "bold"),
                          fg_color="#1B4965", corner_radius=15)
    update_t.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    update1 = ctk.CTkLabel(help_box,
                         text = "The update inputs page contains the following:\n\n    - Your budget for the month, which can be updated\n    - Your current balance, which can bee updated\n    - Options to input the following:\n        - Transactions (input $ amount, transaction purpose, date of transaction, and whether it is a need or want\n        - Deposits (input $ amount, source of money, and date of deposit)\n        - Sources + Purposes: New income sources and transaction purposes",
                         text_color="white", font=("Arial", 15),
                         fg_color="#1B4965", corner_radius=15, anchor="w", justify="left")
    update1.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    update2 = ctk.CTkLabel(help_box,
                           text = "\nNote: To use a specific transaction purpose or income source for each transaction or deposit input, you must go to th sources+purposes tab and add it there. \nOtherwise, only default values and previously added values will be available for you to select in the Transactions and Deposits tabs.\n",
                           text_color="white", font=("Arial", 15),
                           fg_color="#1B4965", corner_radius=15, anchor="w", justify="left")
    update2.grid(row=5, column=0, padx=10, pady=10, sticky="w")
    update3 = ctk.CTkLabel(help_box,
                           text = "Validation:\n\n    - Any number value you input for $ amounts, budget, or balance MUST BE A DECIMAL OR INTEGER with no other characters.\n    - You MUST choose a transaction purpose or income source when inputting the for the corresponding inputs.\n    - For transactions, any amount you choose to transact must be less than your budget and balance values. If you want to transact more than you have, you \n      must update the budget and/or balance values. ",
                           text_color="white", font=("Arial", 15),
                           fg_color="#1B4965", corner_radius=15, anchor="w", justify="left")
    update3.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    view_t = ctk.CTkLabel(help_box, text="View Finances Page", text_color="white", font=("Arial", 30, "bold"),
                            fg_color="#1B4965", corner_radius=15)
    view_t.grid(row=7, column=0, padx=10, pady=10, sticky="w")

    view1 = ctk.CTkLabel(help_box,
                           text = "The view page will allow you to do the following:\n\n    - Filter based on Expenses/Inputs\n    - Filter by needs or wants\n    - Filter by data ranges\n    - Filter by amount\n    - Filter by specific purposes or income sources ",
                           text_color="white", font=("Arial", 15),
                           fg_color="#1B4965", corner_radius=15, anchor="w", justify="left")
    view1.grid(row=8, column=0, padx=10, pady=10, sticky="w")

    account_t = ctk.CTkLabel(help_box, text="Creating Accounts", text_color="white", font=("Arial", 30, "bold"),
                            fg_color="#1B4965", corner_radius=15)
    account_t.grid(row=9, column=0, padx=10, pady=10, sticky="w")

    account1 = ctk.CTkLabel(help_box,
                         text = "To create an account, you must log out and select create account. You must fill all input fields with valid inputs. Once your account is created, you will receive an \nemail to the email you inputted and you will see a pop-up notifying you of successful account creation",
                         text_color="white", font=("Arial", 15),
                         fg_color="#1B4965", corner_radius=15, anchor="w", justify="left")
    account1.grid(row=10, column=0, padx=10, pady=10, sticky="w")



if __name__ == "__main__":
    show()
    hide()