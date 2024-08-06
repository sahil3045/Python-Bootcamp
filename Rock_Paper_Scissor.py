import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
images = [rock, paper, scissors]
print("Welcome to rock paper scissors!!")
a = int(input("Type 0 for rock, 1 for paper and 2 for scissors:\n"))

if a >= 3 or a < 0: 
    print("You typed an invalid number try again.")
else:
    print(images[a])
    comp = random.randint(0, 2)
    print("Computer chose: ")
    print(images[comp])


    if a == 0 and comp == 2:
        print("You win!!")
    elif a == 2 and comp == 0:
        print("You loose!")
    elif a ==2 and comp == 1:
        print("You win!")
    elif a == 1 and comp == 0:
        print("You win!")
    elif comp> a:
        print("You loose!")
    elif a == comp:
        print("Its a Draw.")



