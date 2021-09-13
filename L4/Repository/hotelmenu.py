from L4.Entities.reservation import Reservation
from datetime import date
from L4.Entities.guest import Guest
from L4.Repository.guestsmenu import GuestsMenu


class Hotel:
    # Constructor
    def __init__(self, guest_list, room_list, reservation_list):
        self.guest_list = guest_list
        self.room_list = room_list
        self.reservation_list = reservation_list

    def find_guest(self, fname, lname):
        for guest in self.guest_list:
            if guest.first_name == fname and guest.last_name == lname:
                return guest
        return "This guest does not exist"

    # Option 1: Make a reservation
    def make_reservation(self, guests, room, check_in, check_out):
        # verific daca camera este disponibila in perioada data
        '''for reservation in self.reservation_list:
            if reservation.room == room:
                if reservation.check_in <= check_in < reservation.check_out or reservation.check_in < check_out <= reservation.check_out:
                    print("This room is not available in this period!")
                    return'''
        reservation = Reservation(guests, room, check_in, check_out)  # creez rezervarea
        self.reservation_list.append(reservation)  # adaug rezervarea in lista de rezervari
        # adaug rezervarea creata in lista de rezervari a clientilor
        for aguest in guests:
            if self.find_guest(aguest.split()[0], aguest.split()[1]) not in self.guest_list:
                self.guest_list.append(aguest)
            self.find_guest(aguest.split()[0], aguest.split()[1]).reservations.append(reservation)
        room.availability = False  # marchez camera drept rezervata
        #print("The reservation was made!")


    '''# Option 2: Show guests with current reservations
    def current_reservations(self):
        today = date.today()
        ok = []
        #g = GuestsMenu(self.guest_list)
        for reservation in self.reservation_list:
            if reservation.check_out >= today:
                #print(reservation.guests)
                for guest in reservation.guests:
                    ok.append(self.find_guest(guest.split()[0], guest.split()[1]))
        return ok
        #if ok == 0:
         #   print("There are no guests with current reservations")

    # Option 3: Filter rooms by price and sea view
    def filter_rooms(self, price, sea_view):
        ok = []
        for room in self.room_list:
            if room.price <= price and room.sea_view == sea_view:
                ok.append(room)
        return ok
                #ok = 1
        #if ok == 0:
         #   print("There are no such rooms!")

    # Option 4: Show rooms that are available today
    def available_rooms(self):
        today = date.today()
        ok = []
        for room in self.room_list:
            if room.availability == 1:
                ok.append(room)
        for reservation in self.reservation_list:
            if today < reservation.check_in or today > reservation.check_out:
                ok.append(reservation.room)
        return ok
        #if ok == 0:
         #   print("There are no rooms available today!")

    def delete_reservation(self, aroom):
        for reseravtion in self.reservation_list:
            if reseravtion.room.number == aroom:  # parametrul aroom reprezinta numarul camerei
                self.reservation_list.remove(reseravtion)'''