from orca.orca import start

e = True and False
# python is case sensative
print(e)

print(type(1))
print(type(1.0))

print(1 == 1.0)  ## it shows TRUE

c = 6
t = 6

print(c - 1)
print(++ t)
print(t)
a = [0, 1, 2, 3, 4, 5, 6]
print(a)
len(a)

j = a.count(11)
print(j)

r = 6 + 9j
b = [1, 3, 5, 2, 5]


def func1(t):
    if (t == 1234):
        print("yes3")
    else:
        print("no3")


if __name__ == "__main__":
    func1(123)

c1 = not (False)
print("s11", c1)

# print("value48 : ",__import__())
print("value48 : ", __name__)

# v = input("get input 1 :")
# w = input("get input 2 :")
v = 4
w = 5
print("val 1 ", v)
print("val 2 ", w)

print("sum:", v + w)

v = int(v)
w = float(w)
print("Sum2 ", v + w)

name = 'Sachin'
name2 = '''yadavG'''

print(name[0:])
print(name[:4])
print(name[1:3])
print(name[:-1])
print(name[-1:])

# String Functions

a = 'abcdefghijklmnopqrstuvwxyz'
b = a.endswith('xyz');
a.startswith('abc');
len(a)
d = a.count('c')

print('sachin'.capitalize())
print('sachin yadav'.capitalize())  # Only capitalize S , not y
print('sachin yadav nice'.title())  # capitalize all
str(12.2343)  # convert into str

'QWERT'.lower()
'asdfgh'.upper()

'asd tdfs !sd #adsd t'.title()

'abd defs ads'.find('ads')  # finds and  the first occurasae location , if not found return -1
'abd defs ads'.find('d')  # output 2

'sachin is good'.replace('good', 'bad')  # if good founds, replaces else do nothing

# Escape Sequence Chars
a = "Dear Sachin \n \tYou are a good boy. \n you will know   \"Go for it\" \n Thanks "

print(a.capitalize())  # it only capitailse 1 word and make lower to other letter
name = 'sachin'

print("My name is " + name)
print(f" Yoo My Name is {name}")  # f is mandatory

# List , Dict , Tuples
# [] -list   mutable
# () - tuple - immutable
# '' -str  -immutable
# {} - Set  -  // unorder // undefined // unindex // non Duplicate
# {} Dictionary { "s" :true , "y": "q",3:7 }   #map    d={} -> empty Dict


a = [1234, 'dfa', 534, 'qwe', False, '123.54', 64.5, None]
print(a)

y = [12, ["sachin", 454], ["232", 65], ["454"], [12, 34, 67, 7]]
print(y)
c = [123, 42, 454, 6, 8, 2, 67, 6, 86, 6, 8]
c.sort()
c.remove(454)
c.append(8)
c.count(6)
c.pop()
c.reverse()
d = c.copy()
print(d)
d.insert(4, 111)
print(d)
d.insert(999, 333)  # if index not found it insert at last
print(d)
d.insert(-1, 888)  # this is imp : as it list/str[] has negaiive index too
print(d)
d.insert(-111, 5678)  # if index not found it insert at first
print(d)

# TUPPLE

a = (1)
b = (1,)
print(type(a))  # int
print(type(b))  # tuple

c = (1, 5, 3, 'asdas', 34.43, '45', '56465', 123, 43, False, 5)
print(c.count(5))
print(c.index(5))
# print(c.index(1115))   # Note it index not found ,gives error, lol

tupple = (1, 2, 3, 4)
new = tupple * 3
print(new)  # (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)

print(4 in tupple)  # true or false
l = len(new)

print(tupple[1:7])  # no index out of bounderror
print(f"Tupple Length {l}")

c1 = (1, 2, 3,)  # note here it means 1,2,3  , ye next , ka bura nhi mante
x, y, z = c1
print(x, y, z)

print(x)

for i in range(5):
    print(f" i: {i}")

# Dictionary : KEY VALUE PAIR ; same as map
# inordered , mutable / indexed  :: NO DUPLICATE Keys

d = {}  # empty dict
marks = {"jatin": 50, "sachin": 30, "yatin": 14, "amit": 87, 1245: 45}
print(marks, type(marks))
print(marks.pop("sachin"))
print(marks.pop("sachinyadav",
                "default_value"))  # this is nice !! , if key is not found ,then return default , if  default not provided, and key not present return error
print(marks.popitem())  # return last item

print(marks["jatin"])
print(marks)

new = {"sachin": 10,
       "yatin": 40,
       "amit": 50,
       "list": [1, 2, 34, 5],
       "map": {"t": 10, "p": 40},
       "sachin": 20  # sachin duplicate , no error , it overrides
       }

print(new)
print(new.keys())
print(new.values())
print(new.get("amit"))

print(new.get("amit2"))  # if exists , provides value , else return None
# print(new["amit2"])     # if exists , provides value , else return ERROR


## FROM KEYS : get values from list and create dict and its value would be X
keys = ["sachin", "yadav", "sharma"]
map1 = dict.fromkeys(keys, 100)

print(map1)  # new map/dict created with value 100

print(new)
ma = {"t": 10, "p": 40}

print(type(ma))

map("123", "11111")  # this is for higher
print()
words = {"a": 'v', "c": 'd', "e": "f"}
print(words.get("c"))

# SET SET SET SET SET SET SET
# SET
s = {12, 3, 5, 6, 5, 78}  # set
s1 = {"s": 12, "A": 3, "a": 5}  # dict

d = {}  # empty dict
sy = set()  # empty set

len(s)
# s.pop()  # not advisable remove random element
s.remove(3)  # remove element , if not found gives ERROR  , so we use discard
s.discard(312345)  # remove , if not found ,no error
s.clear()  # clear
#
s = {12, 3, 5, 6, 5, 78}  # set

# SET union intersection disjoint  # learn about it    difference_update
s1 = {1, 2, 3, 4, 5, 6, 7}
s2 = {5, 6, 7, 8, 9, 0}

s3 = s1.union(s2)  # s1 | s2  # gives all elements
s4 = s1.intersection(s2)  # s1 & s2  # gives eleemts present in both
s5 = s1.difference(s2)  # s1 - s2 # elements only in s1

print(f"union  {s3}")
print(f"intersection  {s4}")
print(f"subtract  {s5}")

print(
    f"subset  :{s1.issubset(s2)}")  # subset means all elements of s1 should present in  s2  eg  {1,2}.issubset({1,2,3,4})
print(f" superset :{s1.issuperset(s2)}")  # subset  s1 has allements of s2    :  s2 {1,2,5,7,8}.issuperset({1,2,7})
print(f"disjoin: {s1.isdisjoint(s3)}")  # no elements  in
print(f" diff :{s1.difference(s2)}")
print(f"diff_update : {s1.difference_update(s2)}")

# s1.symmetric_difference_update()  #
# s1.update()  #
# s1.add()  #
# s1.__contains__()  #
# s1.  s1#

# imp : we can not have list inside set ,as sets elements are required to be hashable and immutable
# ERROR : TypeError: unhashable type: 'list'    for below cmd
# s = {1, 2, 3, 4, 5, [1, 2, 3, 4]}

# CONDITIONS
v = 12
if v != 123:
    print("fail")
elif v != 123:
    print("fail")
else:
    print("fail")
v = 10
if (v > 18):
    print("More than 18", v)
elif (v < 0):
    print("Less than 0 ", v)
else:
    print("Less than 18", v)

marks1 = 100  # int(input("Provide Marks "))
marks2 = 99  # int(input("Provide Marks "))
marks3 = 28  # int(input("Provide Marks "))
total_percentage = (marks1 + marks2 + marks3) / 3

print(total_percentage)
if total_percentage > 40 and marks1 > 33 and marks2 > 33 and marks3 > 33:
    print("passed", total_percentage)

l = ["sachin", "amit", "rahul", 'punnet']
n = 'amit'
if n in l:
    print(n, " is passed")
else:
    print(n, "is failed")

name = "Sachin is gOoD boY"

if 'good' in name:
    print("a true")

if 'sachin' in name:
    print("Sachin true")

if 'good'.lower() in name.lower():
    print("good true")

#### LOOOPSSS

for i in range(5):
    print(i)

print("To Ten Data")

j = 1
while j < 10 and j % 2 == 0:
    print(j)
    j += 1

t1 = {18, 12, 13, 14, 16, 17, 15, 15, 13, 18, 15, 14}

print(t1)

for j in t1:
    print(j)

# RANGE ( start , stop, step_Size)   step_Size is numbers to jump

# t = [1, 56, 7, 4, 08, 23]     # 0 at starting not allowed
# leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers

for i in range(0, 18, 3):
    print("step up ", i)

# NICE THINGS : FOR loop with else ::  after for loop exits, it will start else part ***
# \\

for item in range(0, 9, 3):
    print("item range ", item)
    item += 1
else:
    print("value of ", item)

for item in range(0, 9):
    item += 1
    if (item == 5):
        continue
    print("item range-- ", item)
else:                            # if we add break in for and break statemwnt run , then else not work , else with foe only works when for loop exhaust
    print("value of ", item)

for i in (1, 2, 3, 45, 5):
    pass  # if u dont want to anything, just use pass . it is used to do nothing

for item in ['sachin', 'amit', 'yatin', 'sachil', 'SaSa', 'akash']:
    if item.lower().startswith('s'.lower()):
        print("Name is ", item)

# for(int i=0 ; i< 10 ; i++)
for i in (0, 10):
    i += 1

i = 0;
total_sum = 0
while (i < 11):
    total_sum = total_sum + i
    i = i + 1

print(total_sum)




s=' it is said that my name is my # the value is  905020 '

print(len(s))
print(s.upper())
print(s.lower())
s.capitalize()
print(s.title())  # each 1st work capital
print(s.strip())  # trim
print(s.replace('old','was'))
lst=s.split(" ")  # split into spring by (',')
strn=",".join(lst) # join list by ,
print(strn)
print(s.find("name"))  # Output: 21  , -1 fit not found
startswith
endswith
isalpha

s = "12345"
print(s.isdigit())

s = "Hello123"
print(s.isalnum())

s = "I love Python. Python is great!"
print(s.count("Python"))

name = "John"
age = 25
s = "My name is {} and I am {} years old.".format(name, age)
print(s)


s = "Hello"
print(s.center(10))












































