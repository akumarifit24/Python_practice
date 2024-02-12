class Atm:
    #Constructer:- it is a method which get executed autometically after running the code
    #instance variable:- the value of variables is different for different objects
    #encapsulation:- hiding internal implementation of class from outside code

    #static/class
    __counter = 1

    def __init__(self): #constructer
        # double underscore is used to make variables hide from outside the class means it can only be used inside the class
        self.__pin = ""  #instance variable
        self.__balance = 0  #instance variable
        self.sno = Atm.__counter
        Atm.__counter = Atm.__counter + 1

        print(id(self))
        #self.menu()

    @staticmethod
    def get_counter():
        return Atm.__counter
    
    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("Not Allowed")

    def get_pin(self):
        return self.__pin

    def set_pin(self, new_pin):
        if type(new_pin) == str:
            self.__pin = new_pin
            print('Pin Set Successfully')
        else:
            print("Not Allowed")


    def menu(self):
        user_input = input("""
                    Hello, how would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit
                           3. Enter 3 to withdraw
                           4. Enter 4 to chack balance
                           5. Enter 5 to exit
    """)
        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.deposit()
        elif user_input == '3':
            self.withdraw()
        elif user_input == '4':
            self.check_balance()
        else:
            print('bye')

    def create_pin(self):
        self.__pin = input("Enter your pin")
        print('Pin Set Successfully')
    
    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the Amount"))
            self.__balance += amount
            print("Deposite Successfully")
        else:
            print("Invalid Pin")

    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            amount = int(input("Enter the amount"))
            if amount < self.__balance:
                self.__balance -= amount
                print("withdrawl successful")
            else:
                print("insufficient funds")
        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("invalid pin")
