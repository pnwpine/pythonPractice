"""
Ask the user for a string and print out whether this string is a 
palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""
def Strlist(word):
    
    word1 = word[::-1] # L[x::y] means a slice of L where the x is the index to start from and y is 
                       # the step size. Here are some examples you can try in the interprete
    
    if (word == word1):
        print("This is a paladrome")
    else:
        print("this is not a paladrome")

def main():
    Strlist("abc")
    Strlist("racecar")
    Strlist("dab")
    Strlist("mom")

if __name__ == "__main__":
    main()