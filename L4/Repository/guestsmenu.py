from L4.Entities.guest import Guest
from datetime import date
from L4.Entities.reservation import Reservation


class GuestsMenu:
    # Constructor
    def __init__(self, guest_list, file="guests.txt"):
        self.__guest_list = guest_list
        self.__fName = file
        self.__loadFromFile()

    @property
    def guest_list(self):
        return self.__guest_list

    # Option 1: Add guest
    def add_guest(self, aguest):
        for guest in self.__guest_list:
            if guest.first_name == aguest.first_name and guest.last_name == aguest.last_name:
                raise ValueError("There is already a guest with this name!")
        self.__guest_list.append(aguest)
        self.__storeToFile()

    # Option 2: Modify last name
    def change_name(self, aguest, new_name):
        ok = 0
        for guest in self.__guest_list:
            if guest.first_name == aguest.first_name and guest.last_name == aguest.last_name:
                guest.last_name = new_name
                self.__storeToFile()
                ok = 1
        if ok == 0:
            raise ValueError("This guest does not exist!")

    # Option 3: Delete guest
    def delete_guest(self, aguest):
        ok = 0
        for guest in self.__guest_list:
            if guest.first_name == aguest.first_name and guest.last_name == aguest.last_name:
                self.__guest_list.remove(guest)
                self.__storeToFile()
                ok = 1
        if ok == 0:
            raise ValueError("This guest does not exist!")

    '''def find_guest(self, fname, lname):
        for guest in self.__guest_list:
            if guest.first_name == fname and guest.last_name == lname:
                return guest
        return "This guest does not exist"'''

    def __storeToFile(self):
        f = open(self.__fName, 'w')

        for el in self.__guest_list:
            f.write(str(el) + '\n')

        f.close()

    def __loadFromFile(self):
        f = open(self.__fName, 'r')

        for line in f:
            data = line.strip().split(": ")
            res = []
            name = data[0]
            res_list = data[1]
            if res_list != "[]":
                for elem in res_list.split('/'):
                    res.append(Reservation(elem.split(', ')[0], elem.split(', ')[1], date(elem.split(', ')[2]),
                     date(elem.split(', ')[3])))
                guest = Guest(name.split()[0], name.split()[1], res)
            else:
                guest = Guest(name.split()[0], name.split()[1], res)
            self.__guest_list.append(guest)

        f.close()
