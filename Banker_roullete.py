import random
a = input("Enetr your names:\n")
b = len(a)
names = list(a)
pay = random.randint(0, b - 1)
print(names[pay])
