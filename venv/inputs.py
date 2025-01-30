import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox + lines
from tkinter import messagebox
#import tkcalendar
#from tkcalendar import Calendar
import root_window
from root_window import *
import datetime
import PIL
from PIL import Image
import menu_bar

root = root_window.root_init()
inputs_page = ctk.CTkFrame(root, fg_color="#BEE9E8")

top_nav = ctk.CTkFrame(inputs_page, fg_color="#33739A", height=70, corner_radius=0)
top_nav.configure(fg_color="#33739A")
welcome_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx=20, height=80, width=500, text="")
user_label = ctk.CTkLabel(welcome_label, text="Welcome, usr123!  ", fg_color="#1B4965", font=("Arial", 30, "bold"), text_color="#BEE9E8", padx=20, height=70)

notes_var = tk.StringVar()

# I WILL CHANGE THE FILE PATHS LATER ONCE WE GET RID OF VENV
face1 = ctk.CTkImage(light_image=Image.open("/Users/nikhila/FBLA-Coding-Programming/faces/very_happy.png"), size=(70,70))
face2 = ctk.CTkImage(light_image=Image.open("/Users/nikhila/FBLA-Coding-Programming/faces/happy.png"), size=(70,70))
face3 = ctk.CTkImage(light_image=Image.open("/Users/nikhila/FBLA-Coding-Programming/faces/neutral.png"), size=(70,70))
face4 = ctk.CTkImage(light_image=Image.open("/Users/nikhila/FBLA-Coding-Programming/faces/sad.png"), size=(70,70))
face5 = ctk.CTkImage(light_image=Image.open("/Users/nikhila/FBLA-Coding-Programming/faces/very_sad.png"), size=(70,70))

status_area = ctk.CTkLabel(user_label, text="", image=face1, fg_color="#1B4965", font=("Arial", 30, "bold"), text_color="#BEE9E8", padx=20, height=70, width = 80)

def hide():
    inputs_page.forget()

def show():
    root.configure(fg_color="#BEE9E8")

    import login
    import create_account
    import home_page

    login.hide()
    create_account.hide()
    home_page.hide()
    inputs_page.pack(fill="both", expand=True)  # #62B6CB
    top_nav.grid(row = 0, column = 0, columnspan =4, sticky ="nw")

    side_menu = menu_bar.menu_init(inputs_page)
    side_menu.forget()
    menu_bar.animate_backward()


    # welcome and user sign
    welcome_label.grid(row = 0, column = 0)
    #SHARVIKAAAAA USER NAME HEREEEE (ignore my uppercase im just hoping you see the comments among the rest)
    user_label.grid(row = 0, column = 0, sticky ="w", padx = 2)

    status_area.grid(row = 0, column = 1, sticky = "w", padx = 2)


    #ADD SMILY FACE HERE ^

    # iputs tab name
    inputs_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx = 20, height = 80, width =200, text = "")
    inputs_label.grid(row=0, column = 1, padx = 12)
    tab_label = ctk.CTkLabel(inputs_label, text="INPUTS", font=("Arial", 30, "bold"), text_color="#BEE9E8", padx = 20, height = 70, width = 100)
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


    # Manual Budget Update
    monthly_budget_frame = ctk.CTkFrame(inputs_page, fg_color="#62B6CB", corner_radius=20, width=640, height=100)
    monthly_budget_frame.grid(row=1, column=0, padx=15, pady=15, sticky="e")

    # Manual Balance Updates
    manual_balance_update_frame = ctk.CTkFrame(inputs_page, fg_color="#62B6CB", corner_radius=20, width=480, height=100)
    manual_balance_update_frame.grid(row=1, column=1, padx=15, pady=15, sticky="w")

    tab_view = ctk.CTkTabview(inputs_page, fg_color = "#1B4965", corner_radius= 20, width = 1100, height =600)
    tab_view.place(relx = 0.026, rely = 0.2)

    transactions = tab_view.add("Transactions")
    deposits = tab_view.add("Deposits")
    income_sources = tab_view.add("Income Sources")

    amount_var = tk.StringVar(value = "0.00")
    amount_label = ctk.CTkLabel(transactions, fg_color="#62B6CB", corner_radius=5, width=60, height=40, text_color="black", font = ("Arial", 20, "bold"), text = "Amount: ")
    amount_label.place(relx = 0.001, rely = 0.01)
    amount_entry = ctk.CTkEntry(transactions, width=100, height = 40, textvariable = amount_var, font=("Arial", 12))
    amount_entry.place(relx=0.1, rely=0.01)

    purpose_label = ctk.CTkLabel(transactions, fg_color="#62B6CB", corner_radius=5, width=60, height=40, text_color="black", font = ("Arial", 20, "bold"), text = "Purpose of Transaction: ")
    purpose_label.place(relx = 0.001, rely = 0.13)
    purpose_var = tk.StringVar(value="Choose")  # Default value set to 'Need'
    purpose_options = ["Bills/Rent", "Necessities", "Transportation", "Healthcare", "Education", "Donations", "Entertainment", "Other"]
    purpose_dropdown = ctk.CTkOptionMenu(transactions, variable=purpose_var, values=purpose_options, font=("Arial", 15), height = 40)
    purpose_dropdown.place(relx=0.25, rely=0.13)

    # date label + calendar dropdown
    date_label = ctk.CTkLabel(transactions, text="Date: ", font=("Arial", 20, "bold"), fg_color="#62B6CB", corner_radius=5, height = 40, width = 30, text_color="black")
    date_label.place(relx=0.001, rely=0.28, anchor="w")

    '''
    calendar = Calendar(transactions, selectmode="day", date_pattern="yyyy-mm-dd", font=("Arial", 12), width=20, background="lightblue", foreground="black", borderwidth=1)
    calendar.place(relx=0.25, rely=0.25, anchor="w")
    '''

    # need/want radio buttons
    need_want = ctk.CTkLabel(transactions, text="", fg_color="#62B6CB", corner_radius=5, height = 80, width = 500)
    need_want.place(relx=0.47, rely=0.09, anchor="w")

    need_var = tk.StringVar(value="Need")  # Default value set to 'Need'
    need_radio = ctk.CTkRadioButton(need_want, text="Need", variable=need_var, value="Need", font=("Arial", 20, "bold"), width=70, text_color="black")
    need_radio.place(relx=0.1, rely=0.5, anchor="w")
    want_radio = ctk.CTkRadioButton(need_want, text="Want", variable=need_var, value="Want", font=("Arial", 20, "bold"), width=70, text_color="black")
    want_radio.place(relx=0.5, rely=0.5, anchor="w")

show()
root.mainloop()

if __name__ == "__main__":
    show()
    hide()
