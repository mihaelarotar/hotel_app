from datetime import date

class Controller:
    def __init__(self, repo):
        self.__repo = repo


    def add_guest(self, aguest):
        self.__repo.add_guest(aguest)

    def change_name(self, aguest, new_name):
        self.__repo.change_name(aguest, new_name)

    def delete_guest(self, aguest):
        self.__repo.delete_guest(aguest)

    def show_guests(self):
        return self.__repo.guest_list

    def find_guest(self, fname, lname):
        for guest in self.__repo.guest_list:
            if guest.first_name == fname and guest.last_name == lname:
                return guest
        return "This guest does not exist"


    def add_room(self, aroom):
        self.__repo.add_room(aroom)

    def change_price(self, aroomno, new_price):
        self.__repo.change_price(aroomno, new_price)

    def delete_room(self, aroom):
        self.__repo.delete_room(aroom)

    def show_rooms(self):
        return self.__repo.room_list

    def find_room(self, aroom):
        for room in self.__repo.room_list:
            if room.number == aroom:
                return room
        return "This room does not exist"


    def is_available(self, room, check_in, check_out):
        for reservation in self.__repo.reservation_list:
            if reservation.room == room:
                if reservation.check_in <= check_in < reservation.check_out or reservation.check_in < check_out <= reservation.check_out:
                    return False
        return True

    def make_reservation(self, guests, room, check_in, check_out):
        if self.is_available(room, check_in, check_out):
            self.__repo.make_reservation(guests, room, check_in, check_out)
        else:
            return False

    def current_reservations(self):
        today = date.today()
        ok = []
        # g = GuestsMenu(self.guest_list)
        for reservation in self.__repo.reservation_list:
            if reservation.check_out >= today:
                # print(reservation.guests)
                for guest in reservation.guests:
                    ok.append(self.find_guest(guest.split()[0], guest.split()[1]))
        return ok

    def filter_rooms(self, price, sea_view):
        ok = []
        for room in self.__repo.room_list:
            if room.price <= price and room.sea_view == sea_view:
                ok.append(room)
        return ok

    def available_rooms(self):
        today = date.today()
        ok = []
        for room in self.__repo.room_list:
            if room.availability:
                ok.append(room)
        for reservation in self.__repo.reservation_list:
            if today < reservation.check_in or today > reservation.check_out:
                ok.append(reservation.room)
        return ok
