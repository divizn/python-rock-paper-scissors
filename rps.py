import random

yourScore = 0
compScore = 0
ties = 0
choices = ['rock', 'paper', 'scissors']


def totalScores():
    print("====================SCORES====================")
    print(f"Your score: {yourScore}")
    print(f"Computer score: {compScore}")
    print(f"Ties: {ties}")
    print("==============================================")


while True:
    inp = input("Please choose rock, paper, scissors or type 'Q' to quit) ")

    if inp.upper() == 'Q':
        break
    
    if inp not in choices:
        continue

    else:
        computer = random.choice(choices)

        if inp == 'rock' and computer == 'scissors':
            print(f"You chose {inp} and the computer chose {computer}")
            print("You win!")
            yourScore += 1
            
        elif inp == 'scissors' and computer == 'paper':
            print(f"You chose {inp} and the computer chose {computer}")
            print("You win!")
            yourScore += 1

        elif inp == 'paper' and computer == 'rock':
            print(f"You chose {inp} and the computer chose {computer}")
            print("You win!")
            yourScore += 1

        elif inp == computer:
            print(f"You chose {inp} and the computer chose {computer}")
            print("It's a tie!")
            ties += 1

        else:
            print(f"You chose {inp} and the computer chose {computer}")
            print("You lose!")
            compScore += 1


totalScores()
quit()