#
class T:
    def func(self):
        r = len([1, 2, 3, 4, 5, 6])
        if r > 5:
            print("print length more than 3")


# walrus opr : assign a value to a variable

if (r := len([1, 2, 3, 4, 5, 6])) > 5:
    print("print length more than 3", r)

#
sq = [x * x for x in range(10)]
print(sq)

t = 2
rs = "Even" if t % 2 == 0 else "Odd"
print(rs)

# lambda func:
# It is  func ,takes arg and return response;


squ = lambda y: y * y
print(squ(3))  # taking y and returning y square

add = lambda x, y: x + y
print(add(5, 3))

sho = lambda x, y: print(f"Values are {x} , {y}")
sho(4, 7)

from typing import List, Tuple

l: List[int] = [1, 2, 3, 4, 5, '123']
l2: List[int] = [11, 12, 13, 4, 15, '123']
print(l)

t: Tuple[str, int] = ("123", 123, 54, '5323', 'sachin', True)

print(t)

d1 = {'one': 1, 'two': 2, 'c': 'cat'}
d2 = {'d': 4, 'two': 5, 'e': '5'}

d3 = d1 | d2  # merge & update 2 dict. IT is basically OR operator

print(d3)

with open("oops.py", 'r') as f:
    pass

with open("p4_process.py", 'r') as f:
    pass

with( open("oops.py", 'r') as f,
      open("p4_process.py", 'r') as f2
      ): pass


#    print(str(f));
#    print(str(f));


def try_catch():
    try:
        print("try block")
        return "return_try_block"
        if 'a' == 'b':
            raise Exception("This is throw statement")

    except Exception as e:
        print(e)
        return "return_exception"
    finally:  # Note : even if try block executes without error, and it has return statement,still
        print("finally block")
    #  return "return_finally"


# Note : finally block executes everytime :

# else:  ## it runs after try block , not run when except block executes, will not run if finally
#    print("else block")  #

# 8:44:
print(try_catch())

# pip install virtualenv   # create a new environemt for python working
# pip freeze  # tells all the package install
# pip freeze >requirement.txt # write all packages names in txt file
# pip install -r 'requirement.txt'   # install all packages written in txt file ,when we are uploading release at that time we can provide this


l1 = ["harry", "sachin", "yahoo"]
final = " and ".join(l1)

print(final)
n = 6
ph = [  str(n * i)  for i in range(1, 11)]
print(ph)
ph1 = " \n".join(ph)

print(ph1)
