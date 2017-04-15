import random
import pprint
print ('Welcome to TicTacToe!!!')
print ('Good luck, Have fun ^_^ ')
TTTBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def pb(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
pb(TTTBoard)

print ("Enter the number of your move")
print ( '1|2|3')
print ('-+-+-')
print ('4|5|6')
print ('-+-+-')
print ('7|8|9')

k = int(input())
if k == 1:
    TTTBoard['1'] = 'X'
elif k == 2:
    TTTBoard['3'] = 'X'
elif k == 3:
    TTTBoard['3'] = 'X'
elif k == 4:
    TTTBoard['3'] = 'X'
elif k == 5:
    TTTBoard['3'] = 'X'    
elif k == 6:
    TTTBoard['3'] = 'X'
elif k == 7:
    TTTBoard['3'] = 'X'
elif k == 8:
    TTTBoard['3'] = 'X'    
else:
    TTTBoard['4'] = 'X'
pb(TTTBoard)