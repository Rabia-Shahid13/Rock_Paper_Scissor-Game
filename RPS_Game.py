import random

user_choice = int(input("Choose any number between 0 to 2. Enter 0 for Rock, 1 for Paper and 2 for Scissor. Please enter your choice:"))
if (user_choice >= 3 or user_choice < 0):
    print("Oops! You entered an Invalid number. Try again!")

else:
    computer_choice = random.randint(0, 2)

    print("User Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    if (user_choice == computer_choice):
        print("Game Draw!")
    elif (user_choice == 0 and computer_choice == 2):
        print("You win!")
    elif (computer_choice == 0 and user_choice == 2):
        print("You lose!")
    elif (user_choice > computer_choice):
        print("You win!")
    elif (user_choice < computer_choice):
        print("You loose!")