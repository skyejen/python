import random
import os
from game_data import data
from art import logo, vs


# generate a random opponent
def generate_random_opponent():
    '''This function generates a random opponent out of the list of dictionaries in the data list and returns a list of that opponent.'''
    random_opponent = random.choice(data)
    return random_opponent

def make_comparison_statement(random_opponent_dictionary, letter):
    '''Thus function unpacks a random dictionary and builds a "Compare" statement.'''
    opponent = random_opponent_dictionary["name"]
    description = random_opponent_dictionary["description"]
    country = random_opponent_dictionary["country"]
    return f"Compare {letter}: {opponent}, a {description}, from {country}."

def check_for_and_replace_duplicate_opponent(opponent_1, opponent_2):
    while opponent_1 == opponent_2:
        opponent_2 = generate_random_opponent()
    return opponent_2

def compare_followers(opponent_1, opponent_2):
    '''Compares follower count between the opponents and returns the winner.'''
    if opponent_1["follower_count"] > opponent_2["follower_count"]:
        return opponent_1
    elif opponent_1["follower_count"] < opponent_2["follower_count"]:
        return opponent_2
    else:
        # returns None if it's a draw
        return

def clear_screen_and_reprint_logo(game_logo):
    '''This function clears the terminal and reprints the game logo.'''
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # reprint logo here so it doesn't appear between print statements
    print(game_logo)

def game():

    # generate A and B for the round + define the starting variables
    opponent_a = generate_random_opponent()
    opponent_b = generate_random_opponent()

    # fix for "same opponent for both A and B" bug
    opponent_b = check_for_and_replace_duplicate_opponent(opponent_a, opponent_b)

    # setting user score
    score = 0

    # game loop
    should_game_continue = True

    # print logo
    print(logo)

    while should_game_continue:

        # print "Compare A: FC Barcelona, a Football club, from Spain."
        print(make_comparison_statement(opponent_a, "A"))

        # print vs logo
        print(vs)

        # print "Against B: Justin Bieber, a Musician, from Canada."
        print(make_comparison_statement(opponent_b, "B"))

        # ask for user input with "Who has more followers? Type 'A' or 'B': "
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # little hack for easier comparison
        if user_guess == "a":
            user_guess = opponent_a
        elif user_guess == "b":
            user_guess = opponent_b

        # compare number of followers
        winner_dict = compare_followers(opponent_a, opponent_b) # this returns a dictionary, but user will reply with A and B

        # check for the same follower count
        if winner_dict is None:
            # clear the screen & reprint the game logo
            clear_screen_and_reprint_logo(logo)

            # update score
            score += 1
            print(f"It's a draw! You are getting one for free, lucky you! Current score: {score}. Let's go!")

            # generate a new opponent for B
            opponent_b = generate_random_opponent()
            opponent_b = check_for_and_replace_duplicate_opponent(opponent_a, opponent_b)

        # calculate the result
        elif user_guess != winner_dict:
            # clear the screen & reprint the game logo
            clear_screen_and_reprint_logo(logo)

            # if player lost, print the game over message -> this ends game (no reprompt)
            print(f"Sorry, that's wrong. Final score: {score}")
            
            # exit the game
            should_game_continue = False

        else:
            # clear the screen & reprint the game logo
            clear_screen_and_reprint_logo(logo)

            # update score
            score += 1

            # print the winner message
            print(f"You're right! Current score: {score}.")

            # update option A to be the winner
            opponent_a = winner_dict

            # generate a new opponent for B
            opponent_b = generate_random_opponent()
            opponent_b = check_for_and_replace_duplicate_opponent(opponent_a, opponent_b)

game()

