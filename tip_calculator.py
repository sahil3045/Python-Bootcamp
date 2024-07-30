print("Welcom to tip calculator.")

a = float(input("What was the total bill? $"))

b = int(input("How much tip would you like to give(percentage)? 10, 12, or 15?: "))

c = int(input("How many people to split the bill? "))

d = b/100*a+a

e = d/c
round(e, 2)

print("Each person should pay: $", e)