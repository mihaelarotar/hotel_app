from L4.Entities import Guest
from L4.Repository.guestsmenu import GuestsMenu
from L4.Entities import Room
from L4.Repository.roomsmenu import RoomsMenu
from L4.Repository.hotelmenu import Hotel
from datetime import date

lguests = [Guest("Vasile", "Vasilescu"), Guest("Ana", "Pop"), Guest("Maria", "Popescu"), Guest("Ion", "Ionescu"), Guest("George", "Georgescu")]
lrooms = [Room(1, 2, 100, "red", "yes"), Room(2, 1, 150, "blue", "yes"), Room(3, 3, 180, "green", "no"), Room(4, 2, 120, "pink", "no"), Room(5, 1, 75, "white", "yes")]
lreservations = []
#guest1 = Guest("a", "b")
#lg = GuestsMenu(lguests)
#lg.add_guest(guest1)


def guests_menu():
    return """
0 - Go back
1 - Add guest
2 - Modify last name
3 - Delete guest
4 - Show guests
    """


def console1():
    g = GuestsMenu(lguests)
    while True:
        print(guests_menu())
        opt = int(input('Option-'))

        if opt == 0:
            print('Going back')
            break

        elif opt == 1:
            prenume = input('First name: ')
            nume = input('Last name: ')
            if nume.isalpha() == False or prenume.isalpha() == False:
                raise NameError("Name should not contain numbers")
            try:
                guest = Guest(prenume, nume)
                # guest.reservations.append(Reservation())
                g.add_guest(guest)
            except NameError:
                print("Impossible name")

        elif opt == 2:
            # prenume = input('First name: ')
            # nume = input('Last name: ')
            guest = input("Pick a guest (full name): ")
            newname = input('New last name: ')
            g.change_name(guest, newname)

        elif opt == 3:
            prenume = input('First name: ')
            nume = input('Last name: ')
            #guest = input("Pick a guest (full name): ")
            guest = Guest(prenume, nume)
            g.delete_guest(guest)

        elif opt == 4:
            g.print_guest_list()

        else:
            print('This option does not exist!')

        input("\n Press enter to continue")


def rooms_menu():
    return """
0 - Go back   
1 - Add room
2 - Modify price
3 - Delete room
4 - Show rooms
    """


def console2():
    r = RoomsMenu(lrooms)
    h = Hotel(lguests, lrooms, lreservations)
    while True:
        print(rooms_menu())
        opt = int(input('Option-'))

        if opt == 0:
            print('Going back')
            break

        elif opt == 1:
            number = int(input("Room number: "))
            guests_number = int(input("Guests number: "))
            price = int(input("Room price: "))
            colour = input("Room colour: ")
            sea_view = input("Room sea view: ")
            # availability = input("Room available: ")
            room = Room(number, guests_number, price, colour, sea_view)
            r.add_room(room)

        elif opt == 2:
            room = int(input("Room number: "))
            newprice = int(input('New price: '))
            r.change_price(room, newprice)

        elif opt == 3:
            room = int(input("Room number: "))
            r.delete_room(room)
            h.delete_reservation(room)

        elif opt == 4:
            r.print_room_list()

        else:
            print('This option does not exist!')

        input("\n Press enter to continue")


def hotel_menu():
    return """
0 - Go back   
1 - Make reservation
2 - Show guests with current reservations
3 - Filter rooms by price and sea view
4 - Show rooms that are available today
    """


def console3():
    h = Hotel(lguests, lrooms, lreservations)
    while True:
        print(hotel_menu())
        opt = int(input('Option-'))

        if opt == 0:
            print('Going back')
            break

        elif opt == 1:
            aroom = int(input("Introduce room number: "))
            r = RoomsMenu(lrooms)
            room = r.find_room(aroom)
            if room not in lrooms:
                raise ValueError("This room does not exist!")
            guests = []
            guestsnumber = room.guests_number
            #guestsnumber = int(input("Number of guests : "))
            while guestsnumber > 0:
                guest = input("Full name of guest: ")
                guests.append(guest)
                guestsnumber -= 1
            print("Check-in date")
            check_in = date(int(input("year=")), int(input("month=")), int(input("day=")))
            print("Check-out date")
            check_out = date(int(input("year=")), int(input("month=")), int(input("day=")))
            h.make_reservation(guests, room, check_in, check_out)

        elif opt == 2:
            h.current_reservations()

        elif opt == 3:
            price = int(input("Show rooms cheaper than: "))
            sea_view = input("Answer with yes or no. Do you want a room with a sea view? ")
            h.filter_rooms(price, sea_view)

        elif opt == 4:
            h.available_rooms()

        else:
            print('This option does not exist!')

        input("\n Press enter to continue")
