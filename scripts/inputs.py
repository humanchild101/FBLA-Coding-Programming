# NOTE FOR NIKHILA: update icons stuff + ADD NEEDS AND WANTS

# NOTE FOR SHARVIKA: ctrl-F your name and you will find specific places you need to do db for. idk if there's more in this page.
# Make sure all recent updates are updated into your scripts files and make sure db is doing its thing for all of it
# (feel free to give me updates, so I can also suggest what might need db if you'd like)
# another important thing sharvika: each input row in either transactions or deposits table in this page should have a delete option
# for this ^, check the column names I put for the transactions/deposits on ln 75 + 77


# imports
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import root_window
from root_window import *
import datetime
import PIL
from PIL import Image
import menu_bar
from session_manager import SessionManager
import db_connect as db

session = SessionManager()

first_name = session.get("first_name")
last_name = session.get("last_name")
user_id = session.get("user_id")

# root window initialization
root = root_window.root_init()

# input page frame
inputs_page = ctk.CTkFrame(root, fg_color="#BEE9E8")

# navigation bar
top_nav = ctk.CTkFrame(inputs_page, fg_color="#33739A", height=70, corner_radius=0)
top_nav.configure(fg_color="#33739A")
welcome_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx=20, height=80, width=500, text="")
user_label = ctk.CTkLabel(welcome_label, text=f"Welcome, {first_name} {last_name}!", fg_color="#1B4965", font=("Arial", 30, "bold"), text_color="#BEE9E8", padx=20, height=70)

# string var to hold notes
notes_var = tk.StringVar()

# image files for status
face1 = ctk.CTkImage(light_image=Image.open("faces/very_happy.png"), size=(70,70))
face2 = ctk.CTkImage(light_image=Image.open("faces/happy.png"), size=(70,70))
face3 = ctk.CTkImage(light_image=Image.open("faces/neutral.png"), size=(70,70))
face4 = ctk.CTkImage(light_image=Image.open("faces/sad.png"), size=(70,70))
face5 = ctk.CTkImage(light_image=Image.open("faces/very_sad.png"), size=(70,70))

status_area = ctk.CTkLabel(user_label, text="", image=face1, fg_color="#1B4965", font=("Arial", 20, "bold"),
                           text_color="#BEE9E8", padx=20, height=70, width=80)

# inputs tab views
tab_view = ctk.CTkTabview(inputs_page, fg_color="#1B4965", corner_radius=20, width=1100, height=700)
tab_view.place(relx=0.026, rely=0.2)

# transaction and deposits tab. income tab may or may not be added later
transactions = tab_view.add("Transactions")
deposits = tab_view.add("Deposits")
# income_sources = tab_view.add("Income Sources")


# string vars for transaction inputs with default values
amount_var = tk.DoubleVar(value=0.00)
purpose_var = tk.StringVar(value="Choose")
date_options = [(datetime.date.today() - datetime.timedelta(days=i)).strftime("%m-%d-%Y") for i in range(500)]
date_var = ctk.StringVar(value=date_options[0])
need_var = tk.StringVar(value="Need")

# string vars for deposit inputs with default values
amountd_var = tk.DoubleVar(value=0.00)
sourced_var = tk.StringVar(value="None")
date_options = [(datetime.date.today() - datetime.timedelta(days=i)).strftime("%m-%d-%Y") for i in range(500)]
dated_var = ctk.StringVar(value=date_options[0])

# double vars to hold balance and budget amounts
b_var = tk.DoubleVar(value=0.00)
ba_var = tk.DoubleVar(value=0.00)

# SHARVIKAA: Tree view for data table, but you will replace this with the db table i suppose?
transactions_table = ttk.Treeview(transactions, columns=("No.", "Transaction", "N/W", "Amount", "Date", "Del"),
                                  show="headings", height=200)
deposits_table = ttk.Treeview(deposits, columns=("No.", "Deposit", "Amount", "Date", "Del"), show="headings",
                              height=200)

# monthly budget + balance frames
monthly_budget_frame = ctk.CTkFrame(inputs_page, fg_color="#62B6CB", corner_radius=20, width=500, height=100)
manual_balance_update_frame = ctk.CTkFrame(inputs_page, fg_color="#62B6CB", corner_radius=20, width=540, height=100)

# budget + balance text labels
budget = ctk.CTkLabel(monthly_budget_frame, text="$" + str(b_var.get()), font=("Arial", 20, "bold"), corner_radius=20,
                      text_color="black", padx=10, height=40, width=60)
total_balance = ctk.CTkLabel(manual_balance_update_frame, text="$" + str(ba_var.get()), font=("Arial", 20, "bold"),
                             corner_radius=20,
                             text_color="black", padx=10, height=40, width=60)


# function to add a new transaction
def on_t_input():
    # getting string/double var values
    no = len(transactions_table.get_children()) + 1
    transaction = purpose_var.get()
    nw = need_var.get()
    amount = amount_var.get()
    date = date_var.get()

    # if all info is valid
    if transaction and nw and amount and date and transaction != "Choose":
        transactions_table.insert("", "end", values=(no, transaction, nw, amount, date))
        # updates balance values
        # Convert to datetime object
        date_obj = datetime.datetime.strptime(date, "%d-%m-%Y")

        # Convert to new format
        new_date_str = date_obj.strftime("%Y-%m-%d")
        print(new_date_str)

        insert_query = f"""insert into transactions (income_or_expense,source,date_of_transaction,need_or_want,note,amount,user_id) 
                        values ('expense','{transaction}',TO_DATE('{new_date_str}', 'YYYY-MM-dd'),'{nw}','{transaction}',{amount},{user_id})"""
        # updates balance values
        db.insert_values(insert_query)
        
        new_balance = ba_var.get() - amount
        new_budget = b_var.get() - amount
        ba_var.set(new_balance)
        b_var.set(new_budget)
        # updates the text shown
        total_balance.configure(text=f"${new_balance:.2f}")
        budget.configure(text=f"${new_budget:.2f}")
    else:
        messagebox.showwarning("Transaction not created", "Please enter all correct fields.")


# function to add a new deposit
def on_d_input():
    no = len(deposits_table.get_children()) + 1
    deposit = sourced_var.get()
    amount = amountd_var.get()
    date = dated_var.get()

    if deposit and amount and date and deposit != "None":
        deposits_table.insert("", "end", values=(no, deposit, amount, date))
        # update balance values
        date_obj = datetime.datetime.strptime(date, "%d-%m-%Y")

        # Convert to new format
        new_date_str = date_obj.strftime("%Y-%m-%d")
        print(new_date_str)

        insert_query = f"""insert into transactions (income_or_expense,source,date_of_transaction,need_or_want,note,amount,user_id) 
                        values ('income','{deposit}',TO_DATE('{new_date_str}', 'YYYY-MM-dd'),'n/a','{deposit}',{amount},{user_id})"""
        # updates balance values
        db.insert_values(insert_query)
        
        new_balance = ba_var.get() + amount
        ba_var.set(new_balance)
        # update
        total_balance.configure(text=f"${new_balance:.2f}")
    else:
        messagebox.showwarning("Deposit not created", "Please enter all correct fields.")


# updates monthly budget
def update_month_budget():
    if b_var.get() <= ba_var.get():
        current_budget = b_var.get()
        budget.configure(text="$" + str(b_var.get()))
        budget_query = """UPDATE transactions
                        SET budget = {}
                        WHERE user_id = {}""".format(float(current_budget), user_id)
        db.insert_values(budget_query)

    else:
        messagebox.showinfo("Invalid input", "Budget cannot be greater than current balance")


# updates balance
def update_balance():
    total_balance.configure(text="$" + str(ba_var.get()))


# hides page
def hide():
    inputs_page.forget()


# shows page
def show():
    root.configure(fg_color="#BEE9E8")

    # imports
    import login
    import create_account
    import home_page
    import view

    login.hide()
    create_account.hide()
    home_page.hide()
    view.hide()

    inputs_page.pack(fill="both", expand=True)  # #62B6CB
    top_nav.grid(row=0, column=0, columnspan=4, sticky="nw")

    # menu bar initializing
    side_menu = menu_bar.menu_init(inputs_page)
    side_menu.forget()
    menu_bar.animate_backward()

    # welcome and user sign
    welcome_label.grid(row=0, column=0)
    user_label.grid(row=0, column=0, sticky="w", padx=2)
    status_area.grid(row=0, column=1, sticky="w", padx=2)

    # inputs tab name
    inputs_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx=20, height=80, width=200, text="")
    inputs_label.grid(row=0, column=1, padx=12)
    tab_label = ctk.CTkLabel(inputs_label, text="INPUTS", font=("Arial", 30, "bold"), text_color="#BEE9E8", padx=20,
                             height=70, width=100)
    tab_label.grid(row=0, column=0, padx=2, sticky="w")

    # Add inputs icon here ^

    # a frame to include buttons like menu/log out/settings etc
    icon_label = ctk.CTkFrame(top_nav, fg_color="#1B4965", height=70, width=550, corner_radius=0)
    icon_label.grid(row=0, column=2, ipadx=28, ipady=5)

    # button for nav menu
    sidenav_button = ctk.CTkButton(icon_label, text="Menu", font=("Arial", 20, "bold"), fg_color="#BEE9E8",
                                   hover_color="#9ACCD9", text_color="black", width=190, height=50, corner_radius=5,
                                   command=menu_bar.animate)
    sidenav_button.grid(row=0, column=0, padx=15, pady=10, sticky="w")

    # button for logout
    logoutbutton = ctk.CTkButton(icon_label, text="Log Out", font=("Arial", 20, "bold"), fg_color="#BEE9E8",
                                 hover_color="#9ACCD9", text_color="black", width=190, height=50, corner_radius=5,
                                 command=login.show)
    logoutbutton.grid(row=0, column=2, padx=15, pady=10, sticky="e")

    # manual budget update
    monthly_budget_frame = ctk.CTkFrame(inputs_page, fg_color="#62B6CB", corner_radius=20, width=640, height=100)
    monthly_budget_frame.grid(row=1, column=0, padx=15, pady=15, sticky="e")
    current_month = datetime.datetime.now().strftime("%B")
    budget_text = ctk.CTkLabel(monthly_budget_frame, text="Update " + current_month + " Budget",
                               font=("Arial", 20, "bold"), corner_radius=20, text_color="black", padx=10, height=40,
                               width=60)
    budget_text.place(relx=0.0001, rely=0.004)

    budget.place(relx=0.03, rely=0.5)
    b_amount = ctk.CTkEntry(monthly_budget_frame, width=100, height=40, textvariable=b_var, font=("Arial", 12))
    b_amount.place(relx=0.4, rely=0.5)

    updateb = ctk.CTkButton(monthly_budget_frame, text="Update", font=("Arial", 20, "bold"), fg_color="#BEE9E8",
                            hover_color="#9ACCD9", text_color="black", width=120, height=50, corner_radius=5,
                            command=update_month_budget)
    updateb.place(relx=0.7, rely=0.4)

    # manual balance updates
    manual_balance_update_frame.grid(row=1, column=2, padx=15, pady=15, sticky="w")

    balance_txt = ctk.CTkLabel(manual_balance_update_frame, text="Update Balance",
                               font=("Arial", 20, "bold"), corner_radius=20, text_color="black", padx=10, height=40,
                               width=60)
    balance_txt.place(relx=0.0001, rely=0.004)

    total_balance.place(relx=0.03, rely=0.5)
    ba_amount = ctk.CTkEntry(manual_balance_update_frame, width=100, height=40, textvariable=ba_var, font=("Arial", 12))
    ba_amount.place(relx=0.4, rely=0.5)

    updateba = ctk.CTkButton(manual_balance_update_frame, text="Update", font=("Arial", 20, "bold"), fg_color="#BEE9E8",
                             hover_color="#9ACCD9", text_color="black", width=140, height=50, corner_radius=5,
                             command=update_balance)
    updateba.place(relx=0.7, rely=0.4)

    # transactions amount entry
    amount_label = ctk.CTkLabel(transactions, fg_color="#62B6CB", corner_radius=5, width=60, height=40,
                                text_color="black", font=("Arial", 20, "bold"), text="Amount: ")
    amount_label.place(relx=0.001, rely=0.01)
    amount_entry = ctk.CTkEntry(transactions, width=100, height=40, textvariable=amount_var, font=("Arial", 12))
    amount_entry.place(relx=0.1, rely=0.01)

    # transactions purpose entry
    purpose_label = ctk.CTkLabel(transactions, fg_color="#62B6CB", corner_radius=5, width=60, height=40,
                                 text_color="black", font=("Arial", 20, "bold"), text="Purpose of Transaction: ")
    purpose_label.place(relx=0.001, rely=0.13)
    purpose_options = ["Bills/Rent", "Necessities", "Transportation", "Healthcare", "Education", "Donations",
                       "Entertainment", "Other"]
    purpose_dropdown = ctk.CTkOptionMenu(transactions, variable=purpose_var, values=purpose_options, font=("Arial", 15),
                                         height=40, text_color="black", fg_color="#BEE9E8", button_color="#BEE9E8",
                                         button_hover_color="#A0D8D3")
    purpose_dropdown.place(relx=0.25, rely=0.13)

    # date menu
    date_label = ctk.CTkLabel(transactions, text="Date: ", font=("Arial", 20, "bold"), fg_color="#62B6CB",
                              corner_radius=5, height=40, width=30, text_color="black")
    date_label.place(relx=0.001, rely=0.28, anchor="w")
    date_dropdown = ctk.CTkOptionMenu(transactions, variable=date_var, values=date_options, font=("Arial", 15),
                                      height=40, text_color="black", fg_color="#BEE9E8", button_color="#BEE9E8",
                                      button_hover_color="#A0D8D3")
    date_dropdown.place(relx=0.083, rely=0.24)

    # need/want radio buttons
    need_want = ctk.CTkLabel(transactions, text="", fg_color="#62B6CB", corner_radius=5, height=80, width=400)
    need_want.place(relx=0.47, rely=0.01, anchor="nw")
    need_radio = ctk.CTkRadioButton(need_want, text="Need (N)", variable=need_var, value="Need",
                                    font=("Arial", 20, "bold"), width=40, text_color="black", fg_color="#BEE9E8",
                                    hover_color="#1B4965")
    need_radio.place(relx=0.1, rely=0.5, anchor="w")
    want_radio = ctk.CTkRadioButton(need_want, text="Want (W)", variable=need_var, value="Want",
                                    font=("Arial", 20, "bold"), width=40, text_color="black", fg_color="#BEE9E8",
                                    hover_color="#1B4965")
    want_radio.place(relx=0.5, rely=0.5, anchor="w")

    # inputs all info + updates budget/balance with the "command=" command
    input_button = ctk.CTkButton(transactions, text="Input Transaction", font=("Arial", 20, "bold"), fg_color="#9AC0BF",
                                 hover_color="#467F8D", height=40, text_color="black", width=300, corner_radius=10,
                                 command=on_t_input)
    input_button.place(relx=0.5, rely=0.24)

    # for data table, but sharvika you did say you would create a table yeah?
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

    transactions_table.place(relx=0.2, rely=0.4)

    # Deposits amount entry
    amountd_label = ctk.CTkLabel(deposits, fg_color="#62B6CB", corner_radius=5, width=60, height=40,
                                 text_color="black", font=("Arial", 20, "bold"), text="Amount: ")
    amountd_label.place(relx=0.001, rely=0.01)
    amountd_entry = ctk.CTkEntry(deposits, width=100, height=40, textvariable=amountd_var, font=("Arial", 12))
    amountd_entry.place(relx=0.1, rely=0.01)

    # source entry
    sourced_label = ctk.CTkLabel(deposits, fg_color="#62B6CB", corner_radius=5, width=60, height=40,
                                 text_color="black", font=("Arial", 20, "bold"), text="Source of Money: ")
    sourced_label.place(relx=0.001, rely=0.13)
    sourced_entry = ctk.CTkEntry(deposits, width=100, height=40, textvariable=sourced_var, font=("Arial", 12))
    sourced_entry.place(relx=0.2, rely=0.13)

    # date label +  dropdown
    dated_label = ctk.CTkLabel(deposits, text="Date: ", font=("Arial", 20, "bold"), fg_color="#62B6CB",
                               corner_radius=5, height=40, width=30, text_color="black")
    dated_label.place(relx=0.001, rely=0.28, anchor="w")
    dated_dropdown = ctk.CTkOptionMenu(deposits, variable=dated_var, values=date_options, font=("Arial", 15),
                                       height=40, text_color="black", fg_color="#BEE9E8", button_color="#BEE9E8",
                                       button_hover_color="#A0D8D3")
    dated_dropdown.place(relx=0.083, rely=0.24)

    # inputs deposits
    inputd_button = ctk.CTkButton(deposits, text="Input Deposit", font=("Arial", 20, "bold"), fg_color="#9AC0BF",
                                  hover_color="#467F8D", height=40, text_color="black", width=300, corner_radius=10,
                                  command=on_d_input)
    inputd_button.place(relx=0.5, rely=0.24)

    # for deposits table but sharvika, you did say you'll replace with a db table or smth, yeah?
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

    deposits_table.place(relx=0.2, rely=0.4)


show()
root.mainloop()

if __name__ == "__main__":
    show()
    hide()
