# NOTE FOR NIKHILA: CREDIT THAT ONE YT CHANNEL HERE. MOST OF THIS CODE IS FROM THEIR EXAMPLE. (Also add delete account option LATER)

# NOTE FOR SHARVIKA: Once I have added delete account, i'll let you know where that is, so database probably has to be done for that also (LATER NOT NOW)

import customtkinter as ctk

menu_bar = None
pos = 1.05
in_start_pos = True

# Function to hide the old menu bars
def hide_previous_menu():
    global menu_bar
    if menu_bar is not None:
        menu_bar.destroy()  # delete the old menu bar

# this allows for the menu to be initialized in different files
def menu_init(parent, start_pos=1.05, end_pos=0.8):
    global menu_bar, pos, in_start_pos
    hide_previous_menu()  # hide previous menu bar if any
    menu_bar = ctk.CTkFrame(master=parent, fg_color="#1B4965", corner_radius=0, border_color="white", border_width=3)
    pos = start_pos
    menu_bar.place(relx=pos, rely=0, relwidth=abs(start_pos - end_pos), relheight=1)

    import home_page
    import inputs
    import view
    import login
    import help_p

    menu = ctk.CTkLabel(menu_bar, text="Menu", font=("Arial", 24, "bold"), fg_color="#33739A", text_color="white", width=240, height=70, corner_radius=0)
    menu.place(relx=0.01, rely=0)

    home = ctk.CTkButton(menu_bar, text="Home", font=("Arial", 24, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=240, height=50, corner_radius=0, border_color="#1B4965", border_width=2, command = home_page.show)
    home.place(relx=0.01, rely=0.08)

    input = ctk.CTkButton(menu_bar, text="Update Finances", font=("Arial", 24, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=240, height=50, corner_radius=0, border_color="#1B4965", border_width=2, command = inputs.show)
    input.place(relx=0.01, rely=0.125)

    view = ctk.CTkButton(menu_bar, text="View Finances", font=("Arial", 24, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=240, height=50, corner_radius=0, border_color="#1B4965", border_width=2, command = view.show)
    view.place(relx=0.01, rely=0.17)

    help_m = ctk.CTkButton(menu_bar, text="Usage Manual", font=("Arial", 24, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=240, height=50, corner_radius=0, border_color="#1B4965", border_width=2, command=help_p.show)
    help_m.place(relx=0.01, rely=0.215)

    log_out = ctk.CTkButton(menu_bar, text="Log Out", font=("Arial", 24, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=240, height=50, corner_radius=0, border_color="#1B4965", border_width=2, command=login.show)
    log_out.place(relx=0.01, rely=0.260)


    menu_bar.lift()

    return menu_bar

# animates the menu bar
def animate():
    global in_start_pos, menu_bar
    menu_bar.lift()
    if in_start_pos:
        animate_forward()
    else:
        animate_backward()


# animates forward
def animate_forward():
    global pos, in_start_pos, menu_bar
    menu_bar.lift()

    if pos > 0.8:
        pos -= 0.01
        menu_bar.place(relx= pos, rely=0, relwidth=abs(1.05 - 0.8), relheight=1)
        menu_bar.after(10, animate_forward)
    else:
         in_start_pos = False


# animates backwards
def animate_backward():
    global pos, in_start_pos, menu_bar
    menu_bar.lift()
    if pos < 1.05:
         pos += 0.01
         menu_bar.place(relx= pos, rely=0, relwidth=abs(1.05 - 0.8), relheight=1)
         menu_bar.after(10, animate_backward)
    else:
         in_start_pos = True
    menu_bar.forget()

