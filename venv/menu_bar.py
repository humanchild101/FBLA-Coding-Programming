import customtkinter as ctk

menu_bar = None
pos = 1.05  # Start position
in_start_pos = True

# Function to hide the old menu bars
def hide_previous_menu():
    global menu_bar
    if menu_bar is not None:
        menu_bar.destroy()  # Hide the old menu bar

def menu_init(parent, start_pos=1.05, end_pos=0.8):
    global menu_bar, pos, in_start_pos
    hide_previous_menu()  # hide previous menu bar
    menu_bar = ctk.CTkFrame(master=parent, fg_color="#1B4965", corner_radius=0, border_color="white", border_width=3)
    pos = start_pos
    menu_bar.place(relx=pos, rely=0, relwidth=abs(start_pos - end_pos), relheight=1)

    import home_page
    import inputs
    import view

    menu = ctk.CTkLabel(menu_bar, text="Menu", font=("Arial", 24, "bold"), fg_color="#33739A", text_color="white", width=240, height=70, corner_radius=0)
    menu.place(relx=0.01, rely=0)

    home = ctk.CTkButton(menu_bar, text="Home", font=("Arial", 24, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=240, height=50, corner_radius=0, border_color="#1B4965", border_width=2, command = home_page.show)
    home.place(relx=0.01, rely=0.08)

    input = ctk.CTkButton(menu_bar, text="Update Finances", font=("Arial", 24, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=240, height=50, corner_radius=0, border_color="#1B4965", border_width=2, command = inputs.show)
    input.place(relx=0.01, rely=0.125)

    view = ctk.CTkButton(menu_bar, text="View Finances", font=("Arial", 24, "bold"), fg_color="#BEE9E8", hover_color="#9ACCD9", text_color="black", width=240, height=50, corner_radius=0, border_color="#1B4965", border_width=2, command = view.show)
    view.place(relx=0.01, rely=0.17)
    menu_bar.lift()
    return menu_bar

def animate():
    global in_start_pos, menu_bar
    menu_bar.lift()
    if in_start_pos:
        animate_forward()
    else:
        animate_backward()


def animate_forward():
    global pos, in_start_pos, menu_bar
    menu_bar.lift()

    if pos > 0.8:
        pos -= 0.01
        menu_bar.place(relx= pos, rely=0, relwidth=abs(1.05 - 0.8), relheight=1)
        menu_bar.after(10, animate_forward)
    else:
         in_start_pos = False


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

if __name__ == "__main__":
    hide_previous_menu()
    menu_init()
    animate()
    animate_backward()
    animate_forward()