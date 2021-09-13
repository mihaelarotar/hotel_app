class Guest:
    # Constructor
    def __init__(self, first_name, last_name, reservations=[]):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__reservations = reservations

    # getters
    @property
    def first_name(self): return self.__first_name

    @property
    def last_name(self): return self.__last_name

    @property
    def reservations(self): return self.__reservations

    # setters
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @reservations.setter
    def reservations(self, reservations):
        self.__reservations = reservations

    # Representation
    def __str__(self):
        if not self.__reservations:
            return "{} {}: {}".format(self.__first_name, self.__last_name, self.__reservations)
        else:
            return "{} {}: {}".format(self.__first_name, self.__last_name,
                                     '/'.join(str(reservation) for reservation in self.__reservations))

    def __repr__(self):
        return "Guest name: %s %s, reservations: %s" % (self.__first_name, self.__last_name, self.__reservations)
