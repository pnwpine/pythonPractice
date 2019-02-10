def listless ():
    a = [1,1,2,3,5,8,13,21,34,55,89]
    b =[]

    usrnum = int(input("Please enter a number: ")) #Ask for a number to pivot by

    for element in a:
        if (element < usrnum):
            b.append(element) #Appends the number to a list made
    print(b) 

def main():
    listless()  #Could make a dynamic testing case here but its not in the scope of this example.         

if __name__ == "__main__":
    main()
