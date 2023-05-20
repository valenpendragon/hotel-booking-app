import pandas as pd

df = pd.read_csv("./data/hotels.csv", dtype={"id": str})


class Hotel:
    def __init__(self, hotel_id: int):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Books a hotel by changing its availability to no."""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("./data/hotels.csv", index=False)

    def available(self):
        """Checks if the hotel is available."""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        return availability == "yes"


class ReservationConfirmation:
    def __init__(self, customer_name: str, hotel_object: Hotel):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
        """
        return content


# Creating a skeleton command line main program.
print(df)
hotel_ID = input("Enter the id of the hotel you wish to book: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationConfirmation(customer_name=name,
                                                 hotel_object=hotel)
    print(reservation_ticket.generate())
else:
    print("That hotel is not available right now.")
