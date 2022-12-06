"""class Student:
    def subject(self):
        maths = int(input("Enter the marks obtained in Maths = "))
        science = int(input("Enter the marks obtained in Science = "))
        english = int(input("Enter the marks obtained in English = "))
        total = maths + science + english
        print(f"The total marks obtained is {total}")


sub = Student()
sub.subject()


class Details:
    def __init__(self, l, b, h):
        self.l,self.b,self.h = l,b,h

    def area(self):
        area = self.l * self.b
        print("The area of the rectangle is = ", area)

    def volume(self):
        volume = self.l * self.b * self.h
        print("The volume of the rectangle is = ", volume)


l = int(input("Enter the length = "))
b = int(input("Enter the breadth = "))
h = int(input("Enter the height = "))

obj = Details(l, b, h)
obj.area()
obj.volume()"""


class Details:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price


class Bill(Details):
    def cal(self):
        total = self.quantity * self.price
        print(f"The total bill of  {self.product} = {total}")


product = input("Enter the product name = ")
quantity = int(input("Enter quantity = "))
price = int(input("Enter the price = "))

bill = Bill(product, quantity, price)
bill.cal()
