import random

def guessing():
    a = random.randint(1,9)
    test = "false"
    while (test == "false"):
        pick = int(input("Please pick a number: "))
        if pick > a:
            print("You are too high")
        elif pick < a:
            print("You are too low")
        elif pick == a:
            test = "true"
    print("Congrats you got it!")
    

def main():
    guessing()

if __name__ == "__main__":
    main()