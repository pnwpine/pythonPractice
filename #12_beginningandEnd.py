"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""

import random

def main():
    cutter()

def cutter():
    a = arrayMaker()
    highestElement = len(a)
    lowestElement = 0
    b = []
    b.append(a[lowestElement])
    b.append(a[highestElement -1 ])
    print (b)

def arrayMaker():
    size = arrayLength()
    a = []
    for element in range(size):
        a.append(random.randint(0,1000000))
    print(a)
    return a


def arrayLength():
    return int(input("How long would you like the list to be?: "))


if __name__ == "__main__":
    main()