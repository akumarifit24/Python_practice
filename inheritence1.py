##### Inheriting Constructure ######
class Phone:
    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 13)

print(s.brand)