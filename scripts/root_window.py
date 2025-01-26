import customtkinter as ctk

root = None
def root_init():
    global root
    if root == None:
        root = ctk.CTk()
        root.title("FBLA Coding and Programming Sharvika & Nikhila")
        root.geometry('1000x1000')
        root.resizable(True, True)
    return root
