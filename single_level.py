class Phone:
    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")

class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 13).buy()

