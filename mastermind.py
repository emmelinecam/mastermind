import random

red = 'red'
blue = 'blue'
yellow = 'yellow'
green = 'green'
white = 'white'
black = 'black'
colour_options = [red, blue, yellow, green, white, black]

playing = 'yes'

while playing == 'yes':
    guesses_used = 0
    won = False
    board = []
    board_length = 4
    for x in range(board_length):
        board.append(random.choice(colour_options))
        
    while won == False and guesses_used < 10:

        guesses_used = 0
        key_pegs = []
        
        print('please enter your next guesses.')
        print('you can choose from the following colours:')
        print(*colour_options,sep=', ')
        guesses = []
        for index in range(board_length):
            guess = input(f'guess {index+1}: ')
            guesses.append(guess)

        for x in range(0,4):
            if guesses[x] == board[x]:
                key_pegs.append(black)
            elif guesses[x] in board:
                key_pegs.append(white)
                
        print('your key pegs for this guess are:')
        print(*key_pegs)

        if guesses == board:
            won = True

    if won == True:
        print('congrats, you\'ve won!')

    elif guesses > 10:
        print('i\'m sorry, you\'ve run out of guesses!')

    playing = input('would you like to play again? yes/no: ')


