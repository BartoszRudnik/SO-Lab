game_board = {1: '1', 2: '2', 3: '3', 4: '4',
              5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

PLAYER_SIGN = 'O'
COMPUTER_SIGN = 'X'


def choose_sign(player_sign, computer_sign):
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


def print_game_board(game_board):
    print(game_board[1] + '|' + game_board[2] + '|' + game_board[3])
    print('------')
    print(game_board[4] + '|' + game_board[5] + '|' + game_board[6])
    print('------')
    print(game_board[7] + '|' + game_board[8] + '|' + game_board[9])
    print('\n')


def check_if_position_free(game_board, board_position):
    return bool(game_board[board_position])

    if game_board[board_position] == str(board_position):
        return True
    else:
        return False


def check_draw(game_board):
    for key in game_board.keys():
        if game_board[key] == str(key):
            return False
    return True


def check_win(game_board, sign):
    if game_board[1] == game_board[2] and game_board[2] == game_board[3] and game_board[1] == sign:
        return True
    if game_board[4] == game_board[5] and game_board[5] == game_board[6] and game_board[4] == sign:
        return True
    if game_board[7] == game_board[8] and game_board[8] == game_board[9] and game_board[7] == sign:
        return True
    if game_board[1] == game_board[4] and game_board[4] == game_board[7] and game_board[1] == sign:
        return True
    if game_board[2] == game_board[5] and game_board[5] == game_board[8] and game_board[2] == sign:
        return True
    if game_board[3] == game_board[6] and game_board[6] == game_board[9] and game_board[3] == sign:
        return True
    if game_board[1] == game_board[5] and game_board[5] == game_board[9] and game_board[1] == sign:
        return True
    if game_board[3] == game_board[5] and game_board[5] == game_board[7] and game_board[3] == sign:
        return True
    else:
        return False


def make_move(char, position, game_board, player_sign, computer_sign):
    if check_if_position_free(game_board, position):
        game_board[position] = char
        print_game_board(game_board)
        if check_draw(game_board):
            print('Draw')
            exit()
        if check_win(game_board, computer_sign):
            print('Bot wins')
            exit()
        if check_win(game_board, player_sign):
            print('Player wins')
            exit()

        return

    else:
        print('This position is already taken')
        position = int(input('Please provide new position:... '))
        make_move(char, position, game_board, player_sign, computer_sign)

        return


def player_turn(game_board, player_sign, computer_sign):
    position = int(input('Enter next move: '))
    make_move(player_sign, position, game_board, player_sign, computer_sign)
    return


def computer_turn(game_board, player_sign, computer_sign):
    best_score = -1
    best_move = -1

    for key in game_board.keys():
        if game_board[key] == str(key):
            game_board[key] = computer_sign
            score = minimax(game_board, False, player_sign, computer_sign)
            game_board[key] = str(key)

            if score > best_score:
                best_score = score
                best_move = key

    make_move(computer_sign, best_move, game_board, player_sign, computer_sign)

    return


def minimax(game_board, isMaximizing, player_sign, computer_sign):
    if check_win(game_board, computer_sign):
        return 1
    if check_win(game_board, player_sign):
        return -1
    if check_draw(game_board):
        return 0

    if isMaximizing:
        best_score = -1

        for key in game_board.keys():
            if game_board[key] == str(key):
                game_board[key] = computer_sign
                score = minimax(game_board, False, player_sign, computer_sign)
                game_board[key] = str(key)

                if score > best_score:
                    best_score = score

        return best_score
    else:
        best_score = 1

        for key in game_board.keys():
            if game_board[key] == str(key):
                game_board[key] = player_sign
                score = minimax(game_board, True, player_sign, computer_sign)
                game_board[key] = str(key)
                if score < best_score:
                    best_score = score

        return best_score


def play_game(board, player_sign, computer_sign):
    sign_p, sign_c = choose_sign(player_sign, computer_sign)
    print("Computer goes first! Good luck.")

    while not check_win(board, sign_p) or check_win(board, sign_c) or check_draw(board):
        computer_turn(game_board, player_sign, computer_sign)
        player_turn(game_board, player_sign, computer_sign)


play_game(game_board, PLAYER_SIGN, COMPUTER_SIGN)
