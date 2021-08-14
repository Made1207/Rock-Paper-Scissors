import random

def tictactoe():
    options = ['r', 'p', 's']
    com_score = 0
    pl_score = 0
    while pl_score != 3 and com_score != 3:
        com_pick = random.choice(options)
        user_input = input('Pick an option. Rock (r), Paper (p) or Scissors (s): ')

        if user_input == 'r':
            pick = 'rock'
        elif user_input == 'p':
            pick = 'paper'
        elif user_input == 's':
            pick = 'scissors'

        if com_pick == 'r':
            compick = 'rock'
        elif com_pick == 'p':
            compick = 'paper'
        elif com_pick == 's':
            compick = 'scissors'

        if com_pick == user_input:
            print('Computer played', compick + '. You played', pick + '.')
            print('It is a draw. Play again: ')

        if user_input == 'r':
            if com_pick == 's':
                pl_score = pl_score + 1
                print('Computer played scissors. You played rock. You won.')
                print('The score is', pl_score, ':', com_score)
            elif com_pick == 'p':
                com_score = com_score + 1
                print('Computer played paper. You played rock. You lost.')
                print('The score is', pl_score, ':', com_score)

        elif user_input == 'p':
            if com_pick == 'r':
                pl_score = pl_score + 1
                print('Computer played rock. You played paper. You won.')
                print('The score is', pl_score, ':', com_score)
            elif com_pick == 's':
                com_score = com_score + 1
                print('Computer played scissors. You played paper. You lost.')
                print('The score is', pl_score, ':', com_score)

        elif user_input == 's':
            if com_pick == 'p':
                pl_score = pl_score + 1
                print('Computer played paper. You played scissors. You won.')
                print('The score is', pl_score, ':', com_score)
            elif com_pick == 'r':
                com_score = com_score + 1
                print('Computer played rock. You played scissors. You lost.')
                print('The score is', pl_score, ':', com_score)

    if com_score == -3:
        print('You lost. The score is', pl_score, ':', com_score)
    elif pl_score == 3:
        print('You won. The score is', pl_score, ':', com_score)

tictactoe()