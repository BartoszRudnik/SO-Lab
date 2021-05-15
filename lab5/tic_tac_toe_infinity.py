def prepare_game_board(game_board, n):

    for i in range(n**2):
        game_board[i] = i + 1


def choose_sign(player_sign, computer_sign):

    choosen = ' '

    while choosen != 'X' and choosen != 'O':
        choosen = str(input('Choose X or O: '))

        if choosen == 'X':
            player_sign = 'X'
            computer_sign = 'O'
            return player_sign, computer_sign
        if choosen == 'O':
            player_sign = 'O'
            computer_sign = 'X'
            return player_sign, computer_sign
        else:
            print('try again')

    return


def print_game_board(game_board, n):

    count = 0

    for i in range(len(game_board)):
        if count % n == 0 and count != 0:
            print('\n------------------------------------------------')
            if(len(str(game_board[i])) == 1):
                print(str(game_board[i]) + '  |', end='')
            if(len(str(game_board[i])) == 2):
                print(str(game_board[i]) + ' |', end='')
            if(len(str(game_board[i])) == 3):
                print(str(game_board[i]) + '|', end='')
        else:
            if(len(str(game_board[i])) == 1):
                print(str(game_board[i]) + '  |', end='')
            if(len(str(game_board[i])) == 2):
                print(str(game_board[i]) + ' |', end='')
            if(len(str(game_board[i])) == 3):
                print(str(game_board[i]) + '|', end='')

        count += 1
    print('\n')


def check_if_position_free(game_board, board_position):
    if game_board[board_position] == board_position + 1:
        return True
    else:
        return False


def check_draw(game_board):
    for i in range(len(game_board)):
        if game_board[i] == i + 1:
            return False
    return True


def check_win(game_board, player_sign, n, player_pick):

    is_win = True
    for i in range(5):
        if player_pick + i < 0 or player_pick + i >= len(game_board) or game_board[player_pick + i] != player_sign:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if player_pick - i < 0 or player_pick - i >= len(game_board) or game_board[player_pick - i] != player_sign:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if player_pick + (n * i) < 0 or player_pick + (n * i) >= len(game_board) or game_board[player_pick + (n * i)] != player_sign:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if player_pick - (n * i) < 0 or player_pick - (n * i) >= len(game_board) or game_board[player_pick - (n * i)] != player_sign:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if player_pick + n * i + i  < 0 or player_pick + n * i + i >= len(game_board) or game_board[player_pick + n * i + i] != player_sign:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if player_pick - n * i - i < 0 or player_pick - n * i - i >= len(game_board) or game_board[player_pick - n * i - i] != player_sign:
            is_win = False
            break
    if is_win:
        return True

    is_win = True
    for i in range(5):
        if player_pick - n * i + i < 0 or player_pick - n * i + i >= len(game_board) or game_board[player_pick - n * i + i] != player_sign:
            is_win = False
            break
    if is_win:
        return True

    if_win = True
    for i in range(5):
        if player_pick + n * i - i < 0 or player_pick + n * i - i >= len(game_board) or game_board[player_pick + n * i - i] != player_sign:
            is_win = False
            break
        
    return is_win


def make_move(char, position, game_board, player_sign, computer_sign, n):
    if check_if_position_free(game_board, position - 1):
        game_board[position - 1] = char
        print_game_board(game_board, n)
        if(check_draw(game_board)):
            print('Draw')
            exit()
        if(check_win(game_board, computer_sign, n, position - 1)):
            print('Bot wins')
            exit()
        if(check_win(game_board, player_sign, n, position - 1)):
            print('Player wins')
            exit()

        return

    else:
        if char == computer_sign:
            computer_turn(game_board, player_sign, computer_sign, n, -1, position - 1)
        else:
            print('This position is already taken')
            position = int(input('Please provide new position:... '))
            make_move(char, position, game_board, player_sign, computer_sign, n)

        return


def player_turn(game_board, player_sign, computer_sign, n):
    position = int(input('Enter next move: '))
    make_move(player_sign, position, game_board, player_sign, computer_sign, n)

    return position - 1


def computer_turn(game_board, player_sign, computer_sign, n, computer_position, player_position):
    best_move = -1

    direction, player_points = computer_defend(
        game_board, player_sign, n, player_position)

    best_move = deffensive_move(
        game_board, player_sign, computer_sign, n, player_position, direction)

    print(best_move + 1)

    make_move(computer_sign, best_move + 1, game_board,
              player_sign, computer_sign, n)
    return best_move


def deffensive_move(game_board, player_sign, computer_sign, n, player_position, direction):

    if direction == 1:
        index = 1
        while player_position - index * n - index >= 0 and player_position - index * n - index < len(game_board):
            if game_board[player_position - index * n - index] != player_sign and game_board[player_position - index * n - index] != computer_sign:                
                return player_position - index * n - index
            index += 1

        index = 1
        while player_position + index * n + index >= 0 and player_position + index * n + index < len(game_board):
            if game_board[player_position + index * n + index] != player_sign and game_board[player_position + index * n + index] != computer_sign:               
                return player_position + index * n + index
            index += 1

    if direction == 2:
        index = 1
        while player_position - n * index >= 0 and player_position - n * index < len(game_board):
            if game_board[player_position - n * index] != player_sign and game_board[player_position - n * index] != computer_sign:
                print(player_position - n * index)
                return player_position - n * index
            index += 1

        index = 1
        while player_position + n * index >= 0 and player_position + n * index < len(game_board):
            if game_board[player_position + n * index] != player_sign and game_board[player_position + n * index] != computer_sign:
                print(player_position + n * index)
                return player_position + n * index
            index += 1

    if direction == 3:
        index = 1
        while player_position - n * index + index >= 0 and player_position - n * index + index < len(game_board):
            if game_board[player_position - n * index + index] != player_sign and game_board[player_position - n * index + index] != computer_sign:
                return player_position - n * index + index
            index += 1

        index = 1
        while player_position + n * index - index >= 0 and player_position + n * index - index < len(game_board):
            if game_board[player_position + n * index - index] != player_sign and game_board[player_position + n * index - index] != computer_sign:
                return player_position + n * index - index
            index += 1

    if direction == 4:
        index = 1
        while player_position + index >= 0 and player_position + index < len(game_board):
            if game_board[player_position + index] != player_sign and game_board[player_position] != computer_sign:
                return player_position + index
            index += 1

        index = 1
        while player_position - index >= 0 and player_position - index < len(game_board):
            if game_board[player_position - index] != player_sign and game_board[player_position] != computer_sign:
                return player_position - index
            index += 1

    if direction == 5:
        index = 1
        while player_position + index * n + index >= 0 and player_position + index * n + index < len(game_board):
            if game_board[player_position + index * n + index] != player_sign and game_board[player_position + index * n + index] != computer_sign:
                return player_position + index * n + index
            index += 1

        index = 1
        while player_position - index * n - index >= 0 and player_position - index * n - index < len(game_board):
            if game_board[player_position - index * n - index] != player_sign and game_board[player_position - index * n - index] != computer_sign:
                return player_position - index * n - index
            index += 1

    if direction == 6:
        index = 1
        while player_position + n * index >= 0 and player_position + n * index < len(game_board):
            if game_board[player_position + n * index] != player_sign and game_board[player_position + n * index] != computer_sign:
                return player_position + n * index
            index += 1

        index = 1
        while player_position - n * index >= 0 and player_position - n * index < len(game_board):
            if game_board[player_position - n * index] != player_sign and game_board[player_position - n * index] != computer_sign:
                return player_position - n * index
            index += 1

    if direction == 7:
        index = 1
        while player_position + n * index - index >= 0 and player_position + n * index - index < len(game_board):
            if game_board[player_position + n * index - index] != player_sign and game_board[player_position + n * index - index] != computer_sign:
                return player_position + n * index - index
            index += 1

        index = 1
        while player_position - n * index + index >= 0 and player_position - n * index + index < len(game_board):
            if game_board[player_position - n * index + index] != player_sign and game_board[player_position - n * index + index] != computer_sign:
                return player_position - n * index + index
            index += 1

    if direction == 8:
        index = 1
        while player_position - index >= 0 and player_position - index < len(game_board):
            if game_board[player_position - index] != player_sign and game_board[player_position] != computer_sign:
                return player_position - index
            index += 1

        index = 1
        while player_position + index >= 0 and player_position + index < len(game_board):
            if game_board[player_position + index] != player_sign and game_board[player_position] != computer_sign:
                return player_position + index
            index += 1


def computer_defend(game_board, player_sign, n, player_position):

    count_5 = 0
    for i in range(1, 5):
        if player_position - i * n - i >= 0 and player_position - i * n - i < len(game_board):
            if game_board[player_position - i * n - 1] == player_sign:
                count_5 += 1

    count_6 = 0
    for i in range(1, 5):
        if player_position - i * n >= 0 and player_position - i * n < len(game_board):
            if game_board[player_position - i * n] == player_sign:
                count_6 += 1

    count_7 = 0
    for i in range(1, 5):
        if player_position - i * n + 1 >= 0 and player_position - i * n + 1 < len(game_board):
            if game_board[player_position - i * n + 1] == player_sign:
                count_7 += 1

    count_8 = 0
    for i in range(1, 5):
        if player_position + i >= 0 and player_position + i < len(game_board):
            if game_board[player_position + i] == player_sign:
                count_8 += 1

    count_1 = 0
    for i in range(1, 5):
        if player_position + i * n + 1 >= 0 and player_position + i * n + 1 < len(game_board):
            if game_board[player_position + i * n + 1] == player_sign:
                count_1 += 1

    count_2 = 0
    for i in range(1, 5):
        if player_position + i * n >= 0 and player_position + i * n < len(game_board):
            if game_board[player_position + i * n] == player_sign:
                count_2 += 1

    count_3 = 0
    for i in range(1, 5):
        if player_position + i * n - i >= 0 and player_position + i * n - i < len(game_board):
            if game_board[player_position + i * n - i] == player_sign:
                count_3 += 1

    count_4 = 0
    for i in range(1, 5):
        if player_position - i >= 0 and player_position - i < len(game_board):
            if game_board[player_position - i] == player_sign:
                count_4 += 1

    scores = [count_1, count_2, count_3, count_4,
              count_5, count_6, count_7, count_8]

    max_index = 1
    max_score = 0

    for i in range(1, len(scores) + 1):
        if scores[i - 1] > max_score:
            max_score = scores[i - 1]
            max_index = i

    return max_index, max_score


def play_game(game_board, player_sign, computer_sign, n):
    player_sign, computer_sign = choose_sign(player_sign, computer_sign)
    print("Computer goes first! Good luck.")

    prepare_game_board(game_board, n)
    print_game_board(game_board, n)

    computer_position = randint(0, n - 1)
    player_position = randint(0, n - 1)

    while True:
        computer_position = computer_turn(
            game_board, player_sign, computer_sign, n, computer_position, player_position)
        player_position = player_turn(
            game_board, player_sign, computer_sign, n)


def randint(a, b):
    return a + randbelow(b - a + 1)


def randbelow(n):
    if n <= 0:
        raise ValueError
    k = n.bit_length()
    numbytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(numbytes), 'big')
        r >>= numbytes * 8 - k
        if r < n:
            return r


def random_bytes(n):
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)


game_board = [0 for x in range(12**2)]
player_sign = 'O'
computer_sign = 'X'

play_game(game_board, player_sign, computer_sign, 12)
