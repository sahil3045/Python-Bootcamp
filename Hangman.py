import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
print("Welcome to Hangman game.")
word_list = ["bottle", "phone", "pen", "pencil"]
chosen_word = random.choice(word_list)
len = len(chosen_word)

placeholder = ""
for position in range(0, len):
    placeholder += "_"
print(placeholder)


#print(guess)
game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess the letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!!")


