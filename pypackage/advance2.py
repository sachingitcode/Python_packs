from functools import reduce

l1 = [41, 32, 53, 94, 65, 56, 78, 8, 19]
l2 = ['a', 'c', 'g', 'e', 'k', 'a', 'p', 'd']

t1 = (1, 2, 3, 45, 56, 7, 89)
t2 = ('a', 'c', 'g', 'e', 'k', 'a', 'p', 'd')
s1 = {1, 2, 3, 4, 5, 5, 6, 1, 8, 9}
s2 = {'a', 'c', 'g', 'e', 'k', 'a', 'p', 'd'}


def func1(a):
    print(f"Function_1: {a} ")
    return 555


def func2(b):
    print(f"Function_2: {b} ")


def func3(c):
    print(f"Function_3: {c} ")


t = lambda a, b: a + b

sq = lambda x: x * x


def sq1(x):
    return x * x


func2(func1)

print(func3(123))
print(t(3, 6))

m = map(sq, s1)
print(list(m))

m1 = map(sq1, s1)  # sq1 is given but no arg provided
print(list(m1))


# map takes 2 args map(FUNCTION , itertable )
# map :it applies  given FUNCTION to all items in an input list (or any iterable)
# and returns a new iterable (often a list).


# filter :#  takes 2 args map(FUNCTION , itertable )
# Here FUNCTION usually return True/false
# filters elements based on a function that returns a Boolean value (True or False).
# Only elements that return True are included in the new iterable.

def even(a):
    if a % 2 == 0:
        return True
    return False


onlyEven = filter(even, l1)
print(list(onlyEven))

even_numbers = filter(lambda x: x % 2 == 0, l1)


# reduce (FUNCTION.iteratable) :


# FUNCTION takes two arguments and returns a single response., this is important to reduce
# ,because at last it reduce() to single result

def sum(a, b):
    return a + b


all = reduce(sum, l1)
print(all)

n = 3
ph = [(n * i) for i in range(1, 11)]
print(ph)
print(list(filter(lambda t: t % 5 == 0, ph)))


def greater(a, b):
    if a > b:
        return a
    return b


print(l1)
print(reduce(greater, l1))
