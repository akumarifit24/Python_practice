# class Customer:

#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# def greet(customer):
#     if customer.gender == "Male":
#         print("Hello", customer.name, "sir")
#     else:
#         print("Hello", customer.name, "ma'am")

#     cust2 = Customer("Nitish", "Male")
#     return cust2

# cust = Customer("Anjali", "Female")

# new_cust = greet(cust)
# print(new_cust.name)


class Customer:

    def __init__(self, name):
        self.name = name

def greet(customer):
    print(id(customer))
    customer.name = "Nitish"
    print(customer.name)
    print(id(customer.name))
     

cust = Customer("Anjali")
print(id(cust))

greet(cust)
print(cust.name)

#class objects are also mutable like lists, dict and sets

