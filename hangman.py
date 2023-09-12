import random
word_list = ["hangman","player","worldcup"]
choosen_word= random.choice(word_list)

end_of_game = False
Lista =[]
size = len(choosen_word)
for _ in choosen_word:
    Lista+="_"
# print(Lista)
lives = 6
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

while not end_of_game:
    guess = input("Guess a letter : ").lower()
    for position in range(size):
        letter = choosen_word[position]
        if letter == guess:
            Lista[position] = letter
    
    if letter not in choosen_word:
        lives-=1
        if lives ==0 :
            end_of_game= True
            print ("You Lose ")
    if "_" in Lista:
        end_of_game= True
        print ("You win")

