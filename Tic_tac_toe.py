from time import sleep
from random import randint

r = "\033[0;31m"
g = "\033[0;32m"
y = "\033[0;33m"
b = "\033[0;34m"
ce = "\033[m"

board = ["=", "=", "=",
         "=", "=", "=",
         "=", "=", "="]

game_over = True
player = "X"
winner = None
robot = "O"

def game():
    show_board()

    while game_over:
        play(player)

        ai_play()

        check_if_game_over()

    sleep(0.5)
    if winner == "X":
        print(f"{b}Congrats {player}, you won{ce}")
    elif winner == "O":
        print(f"{r}Looks like the {robot} won{ce}")
    else:
        print(f"{y}Tie. Try again{ce}")


def show_board():
    print(f"{board[0]} / {board[1]} / {board[2]}")
    print(f"{board[3]} / {board[4]} / {board[5]}")
    print(f"{board[6]} / {board[7]} / {board[8]}")

# Asking for a position on the board
def play(current_player):
    print(f"{g}It's {current_player}'s turn{ce}")
    sleep(0.5)
    # Check if every information is right
    valid = False
    while not valid:

        while True:
            # Check for a real position
            while True:
                # Check if the awnser is a number
                try:
                    play = int(input(f"{g}Chosse a position between 1 - 9: {ce}"))
                except:
                    print(f"{r}Type a number{ce}")
                else:
                    break
            
            if play > len(board):
                print(f"{r}Try a number between 1 - 9{ce}")
            else:
                break

        play -= 1
        # Check if the position is avaliable
        if board[play] != '=':
            print(f"{r}Position already taken by {board[play]}. Try again{ce}")
        else:
            valid = True
    # Put a X or O in the board
    board[play] = player

    show_board()
    sleep(0.5)


def check_if_game_over():
    check_win()
    check_tie()


def check_win():
    global winner
    row_win = check_row()
    collumn_win = check_collum()
    diagonal_win = check_diagonal()
    if row_win:
        winner = row_win
    elif collumn_win:
        winner = collumn_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None


def check_row():
    global game_over
    row_1 = board[0] == board[1] == board[2] != "="
    row_2 = board[3] == board[4] == board[5] != "="
    row_3 = board[6] == board[7] == board[8] != "="
    if row_1 or row_2 or row_3:
        game_over = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[5]
    else:
        return None


def check_collum():
    global game_over
    collumn_1 = board[0] == board[3] == board[6] != "="
    collumn_2 = board[1] == board[4] == board[7] != "="
    collumn_3 = board[2] == board[5] == board[8] != "="
    if collumn_1 or collumn_2 or collumn_3:
        game_over = False
    if collumn_1:
        return board[0]
    elif collumn_2:
        return board[1]
    elif collumn_3:
        return board[2]
    else:
        return None


def check_diagonal():
    global game_over
    diagonal_1 = board[0] == board[4] == board[8] != "="
    diagonal_2 = board[2] == board[4] == board[6] != "="
    if diagonal_1 or diagonal_2:
        game_over = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    else:
        return None


def check_tie():
    global game_over
    if "=" not in board:
        game_over = False
        return True
    else:
        return False


def ai_play():
    print(f"{g}Its O's turn{ce}")
    while True:
        ai = randint(0, 8)
        
        ai -= 1
        
        if not "=" in board:
            break

        if board[ai] == "=":
            board[ai] = robot
            break

    show_board()
    sleep(0.5)


game()