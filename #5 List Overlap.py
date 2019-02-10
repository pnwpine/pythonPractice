

import random

def abMaker():
    aNum = int(input("How long do you want A?: "))
    global a
    a = []
    bNum = int(input("How long do you want B?: "))
    global b
    b = []
    for x in range(1,aNum+1):
        a.append(random.randint(1,50))
    for x in range(1,bNum+1):
        b.append(random.randint(1,50))
    
    print(a)
    print(b)

def listoverlap():
    #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,5,6,7,8] made it dynamic :) 
    #b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] 

    returned = []  

    if (len(a) >= len(b)):
        for element in a:
            if element in b:
                returned.append(element)
    else:
        for element in b:
            if element in a:
                returned.append(element)
    returned = list(set(returned)) #Sets are unorded list of DISTINCT objects, if you need a list, type list infront.
    print(returned)                # Makes it so we dont have duplicate data


if __name__ == "__main__":
    abMaker()
    listoverlap()

