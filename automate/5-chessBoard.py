# Chess Dictionary Validator

import pprint

# Generate a chessBoard dictionary:
chessBoard = {}
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for r in range(1, 9):
    for c in columns:
        chessBoard.setdefault(str(r) + c, '')

maxPiece = {'bking': 1, 'bqueen': 1, 'bbishop': 2, 'brook': 2,
'bknight': 2, 'bpawn': 8, 'wking': 1, 'wqueen': 1, 'wbishop': 2,
'wrook': 2, 'wknight': 2, 'wpawn': 8}

# Make dictionary to count pieces
def numPiece(board):
    count = {}
    checker = True
    for v in board.values():
        count.setdefault(v, 0)
        count[v] = count[v] + 1
    
    for k in count:
        if count[k] > maxPiece[k]:
            print('Too many of ' + k)
            checker = False  

    return checker


def isValidChessBoard(board):
    # Check king's existence
    checker = True
    if 'bking' not in board.values():
        print('bking is missing')
        checker = False

    if 'wking' not in board.values():
        print('wking is missing')
        checker = False

    if numPiece(board) == False:
        checker = False

    for k in board.keys():
        if k not in chessBoard.keys():
            print(k + ' is out of range.')
            checker = False

    return checker

testBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
'5h': 'bqueen', '3e': 'wking', '2c': 'bpawn',
'4a': 'wrook', '5e': 'wrook'}

if isValidChessBoard(testBoard):
    print('The board is valid.')
else:
    print('The board is not valid')
