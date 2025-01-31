#SSHARVIKAAAAAAAAAAAAAA
#need i say any more?
import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox + lines
from tkinter import messagebox
from tkinter import ttk
import root_window
from root_window import *
import datetime
import PIL
from PIL import Image
import menu_bar
import re

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

# Manual Budget Update
monthly_budget_frame = ctk.CTkFrame(inputs_page, fg_color="#62B6CB", corner_radius=20, width=640, height=100)
monthly_budget_frame.grid(row=1, column=0, padx=15, pady=15, sticky="e")

# Manual Balance Updates
manual_balance_update_frame = ctk.CTkFrame(inputs_page, fg_color="#62B6CB", corner_radius=20, width=480, height=100)
manual_balance_update_frame.grid(row=1, column=1, padx=15, pady=15, sticky="w")

tab_view = ctk.CTkTabview(inputs_page, fg_color="#1B4965", corner_radius=20, width=1100, height=700)
tab_view.place(relx=0.026, rely=0.2)

transactions = tab_view.add("Transactions")
deposits = tab_view.add("Deposits")
income_sources = tab_view.add("Income Sources")

pattern = r'^\d+(\.\d+)?$'

#STRING VARS for transactions
amount_var = tk.StringVar(value="0.00")
purpose_var = tk.StringVar(value="Choose")  # Default value set to 'Need'
date_options = [(datetime.date.today() - datetime.timedelta(days=i)).strftime("%m-%d-%Y") for i in range(500)]
date_var = ctk.StringVar(value=date_options[0])  # Default to today's date
need_var = tk.StringVar(value="Need")  # Default value set to 'Need'

#STRING VARS for deposits
amountd_var = tk.StringVar(value="0.00")
sourced_var = tk.StringVar(value="None")  # Default value set to 'None'
date_options = [(datetime.date.today() - datetime.timedelta(days=i)).strftime("%m-%d-%Y") for i in range(500)]
dated_var = ctk.StringVar(value=date_options[0])  # Default to today's date

#data table
#t_frame = ctk.CTkCanvas(transactions, width=620, height=400)
#scroll = ttk.Scrollbar(t_frame, orient="vertical")
#t_frame.configure(yscrollcommand=scroll.set)

transactions_table = ttk.Treeview(transactions, columns=("No.", "Transaction", "N/W", "Amount", "Date", "Del"), show="headings", height=200)
deposits_table = ttk.Treeview(deposits, columns=("No.", "Deposit", "Amount", "Date", "Del"), show="headings", height=200)


# function to add a new transaction
def on_t_input():
    no = len(transactions_table.get_children()) + 1  # automatically adds 1 to the tree length
    transaction = purpose_var.get()
    nw = need_var.get()
    amount = amount_var.get()
    date = date_var.get()

    if (transaction and nw and amount and date) and (re.fullmatch(pattern, amount) and transaction != "Choose") :
        transactions_table.insert("", "end", values=(no, transaction, nw, amount, date))
    else:
        messagebox.showwarning("Transaction not created", "Please enter all correct fields. Amount must have only numbers with no other characters except a decimal point '.' ")


def on_d_input():
    no = len(deposits_table.get_children()) + 1  # automatically adds 1 to the tree length
    deposit = sourced_var.get()
    amount = amountd_var.get()
    date = dated_var.get()

    if (deposit and nw and amount and date) and (re.fullmatch(pattern, amount) and deposit != "None"):
        deposits_table.insert("", "end", values=(no, deposit, amount, date))
    else:
        messagebox.showwarning("Deposit not created",
                               "Please enter all correct fields. Amount must have only numbers with no other characters except a decimal point '.' ")


def hide():
    inputs_page.forget()

def show():
    root.configure(fg_color="#BEE9E8")

    import login
    import create_account
    import home_page
    import view

    login.hide()
    create_account.hide()
    home_page.hide()
    view.hide()
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


    amount_label = ctk.CTkLabel(transactions, fg_color="#62B6CB", corner_radius=5, width=60, height=40, text_color="black", font = ("Arial", 20, "bold"), text = "Amount: ")
    amount_label.place(relx = 0.001, rely = 0.01)
    amount_entry = ctk.CTkEntry(transactions, width=100, height = 40, textvariable = amount_var, font=("Arial", 12))
    amount_entry.place(relx=0.1, rely=0.01)

    purpose_label = ctk.CTkLabel(transactions, fg_color="#62B6CB", corner_radius=5, width=60, height=40, text_color="black", font = ("Arial", 20, "bold"), text = "Purpose of Transaction: ")
    purpose_label.place(relx = 0.001, rely = 0.13)
    purpose_options = ["Bills/Rent", "Necessities", "Transportation", "Healthcare", "Education", "Donations", "Entertainment", "Other"]
    purpose_dropdown = ctk.CTkOptionMenu(transactions, variable=purpose_var, values=purpose_options, font=("Arial", 15), height = 40, text_color= "black",fg_color= "#BEE9E8", button_color= "#BEE9E8", button_hover_color="#A0D8D3")
    purpose_dropdown.place(relx=0.25, rely=0.13)

    # date label + calendar dropdown
    date_label = ctk.CTkLabel(transactions, text="Date: ", font=("Arial", 20, "bold"), fg_color="#62B6CB", corner_radius=5, height = 40, width = 30, text_color="black")
    date_label.place(relx=0.001, rely=0.28, anchor="w")


    date_dropdown = ctk.CTkOptionMenu(transactions, variable=date_var, values=date_options, font=("Arial", 15), height=40, text_color= "black",fg_color= "#BEE9E8", button_color= "#BEE9E8", button_hover_color="#A0D8D3")
    date_dropdown.place(relx = 0.083, rely = 0.24)

    # need/want radio buttons
    need_want = ctk.CTkLabel(transactions, text="", fg_color="#62B6CB", corner_radius=5, height = 80, width = 400)
    need_want.place(relx=0.47, rely=0.01, anchor="nw")

    need_radio = ctk.CTkRadioButton(need_want, text="Need (N)", variable=need_var, value="Need", font=("Arial", 20, "bold"), width=40, text_color="black", fg_color="#BEE9E8",hover_color="#1B4965")
    need_radio.place(relx=0.1, rely=0.5, anchor="w")
    want_radio = ctk.CTkRadioButton(need_want, text="Want (W)", variable=need_var, value="Want", font=("Arial", 20, "bold"), width=40, text_color="black", fg_color="#BEE9E8",hover_color="#1B4965")
    want_radio.place(relx=0.5, rely=0.5, anchor="w")

    #SHARVIKAAAAAAAAAAAA
    input_button = ctk.CTkButton(transactions, text="Input Transaction", font=("Arial", 20, "bold"), fg_color="#9AC0BF", hover_color="#467F8D", height = 40, text_color="black", width=300, corner_radius=10, command=on_t_input)
    input_button.place(relx = 0.5, rely = 0.24)


    transactions_table.heading("No.", text="No.")
    transactions_table.heading("Transaction", text="Transaction")
    transactions_table.heading("N/W", text="N/W")
    transactions_table.heading("Amount", text="Amount")
    transactions_table.heading("Date", text="Date")
    transactions_table.heading("Del", text="Del")

    transactions_table.column("No.", width=50)
    transactions_table.column("Transaction", width=200)
    transactions_table.column("N/W", width=80)
    transactions_table.column("Amount", width=100)
    transactions_table.column("Date", width=100)
    transactions_table.column("Del", width=80)

    #t_frame.place(relx = 0.2, rely = 0.4)
    #scroll.place(relx=1, rely=0, relheight=1, width=20)

    transactions_table.place(relx = 0.2, rely = 0.4)













    amountd_label = ctk.CTkLabel(deposits, fg_color="#62B6CB", corner_radius=5, width=60, height=40,
                                text_color="black", font=("Arial", 20, "bold"), text="Amount: ")
    amountd_label.place(relx=0.001, rely=0.01)
    amountd_entry = ctk.CTkEntry(deposits, width=100, height=40, textvariable=amountd_var, font=("Arial", 12))
    amountd_entry.place(relx=0.1, rely=0.01)

    sourced_label = ctk.CTkLabel(deposits, fg_color="#62B6CB", corner_radius=5, width=60, height=40,
                                 text_color="black", font=("Arial", 20, "bold"), text="Source of Money: ")
    sourced_label.place(relx=0.001, rely=0.13)
    sourced_entry = ctk.CTkEntry(deposits, width=100, height=40, textvariable = sourced_var, font=("Arial", 12))

    sourced_entry.place(relx=0.25, rely=0.13)

    # date label + calendar dropdown
    dated_label = ctk.CTkLabel(deposits, text="Date: ", font=("Arial", 20, "bold"), fg_color="#62B6CB",
                              corner_radius=5, height=40, width=30, text_color="black")
    dated_label.place(relx=0.001, rely=0.28, anchor="w")

    dated_dropdown = ctk.CTkOptionMenu(deposits, variable=dated_var, values=date_options, font=("Arial", 15),
                                      height=40, text_color="black", fg_color="#BEE9E8", button_color="#BEE9E8",
                                      button_hover_color="#A0D8D3")
    dated_dropdown.place(relx=0.083, rely=0.24)

    # need/want radio buttons

    # SHARVIKAAAAAAAAAAAA
    inputd_button = ctk.CTkButton(deposits, text="Input Deposit", font=("Arial", 20, "bold"), fg_color="#9AC0BF",
                                 hover_color="#467F8D", height=40, text_color="black", width=300, corner_radius=10,
                                 command=on_d_input)
    inputd_button.place(relx=0.5, rely=0.24)

    deposits_table.heading("No.", text="No.")
    deposits_table.heading("Deposit", text="Deposit")
    deposits_table.heading("Amount", text="Amount")
    deposits_table.heading("Date", text="Date")
    deposits_table.heading("Del", text="Del")

    deposits_table.column("No.", width=50)
    deposits_table.column("Deposit", width=200)
    deposits_table.column("Amount", width=100)
    deposits_table.column("Date", width=100)
    deposits_table.column("Del", width=80)

    # t_frame.place(relx = 0.2, rely = 0.4)
    # scroll.place(relx=1, rely=0, relheight=1, width=20)

    deposits_table.place(relx=0.2, rely=0.4)


show()
root.mainloop()
if __name__ == "__main__":
    show()
    hide()
