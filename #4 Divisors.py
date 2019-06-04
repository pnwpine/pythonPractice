def divisor (number):
    divs = []

    x = range(1,number+1) #Cant mod by 0, remember that it is undefined

    for element in x:
        if (number % element == 0):
            divs.append(element)
    print(divs)



#Test Cases
def main():
    divisor(5)
    divisor(123455)
    divisor(1000)

if __name__ == "__main__":
    main()