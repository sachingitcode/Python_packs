# class attributes vs object/instance attributes : we can add  instance variables to an object
# instance attributes takes preference over class attribute during get/retrival or set/
# dunder methods -: starting from __   eg __init__, __import__
# public starting from alphanum  ,, protected starting from _   ,, private starting from __


class Emp:
    lang = 'py'
    sal = 12.00


a = Emp()
a.n = 'Hooo'
print(a.n, a.sal, a.lang)  # name is instance variables to an object  where as sal,lang is class attribute


# self parameter
# it represent instance of class, in a class, first method of class is self, by that
# we can  access the attributes of class  and methods of the instance that is calling the method.
# , it is not a reserved keyword in Python. You could technically use a different name,
# I think it is used to store/retrive all elements in class
# But Note when we call the method, it is not provide as method parameter

class Dog:
    name = "Doggy"
    age = "10"

    def display(self):  # here if we romve self . it will not work, we need to provide 1 arg, wherther to use or not
        print(f"Dog is {self.name} so is {self.age}")

    @staticmethod  # compulsory
    def pie_method():  # this is the static method ,it doesnot req self /object element
        print("Hello")
        return 3.14


d = Dog()
d.display()  # display func taking 1 arg , but here,we are not providing

print(d.pie_method())


# static method: if our method doesnot required self means class object , then we can make that as static method

# __init__   dunder method  constructor


class Emp:
    lang = "py"
    sal = "12,00"

    def __init__(self):
        print("i am creating an object")

    def __init__(self, name, salary, language):
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")


# tn=Emp()                  # this will not work as init is overriden
n = Emp('sac', 1234, 'en')  # Note here init is overrided, below one is working
print(n.salary, n.name)


# 7:07:00

class C:
    a = 4

    def show(self):
        print("Values of a : ", self.a)


o = C()
print(o.a)  # 4
o.a = 8  # here instance variable is initilised ,
print(o.a)  # 8  # it shadows the class variable # but it does NOT change the class variable value
print(C.a)  # 4  # to print class variable value
o.show()  # 8  # this is interesting as  we are calling show, which is using self.a ,shill it shows 8


# we can use @classmethod to show class attribures, this works with methods


class Train:
    def __init__(self, name, status, fare):
        self.name = name
        self.status = status
        self.fare = fare

    def getStatus(self):
        print(self.status)

    def getFare(self):
        print(self.fare)


a = Train("A", "P", 500)
b = Train("B", "F", 300)
c = Train("C", "P", 400)

l = [a, b, c]


class A:
    a = 3

    def __init__(self):
        print("Constructor A ")


class B(A):
    b = 5

    def __init__(self):
        super().__init__()
        print("Constructor B ")


class C(B):
    c = 18

    def __init__(self):
        print("Constructor C ")

    def show(self):
        print(f"Value of a :{self.a}")


v = C()
v.show()

C.show(C())  # here only Constructor C  prints means only C is called

t = B()  # Constructor A Constructor B    : as super is calling parent init :so it showing 2 results

# it helps in accessing the super class / parent class method,keyword property

# WE use super() to called the parent cnstructor

print("******")


########################### Need to under stand more
class Emps:
    a = 4567

    @property
    def name(self):
        return self.fname

    @name.setter
    def name(self, value):
        self.fname = value + " yadav"


e = Emps()
e.name = "sachin"

print(e.name)

# Opeartor overloading :
#
print(4 + 5)
print('4' + '5')
print(4 + 5.0)
print(4 + True)  # 5
print(4 + True + True)  # 6
print(4 + True + True + False)  # 6   true -> 1 ,false =0


class operator_overloading:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

    def __len__(self):
        for i in range(6):
            print("", self.a)


class vector_2d:
    l = [{1, 2}, {3, 4}, {5, 6}, [7, 8]]

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print("Vector ", self.i, self.j)


class vector_3d(
    vector_2d):  # inheritance, calling parent class , inharitance means , us class k sare methods,params,variables aa jayege
    def __init__(self, i, j, k):
        super().__init__(i, j)  # calling parent constructor
        self.k = k

    def show(self):
        print("Vector ", self.i, self.j, self.k)


a = vector_2d(1, 2)
b = vector_3d(3, 4, 5)


######################## PROPERTY

# property ; use to   convert a method into a "getter" for an attribute.

class Celsius:
    def __init__(self, temp=0):
        print("Calling constructor...")
        self._temp = temp

    @property  # here everything starts , it makes the method to attribute
    #  and make it as getter method, as it has return statement.
    # getter method only self parameter , we can call this method like a attribute
    def temperature(self):
        print("Getting value...")
        return self._temp

    @temperature.setter  # this temperature  name comes from the above method name ,
    # note it method should have name temperature only.  it looks like constructor
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible.")
        print("Setting value...")
        self._temp = value

    @temperature.deleter
    def temperature(self):
        print("Deleting value...")
        del self._temp  # it delete the attribute


# Note above functions having same name. they were giving error ,
# then after applying @property @temperature.setter, @ deteler , it starting differentiating

c = Celsius(-10)
tmp = c.temperature  # here we calling temperature() method like a attribute, and we are getting values
print(tmp)

c.temperature = 25  # it is setter method, still we can use as attribute

print(c.temperature)

#  when we use + , python calls __add__ method, same for -,* ,
#


import random


class A:
    r = random.randint(0, 100)
    print(f"Random no. {r}")
    i = -1
    while i != r:
        i = int(input("Get no."))
        print(f"Random no. {r} , input : {i}")
        if i > r:
            print("Please provide smaller no.")
        elif i < r:
            print("Please provide larger no.")
        else:
            print("No is equal")


A()
