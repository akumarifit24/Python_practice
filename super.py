## Example 1 #######
# class Phone:
#     def __init__(self, price, brand, camera):
#         print("inside phone constructure")
#         self.price = price
#         self.__brand = brand
#         self.camera = camera

#     def buy(self):
#         print("Buying a Phone")

# class SmartPhone(Phone):
#     def buy(self):
#         print("Buying a Smartphone")
#         super().buy()

# s = SmartPhone(20000, "Apple", 13)

# s.buy()


##### Example 2 ############

class Phone:
    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera


class SmartPhone(Phone):

    def __init__(self, price, brand, camera, os, ram):
        print("First inside this")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside Smartphone Constructor")

s = SmartPhone(20000, "Apple", 13, "Android", 2)

print(s.os)
print(s.brand)

