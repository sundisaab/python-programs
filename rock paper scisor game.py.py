import random #using random module 

def game():

    print("_-_-_-_-_ lets start _  _-_-_-_- ")
      
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = None
    while user_choice not in choices:
        user_choice = input('Enter your choice (rock, paper, scissors): ').lower()
    if user_choice == computer_choice:
        print('Tie!')
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print('wow you won the  game!')
    else:
        print('You lose!')

game()



def again():

    
    game_again = input('''
play agian?
type [y  /  n]
''')

     
    if game_again == 'y':
        game()
    elif game_again == 'n':
        print('thanks for  playing.')
    else:
        again()

 
game()

 
again()



