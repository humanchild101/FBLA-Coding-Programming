# NOTE FOR NIKHILA: add email sending feature

# NOTE FOR SHARVIKA: hmmmmm idk. just make sure all structural stuff is updated into your scripts files
# and check/ensure that database is there for all that need it

# imports
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import root_window
from root_window import *
import re
from email.mime.text import MIMEText
import smtplib

# initializing root window
root = root_window.root_init()
root.configure(fg_color="#1B4965")

# creating current page's frame
account_create = ctk.CTkFrame(root, fg_color="#1B4965")

# ALL Entry Fields
entry_fields = []

# String vars to hold user input
new_fname = tk.StringVar()
new_lname = tk.StringVar()
new_user_var = tk.StringVar()
new_pass_var = tk.StringVar()
pass_ver_var = tk.StringVar()
email_var = tk.StringVar()

# adding string var values to entry_fields list to loop through
entry_fields.append(new_fname)
entry_fields.append(new_lname)
entry_fields.append(new_user_var)
entry_fields.append(new_pass_var)
entry_fields.append(pass_ver_var)
entry_fields.append(email_var)

# code from GeeksForGeeks. Regex to verify a valid password
email_verify = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


# function for when the create account button is pressed. ensures that all entries all filled with valid inputs
def on_account_creation(button):
    button.configure(state="disabled")
    for i in entry_fields:
        if not i.get():
            messagebox.showwarning("Submission not permitted", "Please fill out all the text fields")
            button.configure(state="normal")
            return

    # if database already contains new_user_var.get() then dont add the account and display username already exists

    if not re.fullmatch(email_verify, email_var.get()):
        messagebox.showwarning("Submission not permitted", "Please enter a valid email, ex: abc@gmail.com")
        button.configure(state="normal")
        return

    if not new_pass_var.get() == pass_ver_var.get():
        messagebox.showwarning("Submission not permitted", "Re-typed password does not match original password")
        button.configure(state="normal")
        return

    else:
        smtp = smtplib.SMTP("smtp.gmail.com", 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.login("nikhilamadhavi@gmail.com", "uwxo diwy libt hpim")
        msg = MIMEText("Congratulations " + new_fname.get() + " " + new_lname.get() + "! Your account has been created successfully")
        msg['Subject'] = "Finance Management Account Creation"
        to = email_var.get()
        smtp.sendmail(from_addr="nikhilamadhavi@gmail.com", to_addrs=to, msg = msg.as_string())
        smtp.quit()
        messagebox.showinfo("Success", "Account created successfully!")
        for i in entry_fields:
            i.set("")

    button.configure(state="normal")

# hides page
def hide():
    account_create.forget()


# shows page
def show():
    root.configure(fg_color="#1B4965")

    # imports to avoid circular import error
    import login
    import home_page
    import inputs
    import view
    import help_p

    login.hide()
    home_page.hide()
    inputs.hide()
    view.hide()
    help_p.hide()

    account_create.pack(fill="both", expand=True)

    # center frame with border
    center_border = ctk.CTkFrame(account_create, fg_color="#BEE9E8", corner_radius=20, width=620, height=640)
    center_border.place(relx=0.5, rely=0.5, anchor="center")
    center_frame = ctk.CTkFrame(center_border, fg_color='#62B6CB', corner_radius=15,
                                width=center_border.winfo_screenmmwidth() + 15,
                                height=center_border.winfo_screenmmheight() + 17)  # 62B6CB
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create account label
    loginL = ctk.CTkLabel(center_frame, text="Create Your Account", text_color="white", font=("Arial", 20),
                          fg_color="#1B4965", padx=10, pady=10, corner_radius=15, width=600)
    loginL.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

    # first name entry frame + label + text field
    fname_frame = ctk.CTkFrame(center_frame, fg_color="#3095AE", corner_radius=15, width=600, height=30)
    fname_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky = "w")

    fname_label = ctk.CTkLabel(fname_frame, text="First name:", font=("Arial", 18), fg_color="#3095AE",text_color="black", pady=6, corner_radius=5)
    fname_input = ctk.CTkEntry(fname_frame, textvariable=new_fname, font=("Arial", 15), fg_color="#BEE9E8",text_color="black", width=150, corner_radius=5)
    fname_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    fname_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)

    # last name entry frame + label + text field
    lname_frame = ctk.CTkFrame(center_frame, fg_color="#3095AE", corner_radius=15, width=600, height=30)
    lname_frame.grid(row=1, column=1, columnspan=2, padx=5, pady=10, sticky="e")

    lname_label = ctk.CTkLabel(lname_frame, text="Last name:", font=("Arial", 18), fg_color="#3095AE", text_color="black", pady=6, corner_radius=5)
    lname_input = ctk.CTkEntry(lname_frame, textvariable=new_lname, font=("Arial", 15), fg_color="#BEE9E8", text_color="black", width=150, corner_radius=5)
    lname_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    lname_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)

    # username entry
    user_frame = ctk.CTkFrame(center_frame, fg_color = "#3095AE", corner_radius=15, width = 600, height= 30)
    user_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=10, sticky = "w")

    username_label = ctk.CTkLabel(user_frame, text="Enter a username:", font=("Arial", 18), fg_color="#3095AE",text_color="black", padx=5, pady=6, corner_radius=5)
    username_input = ctk.CTkEntry(user_frame, textvariable=new_user_var, font=("Arial", 15), fg_color="#BEE9E8",text_color="black", width=390, corner_radius=5)
    username_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    username_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)

    # password entry
    pass_frame = ctk.CTkFrame(center_frame, fg_color="#3095AE", corner_radius=15, width=600, height=40)
    pass_frame.grid(row=3, column=0, columnspan=2, padx=5, pady=10, sticky = "w")

    password_label = ctk.CTkLabel(pass_frame, text="Enter a password:", font=("Arial", 18), fg_color="#3095AE",text_color="black", padx=5, pady=6, corner_radius=5)
    password_input = ctk.CTkEntry(pass_frame, textvariable=new_pass_var, font=("Arial", 15), fg_color="#BEE9E8",text_color="black", width=390, corner_radius=5,show="*")
    pas_reqs = ctk.CTkLabel(pass_frame, text = "Suggestion: Include at least 3 numbers, 3 special chars, and 3 uppercase letters.", font=("Arial", 14), fg_color="#3095AE", text_color="black")

    password_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    password_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)
    pas_reqs.grid(row =2, column = 0,columnspan = 2)

    # password verification (ensures the same password is retyped)
    pass_frame = ctk.CTkFrame(center_frame, fg_color="#3095AE", corner_radius=15, width=600, height=50)
    pass_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky = "w")

    password_label = ctk.CTkLabel(pass_frame, text="Retype password", font=("Arial", 18), fg_color="#3095AE", text_color="black", padx=5, pady=6, corner_radius=5)
    password_input = ctk.CTkEntry(pass_frame, textvariable=pass_ver_var, font=("Arial", 15), fg_color="#BEE9E8", text_color="black", width=390, corner_radius=5,show="*")

    password_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    password_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)

    # email entry
    pass_frame = ctk.CTkFrame(center_frame, fg_color="#3095AE", corner_radius=15, width=600, height=50)
    pass_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky = "w")

    password_label = ctk.CTkLabel(pass_frame, text="Email", font=("Arial", 18), fg_color="#3095AE", text_color="black", padx=5, pady=6, width = 60,corner_radius=5)
    password_input = ctk.CTkEntry(pass_frame, textvariable=email_var, font=("Arial", 15), fg_color="#BEE9E8", text_color="black", width=390, corner_radius=5)

    password_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    password_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)

    # create account button
    create_frame = ctk.CTkFrame(center_frame, fg_color="#BEE9E8", corner_radius = 8, width = 160, height = 30)
    create_button = ctk.CTkButton(create_frame, text="Create this account", font=("Arial", 18), fg_color="#3095AE",hover_color="#246690", text_color="black", width=200, corner_radius=5, command= lambda: on_account_creation(create_button))
    create_frame.grid(row = 6, column = 0, columnspan = 2)
    create_button.grid(row=1, column=0, columnspan=2, pady=5, padx=5, ipady=5)

    #dividing line
    canvas = ctk.CTkCanvas(center_frame, width=500, height=3, bg="#1B4965", highlightthickness=0)
    canvas.grid(row=7, column=0, columnspan=2, pady=20)

    # button that takes user back to login page for if they already have an account
    signup_button = ctk.CTkButton(center_frame, text="Login to existing account", font=("Arial", 20), fg_color="#1B4965", hover_color="#246690", text_color="white", width=600, corner_radius=15, command=login.show)
    signup_button.grid(row=8, column=0, columnspan=2, pady=5, padx=5, ipady=6)


if __name__ == "__main__":
    show()
    hide()
