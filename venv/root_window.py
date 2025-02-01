import customtkinter as ctk

# creates a single global root instance that can be used in all files.
root = None
def root_init():
    global root
    if root == None:
        root = ctk.CTk()
        root.title("FBLA Coding and Programming Sharvika & Nikhila")
        root.geometry('1200x1000')
        root.minsize(1200, 1000)
        root.maxsize(1200, 1000)
        root.configure(fg_color="#1B4965")

    return root
