# VERSION 2 - after chatting to Claude and him pointing out "else" in the diagram and ".lower()" trick
# Game logo start
print(r"""
***********************************************************************
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
***********************************************************************

                """)
# Game logo end

print("Welcome to Treasure Island.")

left_or_right = input("Your mission is to find the treasure.\nYou're at a cross road. Where do you want to go?\n\tType 'left' or 'right'\n").lower()

# First crossroad (right vs left)
if left_or_right == "left":

    wait_or_swim = input("You've come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()

    # Second crossroad (wait vs swim)
    if wait_or_swim == "wait":
        red_or_yellow_or_blue = input("You arrived at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which colour do you choose?\n").lower()

        # Third crossroad (red, yellow and blue)
        if red_or_yellow_or_blue == "red":
            print("It's a room full of fire. Game over.")
        elif red_or_yellow_or_blue == "yellow":
            print("You found the treasure! You win!")
        elif red_or_yellow_or_blue == "blue":
            print("You enter a room full of beasts. Game over.")
        else:
            print("Game over.")
    
    else:
        print("You get attacked by an angry trout. Game over.")

else:
    print("You fell into a hole. Game over.")  

# ########################################################################################

# VERSION 1 (played the game, didn't watch videos, didn't study the diagram)

# Game logo start
# print(r"""
# ***********************************************************************
#   ____________________________________________________________________
#  / \-----     ---------  -----------     -------------- ------    ----\
#  \_/__________________________________________________________________/
#  |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
#  |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
#  | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
#  |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
#  |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
#  |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
#  |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
#  |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
#  | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
#  |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
#  |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
#  | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
#  |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
#  | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
#  |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
#  | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
#  |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
#  | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
#  |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
#  |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
#  / \----- ----- ------------  ------- ----- -------  --------  -------\
#  \_/__________________________________________________________________/
# ***********************************************************************

#                 """)
# # Game logo end

# print("Welcome to Treasure Island.")

# left_or_right = input("Your mission is to find the treasure.\nYou're at a cross road. Where do you want to go?\n\tType 'left' or 'right'\n")

# # First crossroad (right vs left)
# if left_or_right == "right":
#     print("You fell into a hole. Game over.")
# elif left_or_right == "left":
#     wait_or_swim = input("You've come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat. Type 'swim' to swim across.\n")

#     # Second crossroad (wait vs swim)
#     if wait_or_swim == "wait":
#         red_or_yellow_or_blue = input("You arrived at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which colour do you choose?\n")

#         # Third crossroad (red, yellow and blue)
#         if red_or_yellow_or_blue == "red":
#             print("It's a room full of fire. Game over.")
#         elif red_or_yellow_or_blue == "yellow":
#             print("You found the treasure! You win!")
#         elif red_or_yellow_or_blue == "blue":
#             print("You enter a room full of beasts. Game over.")
    
#     elif wait_or_swim == "swim":
#         print("You get atacked by an angry trout. Game Over.")

# ########################################################################################


# Internal notes I've taken while playing Angela's game

# right -> "You fell into a hole. Game over."
# left -> "You've come to a lake. There is an island in the middle of the lake.\n\tType 'wait' to wait for a boat. Type 'swim' to swim across."

# wait -> "You arrived at the island unharmed. There is a house with 3 doors.\n\tOne red, one yellow and one blue. Which colour do you choose?"
## red -> "It's a room full of fire. Game over."
## yellow -> "You found the treasure! You win!"
## blue -> "You enter a room full of beasts. Game over."

# swim -> "You get attacked by an angry trout. Game Over."
