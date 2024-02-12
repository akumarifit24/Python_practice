##### Polymorphism ######

# Method Overriding
class Phone:
    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):
    def buy(self):
        print("Buying a Smartphone")


s = SmartPhone(20000, "Apple", 13)

s.buy()


# Method Overloading

class Geometry:
    def area(self, a, b = 0):
        if(b == 0):
            print("circle ", 3.14*a*a)
        else:
            print("Rect ", a*b)

obj = Geometry()
obj.area(4)
obj.area(4,5)