"""Tic Tac Toe 3x3 version"""

import sys

game_board = {1: '1', 2: '2', 3: '3', 4: '4',
              5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

PLAYER_SIGN = 'O'
COMPUTER_SIGN = 'X'


def choose_sign(player_sign, computer_sign):
    """Allows user to choose 'X' or 'O'"""
    choosen = ' '

    while choosen not in ('X', '0'):
        choosen = str(input('Choose X or O: '))

        if choosen == 'X':
            player_sign = 'X'
            computer_sign = 'O'
            return player_sign, computer_sign
        if choosen == 'O':
            player_sign = 'O'
            computer_sign = 'X'
            return player_sign, computer_sign
        print('try again')


def print_game_board(board):
    """Prints game board"""
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('\n')


def check_if_position_free(board, board_position):
    """Checks if choosen position is free"""
    return bool(board[board_position])


def check_draw(board):
    """Checks for game draw"""
    for key in board.keys():
        if board[key] == str(key):
            return False
    return True


def check_win(board, sign):
    """Checks if 'sign' player wins"""
    if board[1] == board[2] and board[2] == board[3] and board[1] == sign:
        return True
    if board[4] == board[5] and board[5] == board[6] and board[4] == sign:
        return True
    if board[7] == board[8] and board[8] == board[9] and board[7] == sign:
        return True
    if board[1] == board[4] and board[4] == board[7] and board[1] == sign:
        return True
    if board[2] == board[5] and board[5] == board[8] and board[2] == sign:
        return True
    if board[3] == board[6] and board[6] == board[9] and board[3] == sign:
        return True
    if board[1] == board[5] and board[5] == board[9] and board[1] == sign:
        return True
    if board[3] == board[5] and board[5] == board[7] and board[3] == sign:
        return True

    return False


def make_move(char, position, board, player_sign, computer_sign):
    """Assign player or computer sign to choosen position"""
    if check_if_position_free(board, position):
        board[position] = char
        print_game_board(board)
        if check_draw(board):
            print('Draw')
            sys.exit()
        if check_win(board, computer_sign):
            print('Bot wins')
            sys.exit()
        if check_win(board, player_sign):
            print('Player wins')
            sys.exit()

        return

    print('This position is already taken')
    position = int(input('Please provide new position:... '))
    make_move(char, position, board, player_sign, computer_sign)


def player_turn(board, player_sign, computer_sign):
    """Allows user to choose position"""
    position = int(input('Enter next move: '))
    make_move(player_sign, position, board, player_sign, computer_sign)


def computer_turn(board, player_sign, computer_sign):
    """Allows user to choose position"""
    best_score = -1
    best_move = -1

    for key in board.keys():
        if board[key] == str(key):
            board[key] = computer_sign
            score = minimax(board, False, player_sign, computer_sign)
            board[key] = str(key)

            if score > best_score:
                best_score = score
                best_move = key

    make_move(computer_sign, best_move, board, player_sign, computer_sign)


def minimax(board, is_maximizing, player_sign, computer_sign):
    """Algorithm for next computer move"""
    if check_win(board, computer_sign):
        return 1
    if check_win(board, player_sign):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -1

        for key in board.keys():
            if board[key] == str(key):
                board[key] = computer_sign
                score = minimax(board, False, player_sign, computer_sign)
                board[key] = str(key)

                if score > best_score:
                    best_score = score

        return best_score

    best_score = 1

    for key in board.keys():
        if board[key] == str(key):
            board[key] = player_sign
            score = minimax(board, True, player_sign, computer_sign)
            board[key] = str(key)
            if score < best_score:
                best_score = score

    return best_score


def play_game(board, player_sign, computer_sign):
    """Starts game"""
    sign_p, sign_c = choose_sign(player_sign, computer_sign)
    print("Computer goes first! Good luck.")

    while not check_win(board, sign_p) or check_win(board, sign_c) or check_draw(board):
        computer_turn(game_board, sign_p, sign_c)
        player_turn(game_board, sign_p, sign_c)


play_game(game_board, PLAYER_SIGN, COMPUTER_SIGN)
