from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from L4.Entities.guest import Guest
from L4.Repository.guestsmenu import GuestsMenu
from L4.Entities.room import Room
from L4.Repository.roomsmenu import RoomsMenu
from L4.Repository.hotelmenu import Hotel
from L4.Controller.controller import Controller
from datetime import date

lguests = []
lrooms = []
lreservations = []


def help():
    print("I need help!")

# ======================================================================================================================


repo1 = GuestsMenu(lguests)
control1 = Controller(repo1)

# Buttons for Guests menu
class guests_menu_buttons:

    def __init__(self, guests_menu, controller):
        self.guests_menu = guests_menu
        self.controller = controller

        self.frame = Frame(self.guests_menu)
        self.frame.pack()
        self.label = Label(self.frame)

        self.first_name = Label(self.frame, text="First name")
        self.first_name.grid(row=0, column=0, sticky=E)
        self.first_name_txt = Entry(self.frame)
        self.first_name_txt.grid(row=0, column=1, sticky=E)
        self.last_name = Label(self.frame, text="Last name")
        self.last_name.grid(row=1, column=0, sticky=E)
        self.last_name_txt = Entry(self.frame)
        self.last_name_txt.grid(row=1, column=1, sticky=E)
        self.new_name = Label(self.frame, text="New name")
        self.new_name.grid(row=6, column=2, sticky=E)
        self.new_name_txt = Entry(self.frame)
        self.new_name_txt.grid(row=6, column=3, sticky=E)

        self.labelFrame = ttk.LabelFrame(self.frame, text="Open a file")
        self.labelFrame.grid(row=0, column=3)
        self.button = ttk.Button(self.labelFrame, text="Browse a file", command=self.fileDialog)
        self.button.grid(row=0, column=4)

        self.empty = Label(self.frame)
        self.empty.grid(row=3)
        self.btn0 = Button(self.frame, text="Exit guests menu", command=self.guests_menu.destroy)
        self.btn0.grid(row=4, column=1, sticky=W)
        self.btn1 = Button(self.frame, text="Add guest", command=self.add_guest)
        self.btn1.grid(row=5, column=1, sticky=W)
        self.btn2 = Button(self.frame, text="Modify last name", command=self.change_name)
        self.btn2.grid(row=6, column=1, sticky=W)
        self.btn3 = Button(self.frame, text="Delete guest", command=self.delete_guest)
        self.btn3.grid(row=7, column=1, sticky=W)
        self.btn4 = Button(self.frame, text="Show guests", command=self.show_guests)
        self.btn4.grid(row=8, column=1, sticky=W)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetype=(("txt", "*.txt"),
                                                                                                  ("All Files", "*.*")))

    def add_guest(self):
        guest = Guest(self.first_name_txt.get(), self.last_name_txt.get())
        self.controller.add_guest(guest)
        # clear textboxes
        self.first_name_txt.delete(0, 'end')
        self.last_name_txt.delete(0, 'end')

    def delete_guest(self):
        guest = Guest(self.first_name_txt.get(), self.last_name_txt.get())
        self.controller.delete_guest(guest)
        # clear textboxes
        self.first_name_txt.delete(0, 'end')
        self.last_name_txt.delete(0, 'end')

    def change_name(self):
        guest = Guest(self.first_name_txt.get(), self.last_name_txt.get())
        self.controller.change_name(guest, self.new_name_txt.get())
        # clear textboxes
        self.first_name_txt.delete(0, 'end')
        self.last_name_txt.delete(0, 'end')
        self.new_name_txt.delete(0, 'end')

    def show_guests(self):
        root_guests_menu = Tk()
        root_guests_menu.title("Guest list")
        root_guests_menu.geometry('800x200')

        menu_guests_menu = Menu(root_guests_menu)
        root_guests_menu.config(menu=menu_guests_menu)
        submenu_guests_menu = Menu(menu_guests_menu)
        menu_guests_menu.add_cascade(label="File", menu=submenu_guests_menu)
        submenu_guests_menu.add_command(label="Help", command=help)
        submenu_guests_menu.add_command(label="Exit guests menu", command=root_guests_menu.destroy)

        # item = " ".join(self.controller.show_guests())
        # self.label = Label(root_guests_menu, text=str(self.controller.show_guests()))
        # self.label.pack()
        # self.label.configure(text=item)

        for item in self.controller.show_guests():
            self.label = Label(root_guests_menu, text=str(item))
            self.label.pack()

        root_guests_menu.mainloop()


'''
        l = self.controller.show_guests()
        for i in range(len(l)):
            self.label.destroy()
        for i in range(len(l)):
            self.label = Label(self.frame, text=str(l[i]))
            self.label.grid(row=i + 11, column=1)
'''

# ======================================================================================================================

repo2 = RoomsMenu(lrooms)
control2 = Controller(repo2)


# Buttons for Rooms menu
class rooms_menu_buttons:

    def __init__(self, rooms_menu, controller):
        self.rooms_menu = rooms_menu
        self.controller = controller

        self.frame = Frame(rooms_menu)
        self.frame.pack()
        self.label = Text(self.frame, height=15, width=30)
        # number, guests number, colour, price, sea_view
        self.number = Label(self.frame, text="Room number")
        self.number.grid(row=0, column=0, sticky=E)
        self.number_txt = Entry(self.frame)
        self.number_txt.grid(row=0, column=1, sticky=W)
        self.guests_no = Label(self.frame, text="Guests no.")
        self.guests_no.grid(row=1, column=0, sticky=E)
        self.guests_no_txt = Entry(self.frame)
        self.guests_no_txt.grid(row=1, column=1, sticky=W)
        self.colour = Label(self.frame, text="Colour")
        self.colour.grid(row=2, column=0, sticky=E)
        self.colour_txt = Entry(self.frame)
        self.colour_txt.grid(row=2, column=1, sticky=W)
        self.price = Label(self.frame, text="Price")
        self.price.grid(row=3, column=0, sticky=E)
        self.price_txt = Entry(self.frame)
        self.price_txt.grid(row=3, column=1, sticky=W)
        self.sea_view = Label(self.frame, text="Sea view")
        self.sea_view.grid(row=4, column=0, sticky=E)
        self.sea_view_txt = Entry(self.frame)
        self.sea_view_txt.grid(row=4, column=1, sticky=W)
        self.new_price = Label(self.frame, text="New price")
        self.new_price.grid(row=9, column=2, sticky=E)
        self.new_price_txt = Entry(self.frame)
        self.new_price_txt.grid(row=9, column=3, sticky=W)

        self.labelFrame = ttk.LabelFrame(self.frame, text="Open a file")
        self.labelFrame.grid(row=12, column=0)

        self.empty = Label(self.frame)
        self.empty.grid(row=6)
        self.btn0 = Button(self.frame, text="Exit rooms menu", command=rooms_menu.destroy)
        self.btn0.grid(row=7, column=1)
        self.btn1 = Button(self.frame, text="Add rooms", command=self.add_room)
        self.btn1.grid(row=8, column=1)
        self.btn2 = Button(self.frame, text="Modify price", command=self.change_price)
        self.btn2.grid(row=9, column=1)
        self.btn3 = Button(self.frame, text="Delete room", command=self.delete_room)
        self.btn3.grid(row=10, column=1)
        self.btn4 = Button(self.frame, text="Show rooms", command=self.show_rooms)
        self.btn4.grid(row=11, column=1)

        self.button = ttk.Button(self.labelFrame, text="Browse a file", command=self.fileDialog)
        self.button.grid(row=12, column=1)

    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetype=(("txt", "*.txt"), ("All Files", "*.*")))

    def clear(self):  # clear textboxes
        self.number_txt.delete(0, 'end')
        self.guests_no_txt.delete(0, 'end')
        self.colour_txt.delete(0, 'end')
        self.price_txt.delete(0, 'end')
        self.sea_view_txt.delete(0, 'end')
        self.new_price_txt.delete(0, 'end')

    def add_room(self):
        room = Room(self.number_txt.get(), self.guests_no_txt.get(), self.colour_txt.get(), self.price_txt.get(),
                    self.sea_view_txt.get())
        self.controller.add_room(room)
        self.clear()

    def change_price(self):
        self.controller.change_price(self.number_txt.get(), self.new_price_txt.get())
        self.clear()

    def delete_room(self):
        self.controller.delete_room(self.number_txt.get())
        self.clear()

    def show_rooms(self):
        l = self.controller.show_rooms()
        for i in range(len(l)):
            self.label.delete('1.0', END)
        for i in range(len(l)):
            #self.label = Text(self.frame, text=str(l[i]))
            self.label.grid(row=14, column=1)
            self.label.insert(END, str(l[i])+'\n')


'''
        root_rooms_menu = Tk()
        root_rooms_menu.title("Room list")
        root_rooms_menu.geometry('500x400')

        menu_rooms_menu = Menu(root_rooms_menu)
        root_rooms_menu.config(menu=menu_rooms_menu)
        submenu_rooms_menu = Menu(menu_rooms_menu)
        menu_rooms_menu.add_cascade(label="File", menu=submenu_rooms_menu)
        submenu_rooms_menu.add_command(label="Help", command=help)
        submenu_rooms_menu.add_command(label="Exit rooms menu", command=root_rooms_menu.destroy)

        # label = Label(root_rooms_menu, text=str(self.controller.show_rooms()))
        # label.pack()
        for item in self.controller.show_rooms():
            self.label = Label(root_rooms_menu, text=str(item))
            self.label.pack()
        root_rooms_menu.mainloop()
'''


# =======================================================================================================================

repo3 = Hotel(lguests, lrooms, lreservations)
control3 = Controller(repo3)


# Buttons for Hotel menu
class hotel_menu_buttons:

    def __init__(self, hotel_menu, controller):
        self.hotel_menu = hotel_menu
        self.controller = controller

        self.frame = Frame(hotel_menu)
        self.frame.pack()

        self.label = Text(self.frame)

        self.room = Label(self.frame, text="Room")
        self.room.grid(row=0, column=0, sticky=E)
        self.room_txt = Entry(self.frame)
        self.room_txt.grid(row=0, column=1, sticky=W)
        self.guests = Label(self.frame, text="Guests")
        self.guests.grid(row=1, column=0, sticky=E)
        self.guests_txt = Entry(self.frame)
        self.guests_txt.grid(row=1, column=1, sticky=W)
        self.check_in = Label(self.frame, text="Check_in")
        self.check_in.grid(row=2, column=0, sticky=E)
        self.check_in_txt = Entry(self.frame)
        self.check_in_txt.grid(row=2, column=1, sticky=W)
        self.check_out = Label(self.frame, text="Check_out")
        self.check_out.grid(row=3, column=0, sticky=E)
        self.check_out_txt = Entry(self.frame)
        self.check_out_txt.grid(row=3, column=1, sticky=W)

        self.price = Label(self.frame, text="Price")
        self.price.grid(row=11, column=0, sticky=E)
        self.price_txt = Entry(self.frame)
        self.price_txt.grid(row=11, column=1, sticky=W)
        self.sea_view = Label(self.frame, text="Sea view")
        self.sea_view.grid(row=12, column=0, sticky=E)
        self.sea_view_txt = Entry(self.frame)
        self.sea_view_txt.grid(row=12, column=1, sticky=W)

        self.btn0 = Button(self.frame, text="Exit hotel menu", command=hotel_menu.destroy)
        self.btn0.grid(row=5, column=1)

        self.btn1 = Button(self.frame, text="Make reservation", command=self.make_reservation)
        self.btn1.grid(row=6, column=1)

        #self.empty = Label(self.frame)
        #self.empty.grid(row=7)

        self.btn2 = Button(self.frame, text="Show guests with current reservations", command=self.current_reservations)
        self.btn2.grid(row=8, column=1)

        #self.empty1 = Label(self.frame)
        #self.empty1.grid(row=9)

        self.btn3 = Button(self.frame, text="Filter rooms by price and sea view", command=self.filter_rooms)
        self.btn3.grid(row=10, column=1)

        #self.empty2 = Label(self.frame)
        #self.empty2.grid(row=12)

        self.btn4 = Button(self.frame, text="Show rooms that are available today", command=self.available_rooms)
        self.btn4.grid(row=13, column=1)

        self.empty3 = Label(self.frame)
        self.empty3.grid(row=14)

    def show(self, l):
        for i in range(len(l)):
            self.label.delete('1.0', END)
        for i in range(len(l)):
            # self.label = Label(self.frame, text=str(l[i]))
            self.label.grid(row=15, column=1)
            self.label.insert(END, str(l[i]) + "\n")

    def make_reservation(self):
        room = self.controller.find_room(self.room_txt.get())
        check_in = date(int(self.check_in_txt.get().split("/")[2]), int(self.check_in_txt.get().split("/")[1]),
                        int(self.check_in_txt.get().split("/")[0]))
        check_out = date(int(self.check_out_txt.get().split("/")[2]), int(self.check_out_txt.get().split("/")[1]),
                         int(self.check_out_txt.get().split("/")[0]))
        if self.controller.make_reservation(self.guests_txt.get().split(", "), room, check_in, check_out) is False:
            self.label.delete('1.0', END)
            #self.label = Label(self.frame, text="This room is not available in this period!")
            self.label.grid(row=15, column=1)
            self.label.insert(END, "This room is not available in this period!")
        else:
            self.controller.make_reservation(self.guests_txt.get().split(", "), room, check_in, check_out)
        # clear textboxes
        self.room_txt.delete(0, 'end')
        self.guests_txt.delete(0, 'end')
        self.check_in_txt.delete(0, 'end')
        self.check_out_txt.delete(0, 'end')

    def current_reservations(self):
        l = self.controller.current_reservations()
        if not l:
            self.label.delete('1.0', END)
            #self.label = Label(self.frame, text="There are no guests with current reservations")
            self.label.grid(row=15, column=1)
            self.label.insert(END, "There are no guests with current reservations")
        else:
            self.show(l)

    def filter_rooms(self):
        l = self.controller.filter_rooms(self.price_txt.get(), self.sea_view_txt.get())
        if not l:
            self.label.delete('1.0', END)
            #self.label = Label(self.frame, text="There are no such rooms")
            self.label.grid(row=15, column=1)
            self.label.insert(END, "There are no such rooms")
        else:
            self.show(l)

    def available_rooms(self):
        l = self.controller.available_rooms()
        if not l:
            self.label.delete('1.0', END)
            #self.label = Label(self.frame, text="There are no rooms available today!")
            self.label.grid(row=15, column=1)
            self.label.insert(END, "There are no rooms available today!")
        else:
            self.show(l)


# =======================================================================================================================


# Buttons for main
class main_buttons:

    def __init__(self, main_menu):
        frame = Frame(main_menu)
        frame.pack()

        self.btn0 = Button(frame, text="Exit app", command=main_menu.destroy)
        self.btn0.pack()

        self.btn1 = Button(frame, text="Guests menu", command=self.access_guests_menu)
        self.btn1.pack()

        self.btn2 = Button(frame, text="Rooms menu", command=self.access_rooms_menu)
        self.btn2.pack()

        self.btn3 = Button(frame, text="Hotel menu", command=self.access_hotel_menu)
        self.btn3.pack()

    def access_guests_menu(self):
        root_guests_menu = Tk()
        root_guests_menu.title("Guests menu")
        root_guests_menu.geometry('500x350')

        menu_guests_menu = Menu(root_guests_menu)
        root_guests_menu.config(menu=menu_guests_menu)
        submenu_guests_menu = Menu(menu_guests_menu)
        menu_guests_menu.add_cascade(label="File", menu=submenu_guests_menu)
        submenu_guests_menu.add_command(label="Help", command=help)
        submenu_guests_menu.add_command(label="Exit guests menu", command=root_guests_menu.destroy)

        guests_menu_buttons(root_guests_menu, control1)
        root_guests_menu.mainloop()

    def access_rooms_menu(self):
        root_rooms_menu = Tk()
        root_rooms_menu.title("Rooms menu")
        root_rooms_menu.geometry('500x400')

        menu_rooms_menu = Menu(root_rooms_menu)
        root_rooms_menu.config(menu=menu_rooms_menu)
        submenu_rooms_menu = Menu(menu_rooms_menu)
        menu_rooms_menu.add_cascade(label="File", menu=submenu_rooms_menu)
        submenu_rooms_menu.add_command(label="Help", command=help)
        submenu_rooms_menu.add_command(label="Exit rooms menu", command=root_rooms_menu.destroy)

        rooms_menu_buttons(root_rooms_menu, control2)
        root_rooms_menu.mainloop()

    def access_hotel_menu(self):
        root_hotel_menu = Tk()
        root_hotel_menu.title("Hotel menu")
        root_hotel_menu.geometry('500x300')

        menu_hotel_menu = Menu(root_hotel_menu)
        root_hotel_menu.config(menu=menu_hotel_menu)
        submenu_hotel_menu = Menu(menu_hotel_menu)
        menu_hotel_menu.add_cascade(label="File", menu=submenu_hotel_menu)
        submenu_hotel_menu.add_command(label="Help", command=help)
        submenu_hotel_menu.add_command(label="Exit hotel menu", command=root_hotel_menu.destroy)

        hotel_menu_buttons(root_hotel_menu, control3)
        root_hotel_menu.mainloop()
