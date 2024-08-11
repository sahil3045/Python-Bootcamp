print("Welcome to Python pizza delivery Services!!")

amount = 0

size = input("What size do you want? S, M, OR L?\n")
pepperoni = input("Do you want pepperoni? (Y or N): ")
cheese = input("Do you want cheese slice? (Y or N): ")

if size == "S":
    amount += 15
elif size == "M":
    amount += 20
else :
    amount += 25

if pepperoni == "Y":
    if size == "S":
        amount += 2
    else:
        amount += 3
    
if cheese == "Y":
    amount += 1
else:
    amount += 0

print(f"Thankyou for choosing Python pizza, Your total bill will be {amount}.")
