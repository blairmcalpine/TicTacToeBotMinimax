import copy

def print_board(board):
    print()
    for row in board:
        print('+---+---+---+')
        for spot in row:
            print('|',end='')
            if spot == None:
                print('   ',end='')
            else:
                print(' '+str(spot)+' ',end='')
        print('|')
    print('+---+---+---+\n')
        
def check_win(board, piece):
    for i in range(3):
        piece_count_1 = 0
        piece_count_2 = 0
        for j in range(3):
            if board[i][j] == piece: piece_count_1 += 1
            if board[j][i] == piece: piece_count_2 += 1
        if piece_count_1 == 3:
            return True
        elif piece_count_2 == 3:
            return True
    piece_count = 0
    for i in range(3):
        if board[i][i] == piece: piece_count += 1
    if piece_count == 3:
        return True
    piece_count = 0
    for i in range(3):
        if board[i][2-i] == piece: piece_count += 1
    if piece_count == 3:
        return True
    return False

def check_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False
    return True

def find_value(board, depth, is_turn, piece, opp_piece):
    if check_win(board, piece):
        return 10 - depth
    if check_win(board, opp_piece):
        return -10 + depth
    if check_full(board):
        return 0
    if is_turn:
        best_val = None
        for i in range(1, 10):
            temp_board = copy.deepcopy(board)
            if place_piece(temp_board, i, piece):
                value = find_value(temp_board, depth+1, False, piece, opp_piece)
                if best_val == None or value > best_val:
                    best_val = value
    else:
        best_val = None
        for i in range(1, 10):
            temp_board = copy.deepcopy(board)
            if place_piece(temp_board, i, opp_piece):
                value = find_value(temp_board, depth+1, True, piece, opp_piece)
                if best_val == None or value < best_val:
                    best_val = value
    return best_val

def find_place(board, piece, opp_piece):
    best_val = None
    best_move = None
    for i in range(1, 10):
        temp_board = copy.deepcopy(board)
        if place_piece(temp_board, i, piece):
            value = find_value(temp_board, 0, False, piece, opp_piece)
            if best_val == None or value > best_val:
                best_val = value
                best_move = i
    return best_move

def place_piece(board, pos, piece):
    try:
        pos = int(pos)
    except TypeError:
        return False
    if pos < 1 or pos > 9:
        return False
    if board[(pos-1)//3][(pos-1)%3] != None:
        return False
    board[(pos-1)//3][(pos-1)%3] = piece
    return True

def turn(is_human, board, piece, opp_piece):
    if is_human:
        while not place_piece(board, input('Enter the position (1-9): '), opp_piece):
                    print('Invalid Input.')
    else:
        print('Calculating...')
        place_piece(board, find_place(board, piece, opp_piece), piece)
    print_board(board)
    if check_win(board, piece):
        print(piece+"'s win.")
        return
    if check_win(board, opp_piece):
        print(opp_piece+"'s win.")
        return
    if check_full(board):
        print("Tie.")
        return
    turn((not is_human), board, piece, opp_piece)

if __name__ == '__main__':
    while True:
        board = [[None, None, None],
                 [None, None, None],
                 [None, None, None]]
        while True:
            start = input('Would you like to start? Enter Y for yes or N for no. ')
            if start.upper() == 'Y':
                print_board(board)
                turn(True, board, 'O', 'X')
                break
            elif start.upper() == 'N':
                board[0][0] = 'X'
                print_board(board)
                turn(True, board, 'X', 'O')
                break
            print('Invalid input.')

        again = input('\nWould you like to play again? Enter Y for yes or N for no. ')
        print()
        if again.upper() == 'N':
            break
        elif again.upper() == 'Y':
            pass
        else:
            print('Invalid input.')
        
