import random

valid_options = ['paper', 'scissors', 'rock']
who_win = None
player_intention = 'yes'

print('Hello!')
my_name = input('What\'s your name?\n')
print('Hello', my_name)

print('Play one time a game with me', my_name)

pc_option = random.choice(valid_options)

while player_intention == 'yes':
    while True:
        player_option = input('Choose :{0}(Caution with the mayus)\n'.format(valid_options))
        if player_option not in valid_options:
            print("That is not a valid option you dickhead")
        else:
            break

    print('PC option: {0}'.format(pc_option))

    if (player_option == 'paper' and pc_option == 'rock') or \
            (player_option == 'scissors' and pc_option == 'paper') or \
            (player_option == 'rock' and pc_option == 'scissors'):
        input('You win {0},\nGG.'.format(my_name))

    if (pc_option == 'paper' and player_option == 'rock') or \
            (pc_option == 'scissors' and player_option == 'paper') or \
            (pc_option == 'rock' and player_option == 'scissors'):
        input('You lose {0},\nGAME OVER.'.format(my_name))

    else:
        input('Draw,\nGAME OVER.')
