import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))


# My version after Claude told me about two tricks:
# easy_password_list = random_letters + random_numbers + random_symbols
# random.shuffle()

random_letters  = []
random_numbers  = []
random_symbols  = []
easy_password_list = []
hard_password_list = []

for letter in range(0, num_letters):
    new_letter = random.choice(letters)
    random_letters.append(new_letter)

for number in range(0, num_numbers):
    new_number = random.choice(numbers)
    random_numbers.append(new_number)

for symbol in range(0, num_symbols):
    new_symbol = random.choice(symbols)
    random_symbols.append(new_symbol)

easy_password_list = random_letters + random_numbers + random_symbols
random.shuffle(easy_password_list)

hard_password_str = ""

for char in easy_password_list:
    hard_password_str = hard_password_str + str(char)

print(hard_password_str)

# ================================================================================================================

# My first solo version, working but not optimised (and powered by Abbot, the tastiest ale ever)
# # easy version

# # generate random letters
# random_letters  = []

# for letter in range(0, num_letters):
#     new_letter = random.choice(letters)
#     random_letters.append(new_letter)

# # print(random_letters)

# # generate random numbers
# random_numbers  = []

# for number in range(0, num_numbers):
#     new_number = random.choice(numbers)
#     random_numbers.append(new_number)

# # print(random_numbers)

# # generate random symbols
# random_symbols  = []

# for symbol in range(0, num_symbols):
#     new_symbol = random.choice(symbols)
#     random_symbols.append(new_symbol)

# # print(random_symbols)

# # generate password itself - easy version

# easy_password_list = []
# easy_password_str = ""

# for char in random_letters:
#     easy_password_list.append(char)

# for char in random_numbers:
#     easy_password_list.append(char)

# for char in random_symbols:
#     easy_password_list.append(char)

# for char in easy_password_list:
#     easy_password_str = easy_password_str + str(char)

# # print(easy_password_list)
# # print(easy_password_str)

# # hard version
# easy_password_working_copy = easy_password_list.copy()
# hard_password_list = []
# hard_password_str = ""

# i = 0
# while i < len(easy_password_list):
#    new_letter_hard = random.choice(easy_password_working_copy)
#    easy_password_working_copy.remove(new_letter_hard)
#    hard_password_list.append(new_letter_hard)
#    i += 1

# for char in hard_password_list:
#     hard_password_str = hard_password_str + str(char)

# # print(hard_password_list)
# print(hard_password_str)


# ================================================================================================================

# Adding Angela's versions below after having watched the walkthrough

# Easy level

# password = ""
# for char in range(0, num_letters):
#     password += random.choice(letters)

# for char in range(0, num_symbols):
#     password += random.choice(symbols)

# for char in range(0, num_numbers):
#     password += random.choice(numbers)

# print(password)

# Hard level

# password_list = []

# for char in range(0, num_letters):
#     password_list.append(random.choice(letters))

# for char in range(0, num_symbols):
#     password_list.append(random.choice(symbols))

# for char in range(0, num_numbers):
#     password_list.append(random.choice(numbers))

# random.shuffle(password_list)

# password = ""

# for char in password_list:
#     password += char

# print(f"Your password is: {password}")