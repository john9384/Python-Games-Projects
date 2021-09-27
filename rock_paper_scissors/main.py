import random

def play():
  user = input('r => Rock, p => Paper, s => Scissors \
    Pick your choice ----> ')

  computer = random.choice(['r', 'p', 's'])

  if user == computer:
    print('Tie')
    return play()

  if check_winner(user, computer):
    return'You won'

  return 'Computer wins'

def check_winner(player1, comp):
  '''
  Rock beats sissors 
  sissors cuts paper
  paper beats rock
  '''
  
  if(player1 == 'r' and comp == 's') or (player1 == 's' and comp == 'p')\
    or (player1 == 'p' and comp == 'r'):
      return True


print(play())