import random
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

lives = 6
game_over = False

import hangman_art
print(hangman_art.logo)
print("\n")

display = []
for letter in chosen_word:
    display += "_"

print("\n")
print(' '.join(display))

while not game_over:
  guess = input("\nGuess a letter: ").lower()
  print("\n*************************************")
  
  if guess in display:
    print (f"\nYou already guessed {guess}, please try again")
  
  
  for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
          display[position] = letter

  if guess not in chosen_word:
    lives -= 1
    print(f"\nThe letter {guess} is not in the word, you lose a life.")

  if lives == 1:
    print("\n!!CAREFUL, THIS IS YOUR LAST LIFE!!")
 
  print("\n")
  print(' '.join(display))
  print (hangman_art.stages[lives])

  if lives == 0:
    game_over = True
    print(f"\nThe word was {chosen_word}")
    print("You lose.")
    print("\n")

  if "_" not in display:
    game_over =  True
    print(f"\nYes, {chosen_word}")
    print("You win!")
