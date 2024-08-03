print("The love calculator is calculating your score....")

name1 = input("Enter name1: ")
name2 = input("Enter name2: ")

combined_names = name1 + name2
a = combined_names.lower()
t = a.count("t")
r = a.count("r")
u = a.count("u")
e = a.count("e")
first = t + r + u + e

l = a.count("l")
o = a.count("o")
v = a.count("v")
e = a.count("e")
second = l + o + v + e

score = (first) + (second)
if (score < 10) or (score > 90):
    print("Your score is ", score, " you go togeather like coke and mentos.")
elif (score >= 40) or (score <= 50):
    print("Your score is ", score, " you go alright together.")
else: 
    print("Your score is ", score, ".")