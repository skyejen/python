import random

# import logo for final testing (create a new file)
# print logo

# generate random number
guess = random.randint(1, 100)

# ========================================== HELPER FUNCTIONS ==========================================

def decide_on_difficulty(difficulty):
    """Assign number of lives based on difficulty user chosen."""
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    return lives

def nudge_user(user_guess, guess):
    """Helps user by nudging them in the right direction."""
    if user_guess < guess:
        return "Too low.\nGuess again."
    elif user_guess > guess:
        return "Too high.\nGuess again."

def declare_game_resuls(lives, user_guess, guess):
    """Declare the end game results."""
    if lives <= 0:
        return "You've run out of guesses. Refresh the page to run again."
    elif user_guess == guess:
        return f"You got it! The answer was {guess}."

# ============================================ MAIN GAME CODE ============================================

# greet the user at the start of the game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# ask for difficulty & assign the correct number of lives
user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
lives = decide_on_difficulty(user_difficulty)

game_over = False

while not game_over:
    # let user know how many lives they have left
    print(f"You have {lives} attempts remaining to guess the number.")

    # ask the user to make a guess
    user_guess = int(input("Make a guess: "))

    # check if the user has won
    if user_guess == guess:
        print(declare_game_resuls(lives, user_guess, guess))
        game_over = True

    else:
        # deduct a life if the user guessed wrong
        lives -= 1

        # end the game if the user ran out of lives
        if lives <= 0:
            print(declare_game_resuls(lives, user_guess, guess))
            game_over = True

        # if the game is still going, help the user and reprompt
        else:
            print(nudge_user(user_guess, guess))
