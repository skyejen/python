import random
from art import logo

# Initialise the cards list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# ================================================ HELPER FUNCTIONS ================================================
def deal_random_card():
    """Deal a single random card"""
    random_card = random.choice(cards)
    return random_card

def deal_first_pair():
    """Deal the first two cards / hand to the player or the computer"""
    card_list = []
    for card in range(0, 2):
        card_list.append(deal_random_card())

    return card_list

def calculate_score(card_list):
    """Calculate the score of the player or the computer"""
    score = 0
    for card in card_list:
        score += card
    return score

def display_mid_game_results(user_cards, user_score, comp_cards):
    """Display the game results while the human player is still drawing more cards"""
    return (f"\tYour cards: {user_cards}, current score: {user_score}\n"
            f"\tComputer's first card: {comp_cards[0]}")

def display_final_game_results(user_cards, user_score, comp_cards, comp_score):
    """Display the game results after the human player stopped drawing more cards"""
    return (f"   Your final hand: {user_cards}, final score: {user_score}\n"
            f"   Computer's final hand: {comp_cards}, final score: {comp_score}")

def update_ace_points(score, card_list):
    """If player goes over 21 and have an ACE, replace 11 points with 1"""

    if score > 21 and 11 in card_list:
        temp_list = card_list.copy()
        for card in temp_list:
            if score <= 21:
                break
            elif card == 11:
                card_list.remove(11)
                card_list.append(1)
                score = score - 10

    return score

def add_new_card_adjust_aces_and_update_score(card_list, score):
    random_card = deal_random_card()
    card_list.append(random_card)
    score += random_card
    # Updating Ace points from 11 to 1 in case the player goes over 21
    score = update_ace_points(score, card_list)
    # Returning score only because we are updating cards inside this function
    return score

def is_round_over(user_score, comp_score):
    return user_score >= 21 or comp_score >= 21

def define_winner(user_score, comp_score):
    """Define a player who went over 21 or is closer to 21"""
    if user_score == comp_score:
        return "It's a draw!"
    elif user_score == 21:
        return "You win! :D"
    elif comp_score == 21:
        return "You lose! :("
    elif user_score > 21:
        return "You went over. You lose :'("
    elif comp_score > 21:
        return "Computer went over. You win! :)"
    elif user_score > comp_score:
        return "You win! :D"
    else:
        return "You lose! :("

# ================================================ MAIN GAME CODE ================================================

# New game switch
new_game = True

while new_game:
    # Prompt the player to see if they want to play Blackjack
    player_game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

    if player_game_on == "n":
        new_game = False
    else:

        # Print logo if player says 'y'
        print(logo)

        # Establish game session
        game_session = True
        continue_dealing = True

        while game_session:

            # Deal cards for the player
            player_cards = deal_first_pair()
            player_score = calculate_score(player_cards)

            # Deal cards for the computer
            computer_cards = deal_first_pair()
            computer_score = calculate_score(computer_cards)

            # Preliminary check for over 21 and adjusting aces if needed
            player_score = update_ace_points(player_score, player_cards)
            computer_score = update_ace_points(computer_score, computer_cards)

            # Check if anyone already won
            if is_round_over(player_score, computer_score):
                print(display_final_game_results(player_cards, player_score, computer_cards, computer_score))
                print(define_winner(player_score, computer_score))
                game_session = False

            else:
                # Display cards & scores
                print(display_mid_game_results(player_cards, player_score, computer_cards))

                # prompt the player for another card or to pass
                while continue_dealing:
                    player_more_cards = input("Type 'y' to get another card, type 'n' to pass: ").lower()

                    if player_more_cards == "y":
                        player_score = add_new_card_adjust_aces_and_update_score(player_cards, player_score)

                        if is_round_over(player_score, computer_score):
                            continue_dealing = False
                            game_session = False

                        else:
                            print(display_mid_game_results(player_cards, player_score, computer_cards))

                    else:
                        continue_dealing = False
                        while computer_score < 17:
                            computer_score = add_new_card_adjust_aces_and_update_score(computer_cards, computer_score)

                print(display_final_game_results(player_cards, player_score, computer_cards, computer_score))
                print(define_winner(player_score, computer_score))
                game_session = False
