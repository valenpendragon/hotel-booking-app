import pandas as pd

df = pd.read_csv("./data/hotels.csv", dtype={"id": str})
credit_cards = pd.read_csv("./data/cards.csv", dtype=str).to_dict(
    orient="records")


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


class CreditCard:
    def __init__(self, number:str,
                 expiration: str,
                 holder: str,
                 cvc: str):
        self.number = number
        self.expiration = expiration
        self.holder = holder.upper()
        self.cvc = cvc
        print(self)

    def __str__(self):
        output = f"""
            Credit Card Info:
            Number: {self.number}
            Expiration: {self.expiration}
            Holder: {self.holder}
            CVC: {self.cvc}
        """
        return output

    def validate(self):
        card_data = {"number": self.number,
                     "expiration": self.expiration,
                     "holder": self.holder,
                     "cvc": self.cvc}
        if card_data in credit_cards:
            return True
        else:
            return False


# Creating a skeleton command line main program.
print(df)
hotel_ID = input("Enter the id of the hotel you wish to book: ")
hotel = Hotel(hotel_ID)
if hotel.available():
    credit_card = CreditCard(number="1234567890123456",
                             expiration="12/26",
                             holder="John Smith",
                             cvc="123")
    if credit_card.validate():
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationConfirmation(customer_name=name,
                                                     hotel_object=hotel)
        print(reservation_ticket.generate())
    else:
        print("There was a problem with your payment method.")
else:
    print("That hotel is not available right now.")
