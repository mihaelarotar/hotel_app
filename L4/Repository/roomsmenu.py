from L4.Entities.room import Room


class RoomsMenu:
    # Constructor
    def __init__(self, room_list, file="rooms.txt"):
        self.__room_list = room_list
        self.__fName = file
        self.__loadFromFile()

    @property
    def room_list(self):
        return self.__room_list

    # Option 1: Add room
    def add_room(self, aroom):
        for room in self.__room_list:
            if room.number == aroom.number:
                raise ValueError("There is already a room with this number!")
        self.__room_list.append(aroom)
        self.__storeToFile()

    # Option 2: Modify price
    def change_price(self, aroomno, new_price):
        ok = 0
        for room in self.__room_list:
            if room.number == aroomno:  # parametrul aroomno reprezinta numarul unei camere
                room.price = new_price
                self.__storeToFile()
                ok = 1
        if ok == 0:
            raise ValueError("This room does not exist!")

    # Option 3: Delete room
    def delete_room(self, aroom):
        ok = 0
        for room in self.__room_list:
            if room.number == aroom:  # parametrul aroom reprezinta numarul camerei
                self.__room_list.remove(room)
                self.__storeToFile()
                ok = 1
        if ok == 0:
            raise ValueError("This room does not exist!")

    '''def find_room(self, aroom):  # functia afiseaza camera (si toate caracteristicile ei) cu numarul aroom
        for room in self.__room_list:
            if room.number == aroom:
                return room
        return "This room does not exist"'''

    def __storeToFile(self):
        f = open(self.__fName, 'w')

        for el in self.__room_list:
            f.write(str(el) + '\n')

        f.close()

    def __loadFromFile(self):
        f = open(self.__fName, 'r')

        for line in f:
            data = line.strip().split("; ")
            room = Room(data[0], data[1], data[2], data[3], data[4])
            self.__room_list.append(room)

        f.close()
