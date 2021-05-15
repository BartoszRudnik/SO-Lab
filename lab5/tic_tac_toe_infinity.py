"""Tic Tac Toe bigger board"""

import sys

def prepare_game_board(board, number):
    """Prepares game board"""
    for i in range(number**2):
        board[i] = i + 1


def choose_sign(player, computer):
    """Allows user to choose 'X' or 'O' """
    choosen = ' '

    while choosen not in ('X', 'O'):
        choosen = str(input('Choose X or O: '))

        if choosen == 'X':
            player = 'X'
            computer = 'O'
            return player, computer
        if choosen == 'O':
            player = 'O'
            computer = 'X'
            return player, computer
        print('try again')


def print_game_board(board, number):
    """Prints game board"""
    count = 0

    for i in range(len(board)):
        if count % number == 0 and count != 0:
            print('\n------------------------------------------------')
            if len(str(board[i])) == 1:
                print(str(board[i]) + '  |', end='')
            if len(str(board[i])) == 2:
                print(str(board[i]) + ' |', end='')
            if len(str(board[i])) == 3:
                print(str(board[i]) + '|', end='')
        else:
            if len(str(board[i])) == 1:
                print(str(board[i]) + '  |', end='')
            if len(str(board[i])) == 2:
                print(str(board[i]) + ' |', end='')
            if len(str(board[i])) == 3:
                print(str(board[i]) + '|', end='')

        count += 1
    print('\n')


def check_if_position_free(board, board_position):
    """Checks if choosen position is free"""
    return bool(board[board_position] == board_position + 1)


def check_draw(board):
    """Checks if game is draw"""
    for i in range(len(board)):
        if board[i] == i + 1:
            return False
    return True


def check_win(boa, sig, num, pic):
    """Checks if game is won"""
    is_win = True
    for i in range(5):
        if pic + i < 0 or pic + i >= len(boa) or boa[pic + i] != sig:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if pic - i < 0 or pic - i >= len(boa) or boa[pic - i] != sig:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if pic + (num * i) < 0 or pic + (num * i) >= len(boa) or boa[pic + (num * i)] != sig:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if pic - (num * i) < 0 or pic - (num * i) >= len(boa) or boa[pic - (num * i)] != sig:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if pic + num * i + i < 0 or pic + num * i + i >= len(boa) or boa[pic + num * i + i] != sig:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if pic - num * i - i < 0 or pic - num * i - i >= len(boa) or boa[pic - num * i - i] != sig:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if pic - num * i + i < 0 or pic - num * i + i >= len(boa) or boa[pic - num * i + i] != sig:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if pic + num * i - i < 0 or pic + num * i - i >= len(boa) or boa[pic + num * i - i] != sig:
            is_win = False
            break

    return is_win


def make_move(char, position, board, player, computer, num):
    """Assign player sign to choosen position"""
    if check_if_position_free(board, position - 1):
        board[position - 1] = char
        print_game_board(board, num)
        if check_draw(board):
            print('Draw')
            sys.exit()
        if check_win(board, computer, num, position - 1):
            print('Bot wins')
            sys.exit()
        if check_win(board, player, num, position - 1):
            print('Player wins')
            sys.exit()

        return

    if char == computer:
        computer_turn(board, player,
                      computer, num, position - 1)
    else:
        print('This position is already taken')
        position = int(input('Please provide new position:... '))
        make_move(char, position, board,
                  player, computer, num)


def player_turn(board, player, computer, num):
    """Allows player to make move"""
    position = int(input('Enter next move: '))
    make_move(player, position, board, player, computer, num)

    return position - 1


def computer_turn(board, player, computer, num, player_position):
    """Allows computer to make move"""
    best_move = -1

    direction = computer_defend(
        board, player, num, player_position)

    best_move = deffensive_move(
        board, player, computer, num, player_position, direction)

    print(best_move + 1)

    make_move(computer, best_move + 1, board,
              player, computer, num)
    return best_move


def deffensive_move(board, pla, com, num, pos, direction):
    """Computer algorithm to choose next move"""
    if direction == 1:
        index = 1
        while pos - index * num - index >= 0 and pos - index * num - index < len(board):
            if board[pos - index * num - index] != pla and board[pos - index * num - index] != com:
                return pos - index * num - index
            index += 1

        index = 1
        while pos + index * num + index >= 0 and pos + index * num + index < len(board):
            if board[pos + index * num + index] != pla and board[pos + index * num + index] != com:
                return pos + index * num + index
            index += 1

    if direction == 2:
        index = 1
        while pos - num * index >= 0 and pos - num * index < len(board):
            if board[pos - num * index] != pla and board[pos - num * index] != com:
                return pos - num * index
            index += 1

        index = 1
        while pos + num * index >= 0 and pos + num * index < len(board):
            if board[pos + num * index] != pla and board[pos + num * index] != com:
                return pos + num * index
            index += 1

    if direction == 3:
        index = 1
        while pos - num * index + index >= 0 and pos - num * index + index < len(board):
            if board[pos - num * index + index] != pla and board[pos - num * index + index] != com:
                return pos - num * index + index
            index += 1

        index = 1
        while pos + num * index - index >= 0 and pos + num * index - index < len(board):
            if board[pos + num * index - index] != pla and board[pos + num * index - index] != com:
                return pos + num * index - index
            index += 1

    if direction == 4:
        index = 1
        while pos + index >= 0 and pos + index < len(board):
            if board[pos + index] != pla and board[pos] != com:
                return pos + index
            index += 1

        index = 1
        while pos - index >= 0 and pos - index < len(board):
            if board[pos - index] != pla and board[pos] != com:
                return pos - index
            index += 1

    if direction == 5:
        index = 1
        while pos + index * num + index >= 0 and pos + index * num + index < len(board):
            if board[pos + index * num + index] != pla and board[pos + index * num + index] != com:
                return pos + index * num + index
            index += 1

        index = 1
        while pos - index * num - index >= 0 and pos - index * num - index < len(board):
            if board[pos - index * num - index] != pla and board[pos - index * num - index] != com:
                return pos - index * num - index
            index += 1

    if direction == 6:
        index = 1
        while pos + num * index >= 0 and pos + num * index < len(board):
            if board[pos + num * index] != pla and board[pos + num * index] != com:
                return pos + num * index
            index += 1

        index = 1
        while pos - num * index >= 0 and pos - num * index < len(board):
            if board[pos - num * index] != pla and board[pos - num * index] != com:
                return pos - num * index
            index += 1

    if direction == 7:
        index = 1
        while pos + num * index - index >= 0 and pos + num * index - index < len(board):
            if board[pos + num * index - index] != pla and board[pos + num * index - index] != com:
                return pos + num * index - index
            index += 1

        index = 1
        while pos - num * index + index >= 0 and pos - num * index + index < len(board):
            if board[pos - num * index + index] != pla and board[pos - num * index + index] != com:
                return pos - num * index + index
            index += 1

    if direction == 8:
        index = 1
        while pos - index >= 0 and pos - index < len(board):
            if board[pos - index] != pla and board[pos] != com:
                return pos - index
            index += 1

        index = 1
        while pos + index >= 0 and pos + index < len(board):
            if board[pos + index] != pla and board[pos] != com:
                return pos + index
            index += 1

    return -1


def computer_defend(board, player, num, player_position):
    """Algorithm to check player moves"""
    count_5 = 0
    for i in range(1, 5):
        if player_position - i * num - i >= 0 and player_position - i * num - i < len(board):
            if board[player_position - i * num - 1] == player:
                count_5 += 1

    count_6 = 0
    for i in range(1, 5):
        if player_position - i * num >= 0 and player_position - i * num < len(board):
            if board[player_position - i * num] == player:
                count_6 += 1

    count_7 = 0
    for i in range(1, 5):
        if player_position - i * num + 1 >= 0 and player_position - i * num + 1 < len(board):
            if board[player_position - i * num + 1] == player:
                count_7 += 1

    count_8 = 0
    for i in range(1, 5):
        if player_position + i >= 0 and player_position + i < len(board):
            if board[player_position + i] == player:
                count_8 += 1

    count_1 = 0
    for i in range(1, 5):
        if player_position + i * num + 1 >= 0 and player_position + i * num + 1 < len(board):
            if board[player_position + i * num + 1] == player:
                count_1 += 1

    count_2 = 0
    for i in range(1, 5):
        if player_position + i * num >= 0 and player_position + i * num < len(board):
            if board[player_position + i * num] == player:
                count_2 += 1

    count_3 = 0
    for i in range(1, 5):
        if player_position + i * num - i >= 0 and player_position + i * num - i < len(board):
            if board[player_position + i * num - i] == player:
                count_3 += 1

    count_4 = 0
    for i in range(1, 5):
        if player_position - i >= 0 and player_position - i < len(board):
            if board[player_position - i] == player:
                count_4 += 1

    scores = [count_1, count_2, count_3, count_4,
              count_5, count_6, count_7, count_8]

    max_index = 1
    max_score = 0

    for i in range(1, len(scores) + 1):
        if scores[i - 1] > max_score:
            max_score = scores[i - 1]
            max_index = i

    return max_index


def play_game(board, player, computer, number):
    """Start game"""
    player, computer = choose_sign(player, computer)
    print("Computer goes first! Good luck.")

    prepare_game_board(board, number)
    print_game_board(board, number)

    player_position = randint(0, number - 1)

    while True:
        computer_turn(
            board, player, computer, number, player_position)
        player_position = player_turn(
            board, player, computer, number)


def randint(number_a, number_b):
    """Function to generate int number from range (a,b)"""
    return number_a + randbelow(number_b - number_a + 1)


def randbelow(number):
    """Generate rand from range"""
    if number <= 0:
        raise ValueError
    key = number.bit_length()
    numbytes = (key + 7) // 8
    while True:
        rando = int.from_bytes(random_bytes(numbytes), 'big')
        rando >>= numbytes * 8 - key
        if rando < number:
            return rando


def random_bytes(number):
    """Generate random bytes"""
    with open('/dev/urandom', 'rb') as file:
        return file.read(number)


game_board = [0 for x in range(12**2)]
PLAYER_SIGN = 'O'
COMPUTER_SIGN = 'X'

play_game(game_board, PLAYER_SIGN, COMPUTER_SIGN, 12)
