"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. 
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""
def main():
   print(Fibonacci()) 

def userInput():
    return int(input("How long would you like the sequence to go?: "))

def Fibonacci():
    arrayLength = userInput()
    a = []
    for element in range(arrayLength):
        if (element == 0 or element == 1):
            a.append(1)
        else:
            a.append(a[element - 2] + a[element - 1])
    return(a)

if __name__ == "__main__":
    main()

