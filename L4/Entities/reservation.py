class Reservation:
    # Constructor
    def __init__(self, guests, room, check_in, check_out):
        self.__guests = guests
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out
        if self.__check_in >= self.__check_out:
            raise ValueError("The check-out date must be after the check-in date!")

    # getters
    @property
    def guests(self): return self.__guests

    @property
    def room(self): return self.__room

    @property
    def check_in(self): return self.__check_in

    @property
    def check_out(self): return self.__check_out

    # setters
    @guests.setter
    def guests(self, guests):
        self.__guests = guests

    @room.setter
    def room(self, room):
        self.__room = room

    @check_in.setter
    def check_in(self, check_in):
        self.__check_in = check_in

    @check_out.setter
    def check_out(self, check_out):
        self.__check_out = check_out

    # Representation
    def __str__(self):
        return "{}, {}, {}, {}".format(self.__guests, self.__room, self.__check_in, self.__check_out)

    def __repr__(self):
        return "List of guests: %s, %s, Period: %s - %s" % (self.__guests, self.__room, self.__check_in, self.__check_out)
