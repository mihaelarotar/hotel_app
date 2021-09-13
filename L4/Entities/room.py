class Room:
    # Constructor
    def __init__(self, number, guests_number, colour, price, sea_view):
        self.__number = number
        self.__guests_number = guests_number
        self.__colour = colour
        self.__price = price
        self.__sea_view = sea_view
        if self.__sea_view not in ["yes", "no"]:
            raise ValueError("Enter yes or no")
        self.__availability = True

    # getters
    @property
    def number(self): return self.__number

    @property
    def guests_number(self): return self.__guests_number

    @property
    def price(self): return self.__price

    @property
    def colour(self): return self.__colour

    @property
    def sea_view(self): return self.__sea_view

    @property
    def availability(self): return self.__availability

    # setters
    @number.setter
    def number(self, number):
        self.__number = number

    @guests_number.setter
    def guests_number(self, guests_number):
        self.__guests_number = guests_number

    @price.setter
    def price(self, price):
        self.__price = price

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    @sea_view.setter
    def sea_view(self, sea_view):
        self.__sea_view = sea_view

    @availability.setter
    def availability(self, availability):
        self.__availability = availability

    # Representation
    def __str__(self):
        return f"{self.__number}; {self.__guests_number}; {self.__colour}; {self.__price}; {self.__sea_view}"

    def __repr__(self):
        return "Room: %s, Guests no:%s ,Colour: %s, Price: %s, Sea view: %s" \
               % (self.__number, self.__guests_number, self.__colour, self.__price, self.__sea_view)
