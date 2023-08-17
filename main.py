import random

word_list = ['disco', 'sound', 'adieu']
max_tries = 6


def pick_word():
  #need to pick a random word from the list
  rand_idx = random.randrange(0, len(word_list), 1)
  rand_word = word_list[rand_idx]
  word_arr = []
  for char in rand_word:
    word_arr.append(char)
  return word_arr


def check_guess(player_guess, word_arr):
  #check that the guess is 5 letters
  while len(player_guess) != 5:
    player_guess = input("Oops, that was not a 5 letter word. \nTry again: ")

  #create a dictionary for solution word
  word_dict = {}
  for item in word_arr:
    if item not in word_dict.keys():
      word_dict[item] = 1
    else:
      word_dict[item] += 1

  #print("word_dict: ", word_dict)

  guess_arr = []
  for char in player_guess:
    guess_arr.append(char)

  #now the guess array contains all the letters individually
  #now we need to create a guess dictionary
  guess_dict = {}

  #now we need to match it up with the actual word
  output_arr = []
  for idx in range(5):
    guess_letter = guess_arr[idx]
    if guess_letter == word_arr[
        idx]:  #if the letter is in the correct place put an 1
      output_arr.append('1')
    elif guess_letter in word_arr:  #if the letter is there but in the wrong place, put a 0
      if guess_letter not in guess_dict.keys():
        output_arr.append('0')
      else:  #if the letter has already been guessed at least once this turn
        #print(guess_letter, guess_dict[guess_letter], word_dict[guess_letter])
        if guess_dict[guess_letter] < word_dict[guess_letter]:
          output_arr.append('0')
        else:
          output_arr.append('-')  #for a missed letter
    else:  #if the letter is not in the word at all
      output_arr.append('-')

    #update the guess array after each letter is checked
    if guess_letter not in guess_dict.keys():
      guess_dict[guess_letter] = 1
    else:
      guess_dict[guess_letter] += 1

  print(output_arr)
  if output_arr == ['1', '1', '1', '1', '1']:
    print("Congrats you have won")
    return 1  #return a 1 to signal the game is over, 0 means keep going

  return 0


def play_game():
  word = pick_word()
  answer = 0
  tries = 0

  print(
      "Welcome to Wordle! \nYou will have 6 attempts to guess the correct word. If a letter in your guess is in the correct position, it will be marked with a '1'. If a letter in your guess is correct, but in the wrong position, it will be marked with a '0'. \nGood luck!\n"
  )

  while answer != 1 and tries < max_tries:  #6 tries
    player_guess = input("Please enter a 5 letter word: ")
    answer = check_guess(player_guess, word)
    tries += 1

  if tries == 6:
    print("\nOut of tries :(. Better luck next time.")

  print('bye bye')


play_game()
