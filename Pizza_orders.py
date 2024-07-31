print("Thankyou for choosing Python pizza deliveries!!")
#
size = input("What size do you want? S, M, OR L?\n")
amount = 0
if size == "S":
    amount + 15 
    pepperoni = input("Do you want Pepperoni?(Y or N) +2: ")
    if pepperoni == "Y":
        amount + 2
        Cheese = input("Do you want cheese on your pizza?(Y or N) +1: ")
        if Cheese == "Y":
            amount + 1
        else:
            print(amount)
    else:
        print(amount)
else:
    print(amount)

if size == "M": 
    amount + 20
    pepperoni = input("Do you want Pepperoni?(Y or N) +3: ")
    if pepperoni == "Y":
        amount + 3
        Cheese = input("Do you want cheese on your pizza?(Y or N) +1: ")
        if Cheese == "Y":
            amount + 1
    else:
        print(amount)

if size == "L": 
    amount + 25
    pepperoni = input("Do you want Pepperoni?(Y or N) +3: ")
    if pepperoni == "Y":
        amount + 3
        Cheese = input("Do you want cheese on your pizza?(Y or N) +1: ")
        if Cheese == "Y":
            amount + 1
    else:
        print(amount)
