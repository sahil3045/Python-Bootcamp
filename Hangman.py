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

lives = 6

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
        elif letter in correct_letters:
            display += letter
        elif letter not in guess:
            lives - 1
        else:
            display += "_"
    print(display)

    if "_" not in display:
        game_over = True
        print("You win!!")


