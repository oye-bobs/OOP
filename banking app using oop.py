'''
Banking System using OOP





Allows withdraw, view_balance
'''
#Parent Class
class User(): #Holds details about a user
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):#shows user details
       print("Personal details")
       print("")
       print("Name :", self.name)
       print("Age :", self.age)
       print("Gender :", self.gender)
#Child Class
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance = 0 #Stores details about the account balance

    def deposit(self,amount):  #Allows for deposits, credit
        self.amount = amount
        self.balance = self.balance + amount
        print("Account has been credited : $",self.balance)
        
    def withdraw(self,amount): #Allows for withdrawals
        self.amount = amount
        if self.amount > self.balance:
            print("sorry, Insufficient Funds | Balance Available : $", self.balance)
        else: 
            self.balance = self.balance - self.amount
            print("Account has been debited : $",self.balance)

    def show_balance(self): #Allows for viewing account balance
        self.show_details()
        print( "Your account balance is : $",self.balance)
        
        
    
        


    
