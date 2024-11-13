# print start
import math
import random

with open("oops.py","w") as f:
    f.write("")

n = 'sachin'
print("hello ,world")
print('hello ,world')
print(f'Hi {n}')
print("Hello", n)
print("How", 'are', 'you', sep="-")

print("This is line 1 ", end="")  # use for same line , no next line
print("This is line 2 ", end="\n")

for i in range(5):
    print(i, end=" ")

print(".")

n = 5
for i in range(1, n):
    print(" " * math.floor(n - i), "*" * (2 * i - 1))
    i = i + 1;
print(" ")

n = 5
for i in range(0, n):
    if i % 2 == 0:
        print("* " * n)
    else:
        print("*", " " * n, "*")
    i = i + 1;

print(" ")

num = 6;
for i in range(1, 11):
    print(num * (11 - i))
    i = i + 1;


################## FUNCTIONS::

def func1():
    print("Hello")


def f(t):
    print(t)


def f(f, t):
    print("Print 2 ", f + t)


def sum(a, b):
    return a + b


def circle_area(radius, pi=3.14):
    return pi * (radius ** 2)


func1()
# f(5)          # if we have 2 function of same name ,ir-respective of function variables/parameters , it overrides and below fuction works ,
f(9, 5)

print(sum(4, 6))

print(circle_area(4))  # usiing default pi value
print(circle_area(4, 3.1415))  # we can pass custom values

# Lambda functions :
square = lambda x: x ** 2
print(square(4))


# Recursive

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sums(n):
    if n == 1:
        return 1
    return sums(n - 1) + n

    #  Note trick for recursion, it should have 1 terminating condition , other part is recursion


print(sums(5))
print(factorial(5))

'''
 ***
 **
 * '''


def pattern(n):
    print("*" * n)
    if (n == 0):
        return
    pattern(n - 1)


pattern(5)


def inch_to_cm(inch, conversion=2.54):
    return inch * conversion;


c = 'sachin'.replace('ac', 'yo')
print(c)
print('sachin'.split('hi'))  # split to create a list ['sac', 'n']

# strip used to remove whitespaces by default , it takes arg , and removes that too
print('  sachin  '.strip())
print('  sachin yadav'.strip('yadav'))
print('###  sachin  '.strip('####'))
print('  sachin  '.strip())
print(' sachin  '.lstrip())
print('!  sachin  '.rstrip())

# 5:35:00
''' ston -1 ,paper=0 ,scissor=1  


'''


def sn_wa_gun(com):
    print("*" * 3, "Comp ", com)
    dict = {'stone': -1, 'paper': 0, 'scissor': 1}  # 1   ,  -1
    print("Comp", )
    for key, value in dict.items():
        if value == com:
            print("Comp Value", key)
            break;
    you = (input("Enter stone ,paper ,scissor:: ")).lower()

    if you in dict.keys():  # -1 ,    my 1
        if com == dict.get(you):
            print("Draw")
        else:
            if com == 1 and dict.get(you) == -1:
                print("You Win")
            elif dict.get(you) > com:
                print("You Wins")
            else:
                print("Comp Win")
    else:
        print("Please enter correct value")


v = random.choice([-1, 0, 1])
sn_wa_gun(v)

# get Keys from value Map
