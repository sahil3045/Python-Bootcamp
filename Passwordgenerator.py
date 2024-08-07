import random 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["@", "&", "*", "/", "~"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to Pypassowrd Generator!")
a = int(input("Enter the number of letters you want in your password: "))
b = int(input("Enter the number of symbols you want in your password: "))
c = int(input("Enter the number of numbers you want in your password: "))

#Easy level
'''password = ""

for char in range(0, a):
    password += random.choice(letters)
    
for sym in range(0, b):
    password += random.choice(symbols)

for let in range(0, c):
    password += random.choice(numbers)

print(password)'''


#Hard level
password = []

for char in range(0, a):
    password.append(random.choice(letters))
    
for char in range(0, b):
    password.append(random.choice(symbols))

for char in range(0, c):
    password.append(random.choice(numbers))

print(password)
random.shuffle(password)
print(password)

passw = ""
for char in password:
    passw += char

print(f"Your Password is : {passw}")
        
