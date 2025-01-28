import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox + lines
from tkinter import messagebox
import root_window
from root_window import *
import re #for regex
import db_connect as db


#sample account:
#First Name - A, Last Name - B, Username - C, Password - AAA111!!!, Email - nikhilamadhavi@gmail.com


root = root_window.root_init()
account_create = ctk.CTkFrame(root, fg_color="#1B4965")
entry_fields = []
#ALL Entry Fields
new_fname = tk.StringVar()
new_lname = tk.StringVar()
new_user_var = tk.StringVar()
new_pass_var = tk.StringVar()
pass_ver_var = tk.StringVar()
email_var = tk.StringVar()

entry_fields.append(new_fname)
entry_fields.append(new_lname)
entry_fields.append(new_user_var)
entry_fields.append(new_pass_var)
entry_fields.append(pass_ver_var)
entry_fields.append(email_var)
#regex
password_verify = pattern = r'^(?=(.*[A-Z]){3,})(?=(.*[!@#$%^&*(),.?":{}|<>]){3,})(?=(.*[0-9]){3,}).*$' #from ChatGPT
email_verify = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b' #code from GeeksForGeeks

def on_account_creation():
    create_flag = False
    for i in entry_fields:
        if not i.get():
            messagebox.showwarning("Submission not permitted", "Please fill out all the text fields")
            return

        
        if not re.fullmatch(password_verify, pass_ver_var.get()):
            print(f"password string ::{pass_ver_var.get()}")
            messagebox.showwarning("Submission not permitted", "Password must have at least 3 special chars, 3 uppercase letters, and 3 numbers")
            return

        if not re.fullmatch(email_verify, email_var.get()):
            messagebox.showwarning("Submission not permitted", "Please enter a valid email, ex: abc@gmail.com")
            return

        if not new_pass_var.get() == pass_ver_var.get():
            messagebox.showwarning("Submission not permitted", "Re-typed password does not match original password")
            return

        else:
            create_flag=True
    
    if create_flag == True:
        #SQL statement to insert a new row to the table
        insertQuery = """
        INSERT into users (username, user_password, email, first_name, last_name) 
        VALUES ('{}', '{}', '{}', '{}', '{}');""".format(new_user_var.get(), new_pass_var.get(), email_var.get(), new_fname.get(), new_lname.get())
           

        try:
            db.insert_values(insertQuery)

        except(Exception) as error:
            if "violates unique constraint" in str(error): 
                #Username & Email are supposed to be unique
                #If not, warning will pop up
                messagebox.showwarning("Submission not permitted", "Username / Email already exists. Login?")

            else:
                messagebox.showwarning("Submission not permitted", "Error creating a new account")
            


def hide():
    account_create.forget()

def show():
    import login
    login.hide()
    account_create.pack(fill="both", expand=True)  # #62B6CB
    center_border = ctk.CTkFrame(account_create, fg_color = "#BEE9E8", corner_radius=20, width = 620, height= 640)
    center_border.place(relx= 0.5, rely = 0.5, anchor = "center")
    center_frame = ctk.CTkFrame(center_border, fg_color = '#62B6CB', corner_radius=15, width= center_border.winfo_screenmmwidth() + 15, height = center_border.winfo_screenmmheight()+17)  #62B6CB
    center_frame.place(relx = 0.5, rely = 0.5, anchor="center")

    loginL = ctk.CTkLabel(center_frame, text="Create Your Account", text_color="white", font=("Arial", 20), fg_color="#1B4965", padx=10, pady=10, corner_radius=15, width=600)
    loginL.grid(row=0, column=0, columnspan=2, padx=5, pady=5)


    #first name entry frame + label + text field
    fname_frame = ctk.CTkFrame(center_frame, fg_color="#3095AE", corner_radius=15, width=600, height=30)
    fname_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky = "w")

    fname_label = ctk.CTkLabel(fname_frame, text="First name:", font=("Arial", 18), fg_color="#3095AE",text_color="black", pady=6, corner_radius=5)
    fname_input = ctk.CTkEntry(fname_frame, textvariable=new_fname, font=("Arial", 15), fg_color="#BEE9E8",text_color="black", width=150, corner_radius=5)
    fname_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    fname_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)

    #last name entry frame + label + text field
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
    pas_reqs = ctk.CTkLabel(pass_frame, text = "Password must include at least 3 numbers, 3 special chars, and 3 uppercase letters.", font=("Arial", 14), fg_color="#3095AE", text_color="black")

    password_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    password_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)
    pas_reqs.grid(row =2, column = 0,columnspan = 2)

    # password verification
    pass_frame = ctk.CTkFrame(center_frame, fg_color="#3095AE", corner_radius=15, width=600, height=50)
    pass_frame.grid(row=4, column=0, columnspan=2, padx=5, pady=10, sticky = "w")

    password_label = ctk.CTkLabel(pass_frame, text="Retype password", font=("Arial", 18), fg_color="#3095AE", text_color="black", padx=5, pady=6, corner_radius=5)
    password_input = ctk.CTkEntry(pass_frame, textvariable=pass_ver_var, font=("Arial", 15), fg_color="#BEE9E8", text_color="black", width=390, corner_radius=5,show="*")

    password_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    password_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)

    # email
    pass_frame = ctk.CTkFrame(center_frame, fg_color="#3095AE", corner_radius=15, width=600, height=50)
    pass_frame.grid(row=5, column=0, columnspan=2, padx=5, pady=10, sticky = "w")

    password_label = ctk.CTkLabel(pass_frame, text="Email", font=("Arial", 18), fg_color="#3095AE", text_color="black", padx=5, pady=6, width = 60,corner_radius=5)
    password_input = ctk.CTkEntry(pass_frame, textvariable=email_var, font=("Arial", 15), fg_color="#BEE9E8", text_color="black", width=390, corner_radius=5)

    password_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady=4)
    password_input.grid(row=1, column=1, sticky="w", padx=15, pady=10, ipady=5)

    # create account button
    create_frame = ctk.CTkFrame(center_frame, fg_color="#BEE9E8", corner_radius = 8, width = 160, height = 30)
    create_button = ctk.CTkButton(create_frame, text="Create this account", font=("Arial", 18), fg_color="#3095AE",hover_color="#246690", text_color="black", width=200, corner_radius=5, command = on_account_creation)
    create_frame.grid(row = 6, column = 0, columnspan = 2)
    create_button.grid(row=1, column=0, columnspan=2, pady=5, padx=5, ipady=5)

    #dividing line
    canvas = ctk.CTkCanvas(center_frame, width=500, height=3, bg="#1B4965", highlightthickness=0)
    canvas.grid(row=7, column=0, columnspan=2, pady=20)

    #Have an account? login.. page
    signup_button = ctk.CTkButton(center_frame, text="Login to existing account", font=("Arial", 20), fg_color="#1B4965", hover_color="#246690", text_color="white", width=600, corner_radius=15, command=login.show)
    signup_button.grid(row=8, column=0, columnspan=2, pady=5, padx=5, ipady=6)

if __name__ == "__main__":
    show()
    hide()

