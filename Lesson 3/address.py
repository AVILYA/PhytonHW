class Address:
    def __init__(self, index, city, street, house, apartment=None):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment

    def __str__(self):
        apartment_part = f", кв. {self.apartment}" if self.apartment else ""
        return f"{self.index}, {self.city}, {self.street}, д. {self.house}{apartment_part}"