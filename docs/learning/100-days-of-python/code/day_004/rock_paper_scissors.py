import random

# Setting up ASCII art

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'    ____)____
           ______)
        __________)
       (____)
---.__(___)
'''

# ===

# TODO: Define a list for ASCII art + choices

ascii_art = [rock, paper, scissors]

# TODO: Prompt the user to choose

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 0 and user_choice <= 2:

    # TODO: Choose ASCII depending on user's choice

    print(ascii_art[user_choice])

    # TODO: Calculate computer's choice

    computer_choice = random.randint(0, 2)

    # TODO: Post computer's choice with ASCII

    print("\nComputer choice:")
    print(ascii_art[computer_choice])

    # TODO: Calculate the result

    winner = 0

    if user_choice == 0 and computer_choice == 1: # rock vs paper
        winner = "computer"
    elif user_choice == 0 and computer_choice == 2: # rock vs scissors
        winner = "user"
    elif user_choice == 1 and computer_choice == 0: # paper vs rock
        winner = "user"
    elif user_choice == 1 and computer_choice == 2: # paper vs scissors
        winner = "computer"
    elif user_choice == 2 and computer_choice == 0: # scissors vs rock
        winner = "computer"
    elif user_choice == 2 and computer_choice == 1: # scissors vs paper
        winner = "user"
    else:
        winner = "draw" # not using this one, might be better to refactor but not high prio now

    # Angela's if statement below
    # if user_choice >= 3 or user_choice < 0:
    #   print:("You typed an invalid number. You lose!")
    # elif user_choice == 0 and computer_choice == 2:
    #   print("You win!")
    # if computer_choice == 0 and user_choice == 2:
    #   print("You win!")
    # elif computer_choice > user_choice:
    #   print("You lose!")
    # elif user_choice > computer_choice:
    #   print("You lose!")
    # elif computer_choice == user_choice:
    #   print("It's a draw!")

    # TODO: Display the outcome of the round

    if winner == "user":
        print("You win!")
    elif winner == "computer":
        print("You lose!")
    else:
        print("Draw!")

else:
    print("Only numbers from 0 to 2 are allowed, try again.")