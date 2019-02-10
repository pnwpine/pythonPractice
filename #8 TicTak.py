import random

def TickTack ():

    """
    Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare 
    them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
    """
    #I decided to make it one player.

    # Set initial variables


    userscore = 0
    opponentscore = 0
    while userscore or opponentscore < 3: # Start of game, indicate the score you want to go to.
        options = ["rock","paper","scisors"]
        useroption = input("Please choose either rock, paper ot scisor: ")
        oponentoption = random.choice(options)

        print(useroption, oponentoption) # For testing to see what the options were selected

        #Conditions for winning. NOTE: I used pass to make no code run in else due to a draw.

        if   (useroption == "rock" and oponentoption == "scisors"):
            userscore = userscore + 1
        elif (useroption == "scisors" and oponentoption == "rock"):
            opponentscore = opponentscore + 1
        elif (useroption == "scisors" and oponentoption == "paper"):
            userscore = userscore + 1
        elif (useroption == "paper" and oponentoption == "scisors"):
            opponentscore = opponentscore + 1 
        elif (useroption == "paper" and oponentoption == "rock"):
            userscore = userscore+1
        elif (useroption == "rock" and oponentoption == "paper"):
            opponentscore  = opponentscore+1
        else:
            pass
        print (userscore, opponentscore)

    # Check winning conditions

        if (userscore == 3):
            print("Congrats, you win!")
        elif (opponentscore == 3):
            print("Sorry, you lose")
        else:
            pass


            


def main():
    TickTack ()

if __name__ == "__main__":
    main()