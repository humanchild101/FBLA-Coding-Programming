import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox + lines
from tkinter import messagebox
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

root = root_window.root_init()
view_page = ctk.CTkFrame(root, fg_color="#BEE9E8")

top_nav = ctk.CTkFrame(view_page, fg_color="#33739A", height=70, corner_radius=0)
top_nav.configure(fg_color="#33739A")
welcome_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx=20, height=80, width=500, text="")
user_label = ctk.CTkLabel(welcome_label, text=f"Welcome, {first_name} {last_name}!", fg_color="#1B4965",
                          font=("Arial", 20, "bold"), text_color="#BEE9E8", padx=20, height=70)

notes_var = tk.StringVar()

# I WILL CHANGE THE FILE PATHS LATER ONCE WE GET RID OF VENV
face1 = ctk.CTkImage(light_image=Image.open("faces/very_happy.png"), size=(70, 70))
face2 = ctk.CTkImage(light_image=Image.open("faces/happy.png"), size=(70, 70))
face3 = ctk.CTkImage(light_image=Image.open("faces/neutral.png"), size=(70, 70))
face4 = ctk.CTkImage(light_image=Image.open("faces/sad.png"), size=(70, 70))
face5 = ctk.CTkImage(light_image=Image.open("faces/very_sad.png"), size=(70, 70))

status_area = ctk.CTkLabel(user_label, text="", image=face1, fg_color="#1B4965", font=("Arial", 30, "bold"),
                           text_color="#BEE9E8", padx=20, height=70, width=80)


def hide():
    view_page.forget()


def show():
    root.configure(fg_color="#BEE9E8")

    import login
    import create_account
    import home_page
    import inputs

    login.hide()
    create_account.hide()
    home_page.hide()
    inputs.hide()

    def filter_button_clicked():
        income_expense = income_expense_dropdown.get()
        need_want = need_want_dropdown.get()
        date_range = date_range_dropdown.get()
        amount_range = amount_range_dropdown.get()
        source = sources_dropdown.get()
        purpose = purposes_dropdown.get()

        income_expense_filter = ""
        need_want_filter = ""
        date_range_filter = ""
        amount_range_filter = ""

        #SHARVIKAAAAAA do what you need to with these new things
        source_filter = ""
        purpose_filter = ""

        if income_expense != "All":
            income_expense_filter = f"AND income_or_expense = LOWER('{income_expense}')"

        #SHAVRIKAAAA IF THE THING CHOSEN IS INCOME, DO NOT TAAKE INTO CONSIDERATION THE PURPOSES INPUTTED IN THE PURPOSE DROPDOWN. VICE VERSA FOR EXPENSES
        if income_expense == "Income":
            sources_dropdown.configure(state = "normal")
            purposes_dropdown.set("None")
            purposes_dropdown.configure(state = "disabled")

        if income_expense == "Expense":
            sources_dropdown.configure(state = "disabled")
            sources_dropdown.set("None")
            purposes_dropdown.configure(state = "normal")
          
        if need_want != "All":
            need_want_filter = f"AND need_or_want = LOWER('{need_want}')"

        if date_range != "All":
            if date_range == "Last 7 Days":
                start_date = datetime.datetime.now() - datetime.timedelta(days=7)
                date_range_filter = f"AND date_of_transaction >= '{start_date}'"
            elif date_range == "Last 30 Days":
                start_date = datetime.datetime.now() - datetime.timedelta(days=30)
                date_range_filter = f"AND date_of_transaction >= '{start_date}'"
            elif date_range == "This Year":
                start_date = datetime.datetime(datetime.datetime.now().year, 1, 1)
                date_range_filter = f"AND date_of_transaction >= '{start_date}'"

        if amount_range != "All":
            if amount_range == "Below $2000":
                amount_range_filter = "AND amount < 2000"
            elif amount_range == "$2001 - $10000":
                amount_range_filter = "AND amount >= 2000 AND amount <= 10000"
            elif amount_range == "Above $10000":
                amount_range_filter = "AND amount > 10000"

        query = f"""
            SELECT income_or_expense, source, need_or_want, amount, date_of_transaction, note 
            FROM transactions 
            WHERE user_id = {user_id} {income_expense_filter} {need_want_filter} {date_range_filter} {amount_range_filter}
        """

        print("Executing Query:", query)  # Debugging
        data = db.fetch_all_query(query)
        print("Data Retrieved:", data)  # Debugging

        # Clear the table
        for widget in table_frame.winfo_children():
            widget.destroy()

        # Add Column Headers
        for col_index, col_name in enumerate(columns):
            label = ctk.CTkLabel(table_frame, text=col_name, font=("Arial", 14, "bold"))
            label.grid(row=0, column=col_index, padx=10, pady=5)

        # If no data, show a message instead of leaving it blank
        if not data:
            empty_label = ctk.CTkLabel(table_frame, text="No results found", font=("Arial", 14, "italic"), text_color="red")
            empty_label.grid(row=1, column=0, columnspan=len(columns), padx=10, pady=10)
            return

        # Populate Table with Data
        for row_index, row in enumerate(data):
            for col_index, value in enumerate(row):
                label = ctk.CTkLabel(table_frame, text=str(value), font=("Times New Roman", 14))
                label.grid(row=row_index + 1, column=col_index, padx=12, pady=5, sticky="w")


    view_page.pack(fill="both", expand=True)  # #62B6CB
    top_nav.grid(row=0, column=0, columnspan=4, sticky="nw")

    side_menu = menu_bar.menu_init(view_page)
    side_menu.forget()
    menu_bar.animate_backward()

    # welcome and user sign
    welcome_label.grid(row=0, column=0)
    user_label.grid(row=0, column=0, sticky="w", padx=2)

    status_area.grid(row=0, column=1, sticky="w", padx=2)

    # view tab name
    inputs_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx=20, height=80, width=200, text="")
    inputs_label.grid(row=0, column=1, padx=12)
    tab_label = ctk.CTkLabel(inputs_label, text="VIEW FINANCES", font=("Arial", 20, "bold"), text_color="#BEE9E8",
                             padx=20, height=70, width=100)
    tab_label.grid(row=0, column=0, padx=2, sticky="w")

    # Add inputs icon here ^

    # this is for other icons like settings and menu bar to open side navigation menu (nav menu will also include home, tab 1, tab 2, log out, and poossibly settings)
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

    # Database Container
    database_frame = ctk.CTkFrame(view_page, fg_color="#BEE9E8", height=500)
    database_frame.grid(row=2, column=0, columnspan=4, padx=20, pady=(10, 20), sticky="ns")

    # Configure the grid to expand the table
    view_page.grid_rowconfigure(2, weight=1)  
    view_page.grid_columnconfigure(0, weight=1)  

    # Filter Options Div 
    filter_frame = ctk.CTkFrame(view_page, fg_color="#62B6CB", height=140)
    filter_frame.grid(row=1, column=0, columnspan=4, padx=20, pady=(10, 5), sticky="ew")

    filter_label = ctk.CTkLabel(filter_frame, text="Filter Options:", font=("Arial", 16, "bold"), text_color="black")
    filter_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    # Labels for Dropdowns
    income_expense_label = ctk.CTkLabel(filter_frame, text="Income/Expense", font=("Arial", 12, "bold"), text_color= "black")
    income_expense_label.grid(row=1, column=0, padx=10, pady=(5, 0), sticky="w")

    need_want_label = ctk.CTkLabel(filter_frame, text="Need or Want", font=("Arial", 12, "bold"), text_color= "black")
    need_want_label.grid(row=1, column=1, padx=10, pady=(5, 0), sticky="w")

    date_range_label = ctk.CTkLabel(filter_frame, text="Date Range", font=("Arial", 12, "bold"), text_color= "black")
    date_range_label.grid(row=1, column=2, padx=10, pady=(5, 0), sticky="w")

    amount_range_label = ctk.CTkLabel(filter_frame, text="Amount Range", font=("Arial", 12, "bold"), text_color= "black")
    amount_range_label.grid(row=1, column=3, padx=10, pady=(5, 0), sticky="w")

    sources_label = ctk.CTkLabel(filter_frame, text="Sources", font=("Arial", 12, "bold"), text_color= "black") #SHARVIKAAAAAA in values, you have to also add in the sources/purposes that the user adds from inputs page. you can reconfigure what values the dropdown holds with the .configure(values = []) function
    sources_label.grid(row=1, column=4, padx=10, pady=5, sticky="w")

    purposes_label = ctk.CTkLabel(filter_frame, text="Purposes", font=("Arial", 12, "bold"), text_color= "black") #SHARVIKAAAAAA in values, you have to also add in the sources/purposes that the user adds from inputs page. you can reconfigure what values the dropdown holds with the .configure(values = []) function
    purposes_label.grid(row=1, column=5, padx=10, pady=5, sticky="w")

    '''columns_label = ctk.CTkLabel(filter_frame, text="Select Columns", font=("Arial", 12, "bold"))
    columns_label.grid(row=1, column=4, padx=10, pady=(5, 0), sticky="w")'''

    # Dropdowns (Placed Below Labels)
    income_expense_dropdown = ctk.CTkComboBox(filter_frame, values=["All", "Income", "Expense"], width=150)
    income_expense_dropdown.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    need_want_dropdown = ctk.CTkComboBox(filter_frame, values=["All", "Need", "Want"], width=150)
    need_want_dropdown.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    date_range_dropdown = ctk.CTkComboBox(filter_frame, values=["All", "Last 7 Days", "Last 30 Days", "This Year"], width=150)
    date_range_dropdown.grid(row=2, column=2, padx=10, pady=5, sticky="w")

    amount_range_dropdown = ctk.CTkComboBox(filter_frame, values=["All", "Below $2000", "$2001 - $10000", "Above $10000"], width=150)
    amount_range_dropdown.grid(row=2, column=3, padx=10, pady=5, sticky="w")

    # Apply Filter Button (Now below all dropdowns)
    sources_dropdown = ctk.CTkComboBox(filter_frame, values=["None", "All", "Job", "Scholarship"], width=150) #SHARVIKAAAAAA in values, you have to also add in the sources/expenses that the user adds from inputs page. you can reconfigure what values the dropdown holds with the .configure(values = []) function
    sources_dropdown.grid(row=2, column=4, padx=10, pady=5, sticky="w")

    purposes_dropdown = ctk.CTkComboBox(filter_frame, values=["None", "All", "Bills/Rent", "Necessities", "Transportation", "Healthcare", "Education", "Donations", "Entertainment"], width=150) #SHARVIKAAAAAA in values, you have to also add in the sources/purposes that the user adds from inputs page. you can reconfigure what values the dropdown holds with the .configure(values = []) function
    purposes_dropdown.grid(row=2, column=5, padx=10, pady=5, sticky="w")

    # Apply Filter Button (Now below all dropdowns)
    apply_filter_button = ctk.CTkButton(filter_frame, text="Apply Filter", fg_color="#33739A", hover_color="#1B4965", width = 60, command = filter_button_clicked)
    apply_filter_button.grid(row=2, column=6, padx=10, pady=5, sticky="w")

    # Database Container (Expands to bottom)
    database_frame = ctk.CTkFrame(view_page, fg_color="#BEE9E8")
    database_frame.grid(row=2, column=0, columnspan=4, padx=20, pady=(10, 20), sticky="nsew")

    # Make the table take up full available space
    database_frame.grid_rowconfigure(0, weight=1)  # Expands vertically
    database_frame.grid_columnconfigure(0, weight=1)  # Expands horizontally

    # Table Div (Fills entire remaining space)
    table_frame = ctk.CTkScrollableFrame(database_frame)
    table_frame.pack(fill="both", expand=True, padx=10, pady=5)  # Expands dynamically

    # Fetch Data
    data = db.fetch_all_query("SELECT income_or_expense, source, need_or_Want, amount, date_of_transaction, note FROM transactions")
    columns = ["Income/Expense", "Source", "Need/Want", "Amount", "Date", "Note"]

    # Add Column Headers
    for col_index, col_name in enumerate(columns):
        label = ctk.CTkLabel(table_frame, text=col_name, font=("Arial", 14, "bold"))
        label.grid(row=0, column=col_index, padx=10, pady=5, sticky="w")

    # Populate Table with Data
    for row_index, row in enumerate(data):
        for col_index, value in enumerate(row):
            label = ctk.CTkLabel(table_frame, text=str(value), font=("Times New Roman", 14))
            label.grid(row=row_index + 1, column=col_index, padx=12, pady=5, sticky="w")



if __name__ == "__main__":
    show()
    hide()
