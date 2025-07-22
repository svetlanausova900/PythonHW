class Address:
    def __init__(self, index, city, street, house_number, flat_number):
        self.index = index
        self.city = city
        self.street = street
        self.house_number = house_number
        self.flat_number = flat_number


    def __str__(self):
        return f"Индекс {self.index}, город {self.city}, {self.street} улица, номер дома {self.house_number}, квартира {self.flat_number}"