import random
print("Welcome to Hangman game.")
word_list = ["bottle", "phone", "pen", "pencil"]
chosen_word = random.choice(word_list)
len = len(chosen_word)

placeholder = ""
for position in range(0, len):
    placeholder += "_"
print(placeholder)

guess = input("Guess the letter: ").lower()
print(guess)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")








