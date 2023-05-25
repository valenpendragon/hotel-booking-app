import pandas as pd

df = pd.read_csv("./data/hotels.csv", dtype={"id": str})
credit_cards = pd.read_csv("./data/cards.csv", dtype=str).to_dict(
    orient="records")
df_card_security = pd.read_csv("./data/card_security.csv", dtype=str)


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


class SpaHotel(Hotel):
    def book_spa_package(self):
        """Books access to the spa at the hotel"""
        pass


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


class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[
            df_card_security["number"] == self.number, "password"].squeeze()
        return password == given_password


class SpaReservation:
    def __init__(self, customer_name: str, hotel_object: SpaHotel):
        self.customer_name = customer_name
        self.spa_hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your SPA reservation!
        Here is your SPA booking information:
        Name: {self.customer_name}
        Hotel Name: {self.spa_hotel.name}"""
        return content


# Creating a skeleton command line main program.
print(df)
hotel_ID = input("Enter the id of the hotel you wish to book: ")
hotel = SpaHotel(hotel_ID)
if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456",
                                   expiration="12/26",
                                   holder="John Smith",
                                   cvc="123")
    if credit_card.validate():
        password = input("Please enter your secure credit card password: ")
        if credit_card.authenticate(given_password=password):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationConfirmation(customer_name=name,
                                                         hotel_object=hotel)
            print(reservation_ticket.generate())
            choice = input("Would you like to book a spa package (Y/N)? ")
            if choice.lower()[0] == "y":
                spa_reservation = SpaReservation(customer_name=name,
                                                 hotel_object=hotel)
                print(spa_reservation.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment method.")
else:
    print("That hotel is not available right now.")
