class Product:
    def review(self):
        print("Product customer review")

class Phone(Product):
    def __init__(self, price, brand, camera):
        print("inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

class SmartPhone(Phone):
    pass


s = SmartPhone(20000, "Apple", 13)
p = Phone(1000, "sumsung", 1)
s.buy()
s.review()
p.review()


class A:
    def m1(self):
        return 20
    
class B(A):
    def m1(self):
        return 30
    def m2(self):
        return 40

class C(B):
    def m2(self):
        return 20
    

obj1 = A()
obj2 = B()
obj3 = C()

print(obj1.m1() + obj2.m1() + obj3.m2())


