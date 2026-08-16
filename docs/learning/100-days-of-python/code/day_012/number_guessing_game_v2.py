import random
from art import logo


# global variables for difficulty
EASY_DIFFICULTY_LEVEL = 10
HARD_DIFFICULTY_LEVEL = 5

# helper functions
def set_difficulty(user_preferred_difficulty):
    if user_preferred_difficulty == "easy":
        return EASY_DIFFICULTY_LEVEL
    else:
        return HARD_DIFFICULTY_LEVEL
    
def check_answer_provide_feedback(answer, guess):
    if guess > answer:
        return "Too high."
    elif guess < answer:
        return "Too low."
    else:
        return f"You got it! The answer was {answer}."
    

# defining the game function
def game():

    # print logo
    print(logo)

    # come up with an answer
    answer = random.randint(1, 100)

    # greet the user at the start of the game
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # set difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    # calculate lives based on difficulty
    lives = set_difficulty(difficulty)

    # declare guess (until user gives a real value)
    guess = -1

    while guess != answer:

        # check if user ran out of lives (and end the game if so)
        if lives <= 0:

            # ask to restart the page to play again
            print("You've run out of guesses. Refresh the page to run again.")
            # end the game
            break

        else:
            # give feedback on lives remaining
            print(f"You have {lives} attempts remaining to guess the number.")

            # ask for a guess
            guess = int(input("Make a guess: "))

            # compare answer and guess

            if answer == guess:
                # declare victory
                print(check_answer_provide_feedback(answer, guess))

            else:

                # deduct life if guess is wrong
                lives -= 1

                # give feedback (low/high)
                print(check_answer_provide_feedback(answer, guess))

                # ask to guess again
                if lives > 0:
                    print("Guess again.")

game()