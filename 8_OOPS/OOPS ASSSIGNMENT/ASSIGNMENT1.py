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

#Problem 3: Student Grade Calculator

class Student:
    Total_students=0
    def __init__(self,name,marks):
        self.Name=name
        self.Marks=marks
        Student.Total_students+=1
    def Caluculate_Average(self):
        Total_marks=0
        for i in self.Marks:
            Total_marks+=i
        Average=Total_marks/len(self.Marks)
        print(round(Average,2))
    def Get_Grade(self):
        Total_marks=0
        for i in self.Marks:
            Total_marks+=i
        Average=Total_marks/len(self.Marks)
        if(Average<=35):
            print("F")
        elif(Average>=60 and Average<70):
            print("C")
        elif(Average >=70 and Average<80):
            print("C+")
        elif(Average>=80 and Average<90):
            print("B")
        elif(Average>=90 and Average<100):
            print("A")
    @classmethod
    def Students(self):
        print(self.Total_students)
s1=Student("Naveen",[80,70,90])
s1.Caluculate_Average()
s1.Get_Grade()
s2=Student("Meena",[95,92,90])
s2.Caluculate_Average()
s2.Get_Grade()
s3=Student("Arun",[30,35,40])
s3.Caluculate_Average()
s3.Get_Grade()
Student.Students()

# Problem 4: Employee Salary Management

class Employee:

    Company_name="Infosys"

    def __init__(self,emp_id,emp_name,Basic_salary):
        self.Emp_Id=emp_id
        self.Emp_Name=emp_name
        self.Basic_Salary=Basic_salary
    def Set_salary(self,salary):
        self.Basic_Salary=salary
    def Get_Salary(self):
        print(self.Basic_Salary)
    def Calculate_Net_Salary(self):
        basic=self.Basic_Salary * 0.5
        pf=basic * 12/100
        pt=200
        tds=1500
        other=300
        deduction=pf+pt+tds+other
        net_salary=self.Basic_Salary-deduction
        return net_salary
e1=Employee(101,"Naveen",50000)
e1.Set_salary(60000)
print(e1.Calculate_Net_Salary())
e1.Get_Salary()
e2 = Employee(102, "Ravi", 40000)
print(e2.Calculate_Net_Salary())
print(e1.Calculate_Net_Salary())

# Problem 5: Shopping Cart

class Product:
    Total_bill=0
    def __init__(self,name,price,quantity):
        self.Name=name
        self.Price=price
        self.Quantity=quantity
    def Calculate_bill(self):
        calculate=self.Price * self.Quantity
        Product.Total_bill+=calculate
        calculate
p1=Product("Laptop",40000,1)
p1.Calculate_bill()
p2=Product("Mouse",500,2)
p2.Calculate_bill()
p3=Product("Keyboard",1500,1)
p3.Calculate_bill()
print(Product.Total_bill)



# additional

class Room:
    total=20
    def __init__(self,a,b,c,d):
        self.Room_no=a
        self.Type=b
        self.Ac_Or_Non_Ac=c
        self.Avilable=d
    def Check_out(self):
        Room.total+=1
        self.Avilable=True
        
    def Check_in(self):
        Room.total-=1
        if(self.Avilable):
            self.Avilable=False
            print("room avilabe take it")
        else:
            print("Room not avilable")
def lines():
    print("---------------------")
room1=Room(1,"Single","AC",True)
room2=Room(2,"King","AC",True)
room3=Room(3,"Single","AC",True)
room4=Room(4,"queen","AC",True)
room5=Room(5,"king","AC",True)
room6=Room(6,"Single","AC",True)
room7=Room(7,"Single","AC",True)
room8=Room(8,"king","AC",True)
room9=Room(9,"Single","non-AC",True)
room10=Room(10,"Single","non-AC",True)
room11=Room(11,"king","non-AC",True)
room12=Room(12,"Single","non-AC",True)
room13=Room(13,"Single","non-AC",True)
room14=Room(14,"queen","non-AC",True)
room15=Room(15,"Single","non-AC",True)
while True:
    print("1.Check Total Avilable rooms \n2.Check how Many Ac rooms avilable \n3.Check how may non Ac rooms avilable \n4.Check in \n5.Check out 0.exit\n")
    lines()
    user_intput=int(input(" Choose one :- "))
    lines()
    match(user_intput):
        case 1:
            print(Room.total ," Rooms avilable ")
            lines()
        case 4:
            room_no=input("Enter the room no : Ex: room1 to room 20 :- ")
            room=room_no
        case 0:
            print("Bye")
            break
