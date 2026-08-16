import sys

print("Welcome to Python Pizza Deliveries!")

# Small $15, medium $20, large $25
# Pepperoni for S +$2, for M or L + $3
# Extra cheese for any size + $1

# Pizza prices
small_pizza = 15
medium_pizza = 20
large_pizza = 25

# Extras
small_pepperoni_fee = 2
medium_or_large_pepperoni_fee = 3
extra_cheese_fee = 1

# *******************************************************************************************************
# VERSION 4 - after I tried Angela's version and realised she had the same problems I tried to avoid, so I tried buiding an optimised version with the defences I wanted

bill = 0

# Prompt for the SIZE, PEPPERONI and EXTRA CHEESE
size = input("What size of pizza do you want? S, M or L: ").lower()

# Calculate the temp bill based on SIZE
if size == "s":
    bill = small_pizza
elif size == "m":
    bill = medium_pizza
elif size == "l":
    bill = large_pizza
else:
    print("If you still want a pizza, try again, but ensure to choose the right size from the available options.")
    sys.exit()

# Calculate the temp bill based on PEPPERONI
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
if size == "s" and pepperoni == "y":
    bill = bill + small_pepperoni_fee
elif (size == "m" or size == "l") and pepperoni == "y":
    bill = bill + medium_or_large_pepperoni_fee
elif pepperoni == "n":
    pass
else:
    print("If you still want a pizza, try again, but ensure to choose the valid response about pepperoni.")
    sys.exit()

# Calculate the final bill based on EXTRA CHEESE
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()  
if extra_cheese == "y":
    bill = bill + extra_cheese_fee
elif extra_cheese == "n":
    pass
else:
    print("If you still want a pizza, try again, but ensure to choose the valid response about extra cheese.")
    sys.exit()

print(f"Your bill is: ${bill}")

# *******************************************************************************************************


# # *******************************************************************************************************
# # VERSION 3 - after watching Angela's walkthrough. Her structure is exactly what I was trying to do with my V1 at first (until I got desperate)

# bill = 0

# # Prompt for the SIZE, PEPPERONI and EXTRA CHEESE
# size = input("What size of pizza do you want? S, M or L: ").lower()
# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
# extra_cheese = input("Do you want extra cheese? Y or N: ").lower()  

# # Calculate the temp bill based on SIZE
# if size == "s":
#     bill = small_pizza
# elif size == "m":
#     bill = medium_pizza
# elif size == "l":
#     bill = large_pizza
# else:
#     print("If you still want a pizza, try again, but ensure to choose the right size from the available options.")

# # Calculate the temp bill based on PEPPERONI
# if pepperoni == "y":
#     bill = bill + small_pepperoni_fee
# else:
#     bill = bill + medium_or_large_pepperoni_fee

# # Calculate the final bill based on EXTRA CHEESE
# if extra_cheese == "y":
#     bill = bill + extra_cheese_fee

# print(f"Your bill is: ${bill}")

# # *******************************************************************************************************
# VERSION 2
# size = input("What size of pizza do you want? S, M or L: ").lower()

# # todo: work out how much they need to pay based on their size choice
# # todo: work out how much to add to their bill based on their pepperoni choice
# # todo: work out their final amount based on whether they want extra cheese

# if size == "s":
#     bill = small_pizza

#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
#     if pepperoni == "y":
#         bill = bill + small_pepperoni_fee

#     extra_cheese = input("Do you want extra cheese? Y or N: ").lower()  
#     if extra_cheese == "y":
#         bill = bill + extra_cheese_fee

#     print(f"Your bill is: ${bill}")

# elif size == "m":
#     bill = medium_pizza

#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
#     if pepperoni == "y":
#         bill = bill + medium_or_large_pepperoni_fee

#     extra_cheese = input("Do you want extra cheese? Y or N: ").lower()  
#     if extra_cheese == "y":
#         bill = bill + extra_cheese_fee

#     print(f"Your bill is: ${bill}")

# elif size == "l":
#     bill = large_pizza

#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
#     if pepperoni == "y":
#         bill = bill + medium_or_large_pepperoni_fee

#     extra_cheese = input("Do you want extra cheese? Y or N: ").lower()  
#     if extra_cheese == "y":
#         bill = bill + extra_cheese_fee

#     print(f"Your bill is: ${bill}")

# else:
#     print("If you still want a pizza, try again, but ensure to choose the right size from the available options.") 
# *******************************************************************************************************

# *******************************************************************************************************
# VERSION 1
# todo: work out how much they need to pay based on their size choice
# The version below is a failed attempt, I tried making it work for 30+ mins if not more, in different ways, different structures. I was overthining optimisation and tried to write DRY code. But it wasn't working. I think I was trying to optimise it instead of writing simple code that works. I didn't want to repeat myself too much. I don't know why it was so hard when Treasure Island was so simple. I know this is more complex, but it's still very basic
# I was tempted to check the solution, but I know it would defeat the purpose. I decided to keep this code commented out for the record and start afresh
# I just wished I kept all my versions so Claude could see my thinking as I imagine the latest version might be the worse one out of desperation and guessing

# size = input("What size of pizza do you want? S, M or L: ").lower()

# if size == "s":
#     bill = small_pizza

#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
#     if pepperoni == "y":
#         bill = bill + small_pepperoni_fee

#     extra_cheese = input("Do you want extra cheese? Y or N: ").lower()       
#     if extra_cheese == "y":
#         bill = bill + extra_cheese_fee

#     print(f"Your bill is: ${bill}")
#     else:
#         print("Restart your order if you still want a pizza, make sure you reply with available options.")

# elif size == "m":
#     bill = medium_pizza

#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
#     if pepperoni == "y":
#         bill = bill + small_pepperoni_fee

#     extra_cheese = input("Do you want extra cheese? Y or N: ").lower()       
#     if extra_cheese == "y":
#         bill = bill + extra_cheese_fee

#     print(f"Your bill is: ${bill}")
#     else:
#         print("Restart your order if you still want a pizza, make sure you reply with available options.")

# elif size == "l":
#     bill = large_pizza

#     pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
#     if pepperoni == "y":
#         bill = bill + small_pepperoni_fee

#     extra_cheese = input("Do you want extra cheese? Y or N: ").lower()       
#     if extra_cheese == "y":
#         bill = bill + extra_cheese_fee

#     print(f"Your bill is: ${bill}")
#     else:
#         print("Restart your order if you still want a pizza, make sure you reply with available options.")

# else:
#     print("If you still want a pizza, try again, but ensure to choose the right size from the available options.")
# *******************************************************************************************************

