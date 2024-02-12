##### Inheriting Private member ######
#private members can't be accessed in inheritence

class Phone:
    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera


class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 13)

print(s.__brand)