import pandas as pd
df = pd.read_csv("./data/hotels.csv")


class Hotel:
    def __init__(self, id: int):
        pass

    def book(self):
        pass

    def available(self):
        pass


class ReservationConfirmation:
    def __init__(self, customer_name: str, hotel_object: int):
        pass

    def generate(self):
        pass


# Creating a skeleton command line main program.
print(df)
id = input("Enter the id of the hotel you wish to book: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationConfirmation(name, hotel)
    print(reservation_ticket.generate())
else:
    print("That hotel is not available right now.")
