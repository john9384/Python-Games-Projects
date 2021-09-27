import json
import random
import string

file = open('names.json')
data = json.load(file) 


def get_valid_name(names):
  name = random.choice(names)
  return name.lower()

def count_appearance(letter, name):
  return name.count(letter)

def replace_in_new_list(old_list, new_list, letter):
  for index, val in enumerate(old_list):
    if val == letter:
      new_list[index] = letter

def print_result(player1, player2):
  print('{:^8}   {:^8}'.format('Player-1', 'Player-2'))
  print('{:^8}   {:^8}'.format(player1, player2))

def hangman():
  name = get_valid_name(data)
  name_letters = list(name)
  letter_guess = ['*' for _ in range(len(name_letters))]
  
  player1 = 0
  player2 = 0

  player_turn = 'player1'

  while "*" in letter_guess:
    guess = input(f"{player_turn} guess => ")
    letter_app_count = count_appearance(guess, name_letters)
    if guess in letter_guess:
      print("Letter already guessed")
      continue
    
    if player_turn == 'player1':
      if guess in name_letters:
        replace_in_new_list(name_letters, letter_guess, guess)
        player1 += letter_app_count
        player_turn = 'player2'
      else:
        print("Wrong guess")
        player_turn = 'player2'
        
      print(letter_guess)
      print_result(player1, player2)

    else:
      if guess in name_letters:
        replace_in_new_list(name_letters, letter_guess, guess)
        player2 += letter_app_count
        player_turn = 'player1'
      else:
        print("Wrong guess")
        player_turn = 'player1'
        
      print(letter_guess)
      print_result(player1, player2)

  print('========== Word Complete')
  print(''.join(letter_guess).title())
  print_result(player1, player2)
  





hangman()
