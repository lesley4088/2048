from utilities import generate_piece, print_board

DEV_MODE = False

def move_a(game_board):
    for i in range(4):
        lst = []
        for j in range(4):
            if game_board[i][j] != 0:
               lst.append(game_board[i][j])
        while len(lst) < 4:
            lst.append(0)

        game_board[i] = lst

        for j in range(4):
            game_board[i][j] = int(game_board[i][j])

        if game_board[i][0] == game_board[i][1]:
            game_board[i][0] *= 2
            game_board[i][1] = 0
            if game_board[i][2] == game_board[i][3]:
                game_board[i][2] *= 2
                game_board[i][3] = 0
        elif game_board[i][1] == game_board[i][2]:
            game_board[i][1] *= 2
            game_board[i][2] = 0
        elif game_board[i][2] == game_board[i][3]:
            game_board[i][2] *= 2
            game_board[i][3] = 0

        lst = []
        for j in range(4):
            if game_board[i][j] != 0:
                lst.append(game_board[i][j])
        while len(lst) < 4:
            lst.append(0)

        game_board[i] = lst

def move_d(game_board):
    for i in range(4):
        lst = []
        for j in range(4):
            if game_board[i][j] != 0:
                lst.append(game_board[i][j])
        if len(lst) < 4:
            lst.reverse()
            while len(lst) < 4:
                lst.append(0)
            lst.reverse()

        game_board[i] = lst

        if game_board[i][3] == game_board[i][2]:
            game_board[i][3] *= 2
            game_board[i][2] = 0
            if game_board[i][1] == game_board[i][0]:
                game_board[i][1] *= 2
                game_board[i][0] = 0
        elif game_board[i][2] == game_board[i][1]:
            game_board[i][2] *= 2
            game_board[i][1] = 0
        elif game_board[i][1] == game_board[i][0]:
            game_board[i][1] *= 2
            game_board[i][0] = 0

        lst = []
        for j in range(4):
            if game_board[i][j] != 0:
                lst.append(game_board[i][j])
        if len(lst) < 4:
            lst.reverse()
            while len(lst) < 4:
                lst.append(0)
            lst.reverse()

        game_board[i] = lst

def move_w(game_board):
    for i in range(4):
        lst = []

        for j in range(4):
            if game_board[j][i] != 0:
                lst.append(game_board[j][i])

        while len(lst) < 4:
            lst.append(0)

        for j in range(4):
            game_board[j][i] = lst[j]

        if game_board[0][i] == game_board[1][i]:
            game_board[0][i] *= 2
            game_board[1][i] = 0
            if game_board[2][i] == game_board[3][i]:
                game_board[2][i] *= 2
                game_board[3][i] = 0
        elif game_board[1][i] == game_board[2][i]:
            game_board[1][i] *= 2
            game_board[2][i] = 0
        elif game_board[2][i] == game_board[3][i]:
            game_board[2][i] *= 2
            game_board[3][i] = 0

        lst = []

        for j in range(4):
            if game_board[j][i] != 0:
                lst.append(game_board[j][i])

        while len(lst) < 4:
            lst.append(0)

        for j in range(4):
            game_board[j][i] = lst[j]



def move_s(game_board):
    for i in range(4):
        lst = []
        for j in range(4):
            if game_board[j][i] != 0:
                lst.append(game_board[j][i])
        if len(lst) < 4:
            lst.reverse()
            while len(lst) < 4:
                lst.append(0)
            lst.reverse()

        for j in range(4):
            game_board[j][i] = lst[j]


        if game_board[3][i] == game_board[2][i]:
            game_board[3][i] *= 2
            game_board[2][i] = 0
            if game_board[1][i] == game_board[0][i]:
                game_board[1][i] *= 2
                game_board[0][i] = 0
        elif game_board[2][i] == game_board[1][i]:
            game_board[2][i] *= 2
            game_board[1][i] = 0
        elif game_board[1][i] == game_board[0][i]:
            game_board[1][i] *= 2
            game_board[0][i] = 0

        lst = []
        for j in range(4):
            if game_board[j][i] != 0:
                lst.append(game_board[j][i])
        if len(lst) < 4:
            lst.reverse()
            while len(lst) < 4:
                lst.append(0)
            lst.reverse()

        for j in range(4):
            game_board[j][i] = lst[j]
def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    available_space = 16
    num_of_2048 = 0

    for element in game_board:
        for value in element:
            if value != 0:
                available_space -= 1
            elif value == 2048:
                num_of_2048 += 1

    if available_space == 0 or num_of_2048 != 0:
        return True
    else:
        return False


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    for i in range(2):
        cell_index = generate_piece(board)
        board[cell_index['row']][cell_index['column']] = cell_index['value']

    print_board(board)

    while game_over(board) != True:
        move_direction = input()

        while move_direction not in ['a', 'd', 'w', 's', 'q']:
            move_direction = input()

        if move_direction == 'q':
            print("Goodbye")
            return board
        elif move_direction == 'a':
            move_a(board)
        elif move_direction == 'd':
            move_d(board)
        elif move_direction == 'w':
            move_w(board)
        elif move_direction == 's':
            move_s(board)

        if game_over(board) == True:
            break
        else:
            update_index = generate_piece(board)
            board[update_index['row']][update_index['column']] = update_index['value']
            print_board(board)

    for element in game_board:
        if 2048 in element:
            print("win")
            return game_board
    print("lose")
    return game_board



if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
