# Version 2 - after watching the solution (for tips and tricks)
# Angela is using a lot more variables, I reformatted my stuff like hers (order and spacing) but I don't want more variables
# print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill = tip / 100 * bill + bill
bill = round(bill / people, 2)

print(f"Each person should pay: ${bill:.2f}") # Claude reminded me about .2f trick!

# ==============================================

# Left my old to-dos intentionally, don't worry Claude, I'd delete them in a work setting/portfolio, but this is a learning journal
# TODO: check if numbers work +
# TODO: add f strings to display currency +
# TODO: see if you can optimise

# ==============================================

# Version 1 (fully mine), it works but I want to see if I can otpimise it

# print("Welcome to the tip calculator!")

# bill = int(input("What was the total bill? $"))

# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# bill = bill / 100 * tip + bill

# people = int(input("How many people to split the bill? "))

# bill = round(bill / people, 2)

# print(f"Each person should pay: ${bill}")