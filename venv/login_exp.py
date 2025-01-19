import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox
from tkinter import messagebox

root = ctk.CTk()
root.title("FBLA Coding and Programming Sharvika & Nikhila")
root.geometry('1000x1000')
root.configure(fg_color = '#EE6055') #62B6CB
root.resizable(True, True)

def on_login():
    username_in = user_var.get()
    password_in = password_var.get()
    if not username_in and not password_in:
        messagebox.showwarning("No input", "Please enter a username and password")
    else:
        if not username_in:
            messagebox.showwarning("No input", "Please enter a username")

        if not password_in:
            messagebox.showwarning("No input", "Please enter a password")

# center frame
center_frame = ctk.CTkFrame(root, fg_color = '#FFD97D', corner_radius=15)  #62B6CB
center_frame.place(relx = 0.5, rely = 0.5, anchor="center")

# login label 1B4965
loginL = ctk.CTkLabel(center_frame, text = "Login To Your Account: ",text_color="black", font = ("Arial", 20), fg_color = "#EE964B", padx = 10, pady = 10, corner_radius=15, width = 600)
loginL.grid(row = 0, column = 0, columnspan = 2, sticky="w", padx = 5, pady = 5)

# username entry
user_var = tk.StringVar(value = "Username Here") #1B4965 and then BEE9E8
username_label = ctk.CTkLabel(center_frame, text = "Username", font = ("Arial", 18), fg_color = "#EE964B", text_color = "black", padx = 5, pady = 6,corner_radius=5)
username_input = ctk.CTkEntry(center_frame, textvariable=user_var, font=("Arial", 15), fg_color="#FFEED3", text_color="black", width=400, corner_radius=5)
username_label.grid(row=1, column=0, sticky="e", padx=5, pady=10, ipady = 4)
username_input.grid(row=1, column=1, sticky="w", padx=20, pady=10, ipady=5)

# password entry
password_var = tk.StringVar(value="Password Here")#1B4965 and then BEE9E8
password_label = ctk.CTkLabel(center_frame, text="Password ", font=("Arial", 18), fg_color="#EE964B",text_color="black", padx=5, pady=6, corner_radius=5)
password_input = ctk.CTkEntry(center_frame, textvariable=password_var, font=("Arial", 15), fg_color="#FFEED3", text_color = "black", width=400, show="*", corner_radius=5)
password_label.grid(row=2, column=0, sticky="e", padx=5, pady=10,ipady = 4)
password_input.grid(row=2, column=1, sticky="w", padx=20, pady=10, ipady=5)

# login button #1B4965 and then 246690
login_button = ctk.CTkButton(center_frame, text="Login", font=("Arial", 18), fg_color="#EE964B", hover_color="#CAE9FF", text_color="black", width=200, corner_radius=5, command=on_login)
login_button.grid(row=3, column=0, columnspan=2, pady=20, padx=150, sticky="e", ipady = 5)

root.mainloop()
