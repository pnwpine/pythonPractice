
#Logic Function

def OddEven (number):

    """
    Checks to see if a number is off or event via modululois

    if x mod 2 = 0 then it is even due to the remander of the devsion being zero.

    off if otherwise

    """
    if (number % 2 == 0):
        print("The number %i is even" % (number))
    else:
        print("The number %i is odd" % (number))


# Test Cases

"""
Test Cases are important, I use them to determine that it is all working and that I didnt miss anything. 

"""
def main():
    OddEven(2)
    OddEven(5)
    OddEven(5394857348)
    OddEven(0)

#How I set it to main

"""
Main function is the entry point of any program. But python interpreter executes the source file code sequentially
 and doesn’t call any method if it’s not part of the code.But if it’s directly part of the code then it will 
 be executed when the file is imported as a module.

That’s why there is a special technique to define main method in python program, so that it 
gets executed only when the program is run directly and not executed when imported as a module.
 Let’s see how to define python main function in a simple program

"""

if (__name__ == '__main__'):
        main()