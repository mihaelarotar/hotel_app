from L4.UI.GUI import main_buttons
from tkinter import *


def access_main_menu():
    root_main = Tk()
    root_main.title("Main menu")
    root_main.geometry('500x300')

    menu_main = Menu(root_main)
    root_main.config(menu=menu_main)
    submenu_main = Menu(menu_main)
    menu_main.add_cascade(label="File", menu=submenu_main)
    submenu_main.add_command(label="Help", command=help)
    submenu_main.add_command(label="Exit app", command=root_main.destroy)

    main_buttons(root_main)
    root_main.mainloop()


access_main_menu()
