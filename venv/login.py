import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox + lines
from tkinter import messagebox
import root_window
from root_window import *


root = root_window.root_init()

# bg = #1B4965
# border = #BEE9E8
# frame = #62B6CB
# labels = #3095AE    (hover color = #246690)
# entries = #BEE9E8

#------------------------
login_page = ctk.CTkFrame(root, fg_color="#1B4965")
user_var = tk.StringVar(value="Username Here")  # 1B4965 and then BEE9E8
password_var = tk.StringVar(value="Password Here")  # 1B4965 and then BEE9E8


def on_login():
    username_in = user_var.get()
    password_in = password_var.get()
    if not username_in and not password_in:
        messagebox.showwarning("No input", "Please enter a username and password")
        return
    else:
        if not username_in:
            messagebox.showwarning("No input", "Please enter a username")
            return
        if not password_in:
            messagebox.showwarning("No input", "Please enter a password")
            return
    if username_in and password_in:
        messagebox.showinfo("Message", "This will take you to the next page.. well depending on what the user account is")

def forgot_password():
    messagebox.showinfo("Message", "I will create a new password changing window thing for this")

def create_new_account():
    import create_account
    create_account.show()

def hide():
    login_page.forget()

def show():
    import create_account
    create_account.hide()
    login_page.pack(fill="both", expand=True)  # #62B6CB

    # center frame w/ border
    center_border = ctk.CTkFrame(login_page, fg_color = "#BEE9E8", corner_radius=20, width = 620, height= 355)
    center_border.place(relx= 0.5, rely = 0.5, anchor = "center")
    center_frame = ctk.CTkFrame(center_border, fg_color = '#62B6CB', corner_radius=15)  #62B6CB
    center_frame.place(relx = 0.5, rely = 0.5, anchor="center")

    # login label 1B4965
    loginL = ctk.CTkLabel(center_frame, text = "Login To Your Account: ",text_color="white", font = ("Arial", 20), fg_color = "#1B4965", padx = 10, pady = 10, corner_radius=15, width = 600)
    loginL.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)

    # username entry
    username_label = ctk.CTkLabel(center_frame, text = "Username", font = ("Arial", 18), fg_color = "#3095AE", text_color = "black", padx = 5, pady = 6,corner_radius=5)
    username_input = ctk.CTkEntry(center_frame, textvariable=user_var, font=("Arial", 15), fg_color="#BEE9E8", text_color="black", width=400, corner_radius=5)
    username_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady = 4)
    username_input.grid(row=1, column=1, sticky="w", padx=20, pady=10, ipady=5)

    # password entry
    password_label = ctk.CTkLabel(center_frame, text="Password ", font=("Arial", 18), fg_color="#3095AE",text_color="black", padx=5, pady=6, corner_radius=5)
    password_input = ctk.CTkEntry(center_frame, textvariable=password_var, font=("Arial", 15), fg_color="#BEE9E8", text_color = "black", width=400, show="*", corner_radius=5)
    password_label.grid(row=2, column=0, sticky="e", padx=5, pady=10,ipady = 4)
    password_input.grid(row=2, column=1, sticky="w", padx=20, pady=10, ipady=5)

    # forgot password button
    forgot_button = ctk.CTkButton(center_frame, text="Forgot Password?", font=("Arial", 13), fg_color="#3095AE", hover_color="#246690", text_color="black", width=130, corner_radius=5, command=forgot_password)
    forgot_button.grid(row=3, column=1, columnspan=2, padx=50, sticky="e")

    # login button #1B4965 and then 246690
    login_button = ctk.CTkButton(center_frame, text="Login", font=("Arial", 18), fg_color="#3095AE", hover_color="#246690", text_color="black", width=200, corner_radius=5, command=on_login)
    login_button.grid(row=4, column=0, columnspan=2, pady=5, padx=50, ipady = 5)

    canvas = ctk.CTkCanvas(center_frame, width = 500, height = 3, bg = "#1B4965", highlightthickness= 0)
    canvas.grid(row = 5, column = 0, columnspan = 2, pady = 20)

    signup_button = ctk.CTkButton(center_frame, text="Create an account", font=("Arial", 20), fg_color="#1B4965", hover_color="#246690", text_color="white", width=600, corner_radius=15, command=create_new_account)
    signup_button.grid(row=6, column=0, columnspan=2, pady=5, padx=5, ipady = 6)

if __name__ == "__main__":
    show()
    hide()