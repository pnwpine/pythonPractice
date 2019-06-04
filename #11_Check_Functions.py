"""
Ask the user for a number and determine whether the number is prime or not. (For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity to practice using functions, described below.
"""
def main():
    divisors()

def get_integer(): #Created a specific function to get the integer
    return int(input("Enter a number: "))

def divisors():
    number = get_integer() #Instead of that code going here. We just call the get_integer method.
    divs = []
    x = range(1,number +1) #Cant mod by 0, remember that it is undefined

    for element in x:
        if (number % element == 0):
            divs.append(element)
    print(divs)

if __name__ == "__main__":
    main()
