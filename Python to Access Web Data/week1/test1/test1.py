import re

data = open("text2.txt", "r")

x = data.read()

y = re.findall("[0-9]+", x)

print(type(y))


def sum(y):
    total = 0
    for i in y:
        i = int(i)
        total += i
    return total


print(sum(y))
