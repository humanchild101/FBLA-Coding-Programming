# NOTE FOR NIKHILA: add icons

# NOTE FOR SHARVIKA: make sure to carefully combine the latest changes in this w/ your db stuff.
# you'll probably have to add some things for db as well. make sure that no structure changes are deleted
# I'll also be more careful with commits and stuff after what happened yesterday TvT
# ONE OTHER THING: progress bars (or ig you're replacing w/ graph? if so, ignore the next few comments)
#
# they should move by how much ever percentage of the budget is used up. (IM STILL WORKING ON THE NEED WANT BUDGET INPUT)
# The "X" and "Y" should be the amount used out of specified budgets for needs/wants/total

# imports
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import root_window
from root_window import *
import datetime
from dateutil.relativedelta import relativedelta
import PIL
from PIL import Image
import menu_bar
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

# initializing root window + home page frame
root = root_window.root_init()
home_page = ctk.CTkFrame(root, fg_color="#BEE9E8")

# top navigation bar frame
top_nav = ctk.CTkFrame(home_page, fg_color="#33739A", height=70, corner_radius=0)
top_nav.configure(fg_color="#33739A")

# welcome-label wih the user's username
welcome_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx=20, height=80, width=500, text="")
user_label = ctk.CTkLabel(welcome_label, text="Welcome, usr123!  ", fg_color="#1B4965", font=("Arial", 20, "bold"),
                          text_color="#BEE9E8", padx=20, height=70)

monthly_budget_frame = ctk.CTkFrame(home_page, fg_color="#62B6CB", corner_radius=20, width=475, height=510)

# image files for the status
face1 = ctk.CTkImage(light_image=Image.open("faces\very_happy.png"),
                     size=(70, 70))
face2 = ctk.CTkImage(light_image=Image.open("faces\happy.png"), size=(70, 70))
face3 = ctk.CTkImage(light_image=Image.open("faces\neutral.png"), size=(70, 70))
face4 = ctk.CTkImage(light_image=Image.open("faces\sad.png"), size=(70, 70))
face5 = ctk.CTkImage(light_image=Image.open("faces\very_sad.png"), size=(70, 70))

# status area
status_area = ctk.CTkLabel(user_label, text="", image=face1, fg_color="#1B4965", font=("Arial", 30, "bold"),
                           text_color="#BEE9E8", padx=20, height=70, width=80)

# String var for the notes + notes box + notes frame
notes_var = tk.StringVar()
notes_frame = ctk.CTkFrame(home_page, fg_color="#62B6CB", width=470, height=250, corner_radius=20)
notes_box = ctk.CTkTextbox(notes_frame, width=430, height=140, state="disabled", corner_radius=5,
                           fg_color="#1B4965")
#current month
current_month = datetime.datetime.now().strftime("%B")
current_date = datetime.datetime.now()
past_12_months = [(current_date - relativedelta(months=i)).strftime("%Y-%m") for i in range(12)]

# line graph data SHARVIKAAA (for total used... you have to input some random values
# into the db for past 12 months and then get them to show up in this total_used list
# for actual values you have to take all transactions in a certain month, and then add them together
# and then divide by the currently stated budget
monthly_total_expenses = {'month': past_12_months, 'total_used': []}

dataframe = pd.DataFrame(monthly_total_expenses)
figure = plt.Figure(fig_size = (5,4), dpi = 100)
# rows, columns, index pos (the 1,1,1)
figure_plot = figure.add_subplot(1,1,1)
figure_plot.set_ylabel("Total Monthly Expenses")
line_graph = FigureCanvasTkAgg(figure, monthly_budget_frame)
dataframe = dataframe[("month", "total_used")].groupby("month").sum()
dataframe.plot(kind = "line", legend =True, ax = figure_plot, color = "b", marker = "o", fontsize =10)


# next 5 functions are for when the face buttons are clicked
def on_v_happy():
    status_area.configure(image=face1)


def on_happy():
    status_area.configure(image=face2)


def on_neu():
    status_area.configure(image=face3)


def on_sad():
    status_area.configure(image=face4)


def on_v_sad():
    status_area.configure(image=face5)


# SHARVIKAAAAAAA you have to put the txt they enter the in the database and then save it every time it updates
# I put the notes_var variable for now, but idk you might have to replace that w/ something in the database


# updates notes
def update_notes_var():
    notes_var.set(notes_box.get("0.0", "end-1c"))


# edit notes
def edit_notes():
    notes_box.configure(state="normal")
    notes_box.delete("0.0", "end-1c")
    notes_box.insert("0.0", notes_var.get())


# save notes
def save_notes():
    notes_box.configure(state="disabled")
    update_notes_var()
    notes_box.delete("0.0", "end-1c")
    notes_box.insert("0.0", notes_var.get())


# hide page
def hide():
    home_page.forget()


# show page
def show():
    root.configure(fg_color="#BEE9E8")

    # imports
    import login
    import create_account
    import inputs
    import view
    import help_p

    login.hide()
    create_account.hide()
    inputs.hide()
    view.hide()
    help_p.hide()

    # initializing the size menu
    side_menu = menu_bar.menu_init(home_page)
    side_menu.forget()
    menu_bar.animate_backward()

    home_page.pack(fill="both", expand=True)  # #62B6CB
    top_nav.grid(row=0, column=0, columnspan=4, sticky="nw")

    # welcome and user-name sign
    welcome_label.grid(row=0, column=0)
    user_label.grid(row=0, column=0, sticky="w", padx=2)

    status_area.grid(row=0, column=1, sticky="w", padx=2)

    # ADD SMILY FACE HERE ^

    # home tab name
    home_label = ctk.CTkLabel(top_nav, fg_color="#1B4965", padx=20, height=80, width=200, text="")
    home_label.grid(row=0, column=1, padx=12)
    tab_label = ctk.CTkLabel(home_label, text="HOME", font=("Arial", 20, "bold"), text_color="#BEE9E8", padx=20,
                             height=70, width=100)
    tab_label.grid(row=0, column=0, padx=2, sticky="w")

    # Add Home icon here ^

    # for other buttons like menu / log out / possibly settings
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

    # frame for putting recent spending info
    rec_spen_frame = ctk.CTkFrame(home_page, fg_color="#62B6CB", corner_radius=20, width=400, height=270)
    rec_spen_frame.grid(row=1, column=0, padx=20, pady=20, sticky="nw")

    # recent spendings
    rec_spen = ctk.CTkLabel(rec_spen_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 20, "bold"),
                            text="Your Three Most Recent Expenses", corner_radius=100, width=200, height=40)
    rec_spen.place_configure(relx=0.04, rely=0.01)

    p1 = ctk.CTkLabel(rec_spen_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                      text="Purpose1   -   $$   -   XX/XX/XXXX", corner_radius=100, width=200)
    p1.place_configure(relx=0.15, rely=0.15)

    p2 = ctk.CTkLabel(rec_spen_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                      text="Purpose2   -   $$   -   XX/XX/XXXX", corner_radius=100, width=200)
    p2.place_configure(relx=0.15, rely=0.23)

    p3 = ctk.CTkLabel(rec_spen_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                      text="Purpose3   -   $$   -   XX/XX/XXXX", corner_radius=100, width=200)
    p3.place_configure(relx=0.15, rely=0.31)

    # recent deposits
    rec_dep = ctk.CTkLabel(rec_spen_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 20, "bold"),
                           text="Your Three Most Recent Deposits", corner_radius=100, width=200, height=40)
    rec_dep.place_configure(relx=0.04, rely=0.45)

    d1 = ctk.CTkLabel(rec_spen_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                      text="Source1   -   $$   -   XX/XX/XXXX", corner_radius=100, width=200)
    d1.place_configure(relx=0.15, rely=0.59)

    d2 = ctk.CTkLabel(rec_spen_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                      text="Source2   -   $$   -   XX/XX/XXXX", corner_radius=100, width=200)
    d2.place_configure(relx=0.15, rely=0.67)

    d3 = ctk.CTkLabel(rec_spen_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                      text="Source3   -   $$   -   XX/XX/XXXX", corner_radius=100, width=200)
    d3.place_configure(relx=0.15, rely=0.75)

    # Recent transactions + deposit for x purpose and from x source
    trandeps_frame = ctk.CTkFrame(home_page, fg_color="#62B6CB", corner_radius=20, width=400, height=220)
    trandeps_frame.grid(row=2, column=0, padx=20, sticky="nw")

    # most sought out purpose for transactions SHARVIKAAAAAA
    most_trans = ctk.CTkLabel(trandeps_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 18, "bold"),
                              text="Most Transactions For These Purpose:", corner_radius=100, width=170, height=40)
    most_trans.place_configure(relx=0.04, rely=0.05)

    hp1 = ctk.CTkLabel(trandeps_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                       text="Highest Transactions #1   -  Total $$", corner_radius=100, width=200)
    hp1.place_configure(relx=0.07, rely=0.20)

    hp2 = ctk.CTkLabel(trandeps_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                       text="Highest Transactions #2   -  Total $$", corner_radius=100, width=200)
    hp2.place_configure(relx=0.07, rely=0.32)

    # most sought out source for deposits SHARVIKAAAAAA
    most_deps = ctk.CTkLabel(trandeps_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 18, "bold"),
                             text="Most Deposits From These Sources:", corner_radius=100, width=170, height=40)
    most_deps.place_configure(relx=0.04, rely=0.45)

    hp1 = ctk.CTkLabel(trandeps_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                       text="Highest Deposits #1   -   Total $$", corner_radius=100, width=200)
    hp1.place_configure(relx=0.07, rely=0.6)

    hp2 = ctk.CTkLabel(trandeps_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 15),
                       text="Highest Deposits #2   -   Total $$", corner_radius=100, width=200)
    hp2.place_configure(relx=0.07, rely=0.72)

    # total balance frame
    total_balance_frame = ctk.CTkFrame(home_page, fg_color="#62B6CB", corner_radius=20, width=400, height=320)
    total_balance_frame.grid(row=3, column=0, padx=20, pady=20, sticky="nw")

    balance_text = ctk.CTkLabel(total_balance_frame, fg_color="#62B6CB", corner_radius=20, text_color="black",
                                text="Total Balance ~ ", font=("Arial", 45, "bold"))
    balance_text.place(relx=0.02, rely=0.1)

    balance = ctk.CTkLabel(total_balance_frame, fg_color="#62B6CB", corner_radius=20, text_color="black", text="$0.00",
                           font=("Arial", 70, "bold"))
    balance.place(relx=0.02, rely=0.45)

    # notes frame
    notes_frame.place(relx=0.37, rely=0.63)
    notes = ctk.CTkLabel(notes_frame, fg_color="#BEE9E8", text="Notes ~ ", text_color="black",
                         font=("Arial", 25, "bold"), corner_radius=20, padx=20, pady=10, width=450)
    notes.grid(row=0, column=0, sticky="w", padx=10, pady=10)
    notes_box.grid(row=1, column=0, ipady=15, pady=15, padx=20)

    # buttons for editing and saving notes
    edit_button = ctk.CTkButton(notes_frame, text="Edit", font=("Arial", 15, "bold"), fg_color="#BEE9E8",
                                hover_color="#9ACCD9", text_color="black", width=130, height=30, corner_radius=15,
                                command=edit_notes)
    edit_button.grid(row=2, column=0, padx=50, sticky="w", pady=10)

    save_button = ctk.CTkButton(notes_frame, text="Save", font=("Arial", 15, "bold"), fg_color="#BEE9E8",
                                hover_color="#9ACCD9", text_color="black", width=130, height=30, corner_radius=15,
                                command=save_notes)
    save_button.place(relx=0.6, rely=0.872)


    # monthly budget frame
    monthly_budget_frame.place_configure(relx=0.37, rely=0.1)

    # update the month
    your_budget = ctk.CTkLabel(monthly_budget_frame, fg_color="#62B6CB", text_color="black", font=("Arial", 20, "bold"),
                               text="Your Spending Over Months", corner_radius=100, width=200, height=30)
    your_budget.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    canvas = ctk.CTkCanvas(monthly_budget_frame, width=430, height=3, bg="#1B4965", highlightthickness=0)
    canvas.grid(row=1, column=0, columnspan=2, pady=10, padx=20, sticky="w")

    line_graph.get_tk_widget().grid(row = 2, column = 0, sticky = "w")
    '''
    # frame for wants progress bar
    wants_frame = ctk.CTkFrame(monthly_budget_frame, fg_color="#539CCA", corner_radius=10, width=450, height=50)
    wants_frame.grid(row=2, column=0, columnspan=2, pady=30, padx=10, sticky="w")
    
    wants_label = ctk.CTkLabel(wants_frame, text="Wants", font=("Arial", 16, "bold"), text_color="#0C2B3E")
    wants_label.place(relx=0.05, rely=0.5, anchor="w")

    
    # Add a progress bar for wants SHARVIKAAAAA --> progress is set based on budget which is set in inputs by the user
    wants_progress = ctk.CTkProgressBar(wants_frame, width=280, height=20, corner_radius=10, fg_color="#BEE9E8",
                                        border_color="#1B4965", border_width=1)
    wants_progress.place(relx=0.2, rely=0.5, anchor="w")  # Position the progress bar next to the label
    wants_progress.set(0.1)
    

    wants_left = ctk.CTkLabel(wants_frame, width=20, height=15, corner_radius=10, fg_color="#539CCA",
                              text_color="#0C2B3E", font=("Arial", 16, "bold"), text="$X/$Y")
    wants_left.place(relx=0.9, rely=0.5, anchor="center")

    # frame for total progress bar
    needs_frame = ctk.CTkFrame(monthly_budget_frame, fg_color="#539CCA", corner_radius=10, width=450, height=50)
    needs_frame.grid(row=3, column=0, columnspan=2, pady=30, padx=10, sticky="w")

    needs_label = ctk.CTkLabel(needs_frame, text="Needs", font=("Arial", 16, "bold"), text_color="#0C2B3E")
    needs_label.place(relx=0.05, rely=0.5, anchor="w")  # Position the label on the left side of the frame

    
    # Add a progress bar for wants SHARVIKAAAAA --> progress is set based on budget which is set in inputs by the user
    needs_progress = ctk.CTkProgressBar(needs_frame, width=280, height=20, corner_radius=10, fg_color="#BEE9E8",
                                        border_color="#1B4965", border_width=1)
    needs_progress.place(relx=0.2, rely=0.5, anchor="w")  # Position the progress bar next to the label
    needs_progress.set(0.1)
    
    needs_left = ctk.CTkLabel(needs_frame, width=20, height=15, corner_radius=10, fg_color="#539CCA",
                              text_color="#0C2B3E", font=("Arial", 16, "bold"), text="$X/$Y")
    needs_left.place(relx=0.9, rely=0.5, anchor="center")

    # frame for total progress bar
    total_frame = ctk.CTkFrame(monthly_budget_frame, fg_color="#539CCA", corner_radius=10, width=450, height=50)
    total_frame.grid(row=4, column=0, columnspan=2, pady=30, padx=10, sticky="w")

    total_label = ctk.CTkLabel(total_frame, text="Total", font=("Arial", 16, "bold"), text_color="#0C2B3E")
    total_label.place(relx=0.05, rely=0.5, anchor="w")  # Position the label on the left side of the frame

    
    # Add a progress bar for wants SHARVIKAAAAA --> progress is set based on budget which is set in inputs by the user
    total_progress = ctk.CTkProgressBar(total_frame, width=280, height=20, corner_radius=10, fg_color="#BEE9E8",
                                        border_color="#1B4965", border_width=1)
    total_progress.place(relx=0.2, rely=0.5, anchor="w")  # Position the progress bar next to the label
    total_progress.set(0.1)
    
    total_left = ctk.CTkLabel(total_frame, width=20, height=15, corner_radius=10, fg_color="#539CCA",
                              text_color="#0C2B3E", font=("Arial", 16, "bold"), text="$X/$Y")
    total_left.place(relx=0.9, rely=0.5, anchor="center")
    '''


    # displays percent of total budget used SHARVIKAAAAAAAAAA
    percent_budget = ctk.CTkLabel(monthly_budget_frame, fg_color="#62B6CB", corner_radius=20, text_color="black",
                                  text="XYZ% of "+current_month+" Budget Used", font=("Arial", 20, "bold"))
    percent_budget.grid(row=5, column=0, columnspan=2, pady=25, ipady=10, padx=10, sticky="ew")

    # status frame
    status_frame = ctk.CTkFrame(home_page, fg_color="#62B6CB", corner_radius=20, width=238, height=850)
    status_frame.place_configure(relx=0.785, rely=0.1)

    # choose your status
    status_text = ctk.CTkLabel(status_frame, width=20, height=15, corner_radius=10, text_color="#0C2B3E",
                               font=("Arial", 30, "bold"), text="Choose\nYour Status!")
    status_text.place(relx=0.5, rely=0.048, anchor="center")

    very_happy = ctk.CTkButton(status_frame, fg_color="#CEFFFF", image=face1, text="", hover_color="#FFFFFF", width=10,
                               height=10, corner_radius=5, command=on_v_happy)
    very_happy.place(relx=0.5, rely=0.18, anchor="center")

    happy = ctk.CTkButton(status_frame, fg_color="#CEFFFF", image=face2, text="", hover_color="#FFFFFF", width=10,
                          height=10, corner_radius=5, command=on_happy)
    happy.place(relx=0.5, rely=0.36, anchor="center")

    neutral = ctk.CTkButton(status_frame, fg_color="#CEFFFF", image=face3, text="", hover_color="#FFFFFF", width=10,
                            height=10, corner_radius=5, command=on_neu)
    neutral.place(relx=0.5, rely=0.54, anchor="center")

    sad = ctk.CTkButton(status_frame, fg_color="#CEFFFF", text="", image=face4, hover_color="#FFFFFF", width=10,
                        height=10, corner_radius=5, command=on_sad)
    sad.place(relx=0.5, rely=0.72, anchor="center")

    very_sad = ctk.CTkButton(status_frame, fg_color="#CEFFFF", text="", image=face5, hover_color="#FFFFFF", width=10,
                             height=10, corner_radius=5, command=on_v_sad)
    very_sad.place(relx=0.5, rely=0.90, anchor="center")


show()
root.mainloop()

if __name__ == "__main__":
    show()
    hide()
