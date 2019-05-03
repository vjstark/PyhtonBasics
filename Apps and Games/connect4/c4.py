import numpy as np

ROW_COUNT = 6
COL_COUNT = 7
def createBoard():
    board = np.zeros((ROW_COUNT,COL_COUNT))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] == piece

def is_valid_location(board, col):
    return board[5][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r


board = createBoard()
print(board)
game_over = False
turn = 0

while not game_over:
    #Ask for player 1 input
    if turn == 0:
        col = input("Player 1 make a selection (0-6):")

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
    #Ask for player 2 input
    else:
        selection = input("Player 2 make a selection (0-6):")

        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)

    print(board)
    turn += 1
    turn =  turn % 2 #alternate between 0 and 1
