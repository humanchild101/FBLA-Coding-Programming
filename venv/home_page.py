import customtkinter as ctk
import tkinter as tk  # for StringVar + messagebox + lines
from tkinter import messagebox
import login
from login import *
import root_window
from root_window import *

root = root_window.root_init()
home_page = ctk.CTkFrame(root, fg_color="#1B4965")

def show_home_page():
    home_page.pack(fill="both", expand=True)  # #62B6CB

    top_nav = ctk.CTkFrame(home_page, fg_color="#BEE9E8", height=80, corner_radius=0)
    top_nav.pack(fill="x", side="top")


    # welcome and user sign
    welcome_label = ctk.CTkLabel(top_nav, fg_color="#62B6CB", padx = 20, height = 80, width =500, text = "")
    welcome_label.grid(row = 0, column = 0)
    #SHARVIKAAAAA USER NAME HEREEEE (ignore my uppercase im just hoping you see the comments among the rest)
    user_label = ctk.CTkLabel(welcome_label, text="Welcome, usr123!  ", fg_color= "#62B6CB",font=("Arial", 20, "bold"), text_color="black", padx = 20, height = 70)
    user_label.grid(row = 0, column = 0, sticky ="w", padx = 2)

    #ADD SMILY FACE HERE ^

    # home tab name
    home_label = ctk.CTkLabel(top_nav, fg_color="#62B6CB", padx = 20, height = 80, width =200, text = "")
    home_label.grid(row=0, column = 1, padx = 12)
    tab_label = ctk.CTkLabel(home_label, text="Home", font=("Arial", 20, "bold"), text_color="black", padx = 20, height = 70, width = 100)
    tab_label.grid(row = 0, column = 0, padx = 2, sticky = "w")

    #Add Home icon here ^

    #this is for other icons like settings and menu bar to open side navigation menu (nav menu will also include home, tab 1, tab 2, log out, and settings)
    icon_label = ctk.CTkFrame(top_nav, fg_color="#62B6CB", height=70, width=500, corner_radius=0)
    icon_label.grid(row=0, column=2, ipadx=28, ipady = 5)
    #button for nav menu
    sidenav_button = ctk.CTkButton(icon_label, text="Menu", font=("Arial", 20, "bold"), fg_color="#3095AE",hover_color="#246690", text_color="black", width=170, height = 50, corner_radius=5)
    sidenav_button.grid(row = 0, column = 0, padx = 30,pady = 10, sticky = "w")
    #button for settings
    settings_button = ctk.CTkButton(icon_label, text="Settings", font=("Arial", 20, "bold"), fg_color="#3095AE",hover_color="#246690", text_color="black", width=170, height = 50, corner_radius=5)
    settings_button.grid(row = 0, column = 1, padx = 30, pady = 10, sticky = "w")




show_home_page()
root.mainloop()