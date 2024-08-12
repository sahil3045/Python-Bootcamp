import random
print("Welcome to Hangman game.")
word_list = ["bottle", "phone", "pen", "pencil"]
chosen_word = random.choice(word_list)
len = len(chosen_word)

placeholder = ""
for position in range(0, len):
    placeholder += "_"
print(placeholder)


#print(guess)

while guess == chosen_word:
    guess = input("Guess the letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
        else:
            display += "_"
    print(display)
