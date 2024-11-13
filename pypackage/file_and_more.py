# 6 : 00
# f=
# opw
import random

st = "Hello How are you \n yooo yoooo \n twinkle twinkle sachin is \n  ok it iss new \n  little start "
f = open("sample.txt", "w")
f.write(st)
f.close()

f = open("sample.txt", "r")  # read file
data = f.readlines()  # get all lines and add in list
print(f"Total lines  {len(data)}")
for line in data:
    print("data", line)

newline = f.readline()
while (newline != ""):
    print(newline)
    newline = f.readline()  ## // read line 1 by one
f.close()

f = open("sample.txt", "r")
data = f.read()
print(data)
f.close()

with open("sample.txt", "r") as f:  # with statement same as try with resorces
    data = f.read()

# read
with open("sample.txt", "r") as f:
    data = f.read()
    if data.count("twinkle") > 0:
        print("Twinkle Present")
    else:
        print("Not-Present")

    if "twinkle" in data:
        print("Twinkle is  Present")
    else:
        print("Twinkle is not Present")


def game():
    with open("sample.txt", "r") as f:
        line = f.readline()
        while (line != ""):
            print(line)
            line = f.readline()


game()

print(random.randint(1, 50))


# os.makedirs("testFolder", exist_ok=True)  # No Error if path exists,create recursively also


def generateTable(table):
    file = str(table) + "_.txt"
    with open(file, "w") as f:
        for i in range(1, 11):
            f.write(f"{table} * {i} = {table * i}  \n")


def startTable():
    for i in range(1, 4):
        generateTable(i)


# with statement :
str = 'hi donkey how are you , donkey , ganda , is no good ganda , donkey'
rep = ['donkey', 'ganda']
for word in rep:
    str = str.replace(word, "#####")
print(str)



with open("sample.txt", "r") as f:
    lineno = 1
    contet = 'sachin'

    data = f.readline()
    while (data != ""):
        if contet in data:
            print("line No", lineno)
        lineno += 1
        data = f.readline()
