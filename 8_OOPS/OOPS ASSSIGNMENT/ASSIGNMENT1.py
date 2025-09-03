# Problem 1: Library Book Management
# SOURCE CODE

class BOOK:
    Total_books=0
    def __init__(self,title,author,price):
        self.Title=title
        self.Author=author
        self.Price=price
        BOOK.Total_books+=1
    def Display_book(self):
        print(f"Title : {self.Title}, Author : {self.Author}, Price : {self.Price}")
    @classmethod
    def Show_Total_Books(cls):
        print("Total Books : ",cls.Total_books)
b1=BOOK("Rich Dad Poor Dad", "Robert Kiyosaki", 450)
b1.Display_book()
BOOK.Show_Total_Books()

b2 = BOOK("Atomic Habits", "James Clear", 550)
b2.Display_book()
BOOK.Show_Total_Books()


# Problem 2: Bank Account System

# Source code
class BankAccount:
    Ifsc_code="SBIN0001234"

    def __init__(self,Account_number,holder_name,balance):
        self.Account_Number=Account_number
        self.Holder_Name=holder_name
        self.Balance=balance
    def deposit(self,amount):
        print("Deposited : ",amount)
        self.Balance+=amount
    def withdraw(self,amount):
        if(amount>self.Balance):
            print("Insufficient Balance")
        else:
            print("Withdrawn : ",amount)
        self.Balance-=amount
    def Display_balance(self):
        print("Balance : ",self.Balance)
Acc1=BankAccount("12345", "Anand", 1000)
Acc1.deposit(500)
Acc1.withdraw(200)
Acc1.withdraw(2000)