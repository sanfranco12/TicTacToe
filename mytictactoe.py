from ast import For
from secrets import choice
import colorama 
from colorama import Fore
colorama.init()
def main():
    player = next_player("")
    boardx3 = create_boardx3()
    boardx4 = create_boardx4()
    boardx5 = create_boardx5()
    print()

    display_to_use = input("What board\'s size would you like to use? 3x3 / 4x4 / 5x5, please enter a number 3, 4 or 5: ")
    if display_to_use == "3":
        while not (has_a_winnerx3(boardx3) or is_a_drawx3(boardx3)): 
            print() 
            display_boardx3(boardx3)
            make_movex3(player,boardx3)
            player = next_player(player)
        display_boardx3(boardx3)
        print("Good game. Thanks for playing!") 
    elif display_to_use == "4":
        print()
        while not (has_a_winnerx4(boardx4) or is_a_drawx4(boardx4)):
            display_boardx4(boardx4)
            make_movex4(player, boardx4)
            player = next_player(player)
        display_boardx4(boardx4)
        print("Good game. Thanks for playing!") 
    elif display_to_use == "5":
        print()
        while not (has_a_winnerx5(boardx5) or is_a_drawx5(boardx5)):
            display_boardx5(boardx5)
            make_movex5(player, boardx5)
            player = next_player(player)
        display_boardx5(boardx5)
        print("Good game. Thanks for playing!") 
        
def create_boardx3():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def create_boardx4():
    board = []
    for square in range(16):
        board.append(square + 1)
    return board          

def create_boardx5():
    board = []
    for square in range(25):
        board.append(square + 1)
    return board

def display_boardx3(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-----")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-----")
    print(f"{board[6]}|{board[7]}|{board[8]}")

def display_boardx4(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}|{board[3]}")
    print("-----------")
    print(f"{board[4]}|{board[5]}|{board[6]}|{board[7]}")
    print("-----------")
    print(f"{board[8]}|{board[9]}|{board[10]}|{board[11]}")
    print("-----------")
    print(f"{board[12]}|{board[13]}|{board[14]}|{board[15]}")
    print()

def display_boardx5(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}|{board[3]}|{board[4]}")
    print("-----------")
    print(f"{board[5]}|{board[6]}|{board[7]}|{board[8]}|{board[9]}")
    print("-----------")
    print(f"{board[10]}|{board[11]}|{board[12]}|{board[13]}|{board[14]}")
    print("-----------")
    print(f"{board[15]}|{board[16]}|{board[17]}|{board[18]}|{board[19]}")
    print("-----------")
    print(f"{board[20]}|{board[21]}|{board[22]}|{board[23]}|{board[24]}")
    print()
    
def is_a_drawx3(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def is_a_drawx4(board):
    for square in range(16):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def is_a_drawx5(board):
    for square in range(25):
        if board[square] != "x" and board[square] != "o":
            return False
    return True

def has_a_winnerx3(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
    
def has_a_winnerx4(board):
    return (board[0] == board[1] == board[2] or
            board[1] == board[2] == board[3] or
            board[4] == board[5] == board[6] or
            board[5] == board[6] == board[7] or
            board[8] == board[9] == board[10] or
            board[9] == board[10] == board[11] or
            board[12] == board[13] == board[14] or
            board[8] == board[5] == board[2] or
            board[12] == board[9] == board[6] or
            board[9] == board[6] == board[3] or
            board[13] == board[10] == board[7] or
            board[1] == board[6] == board[11] or
            board[0] == board[5] == board[10] or
            board[4] == board[9] == board[14] or
            board[5] == board[10] == board[15] or
            board[0] == board[4] == board[8] or
            board[4] == board[8] == board[12] or
            board[1] == board[5] == board[9] or
            board[5] == board[9] == board[13] or
            board[2] == board[6] == board[10] or
            board[6] == board[10] == board[14] or
            board[3] == board[7] == board[11] or
            board[7] == board[11] == board[15])
    
def has_a_winnerx5(board):
    return (board[0] == board[1] == board[2] or
            board[1] == board[2] == board[3] or
            board[2] == board[3] == board[4] or
            board[5] == board[6] == board[7] or
            board[6] == board[7] == board[8] or
            board[7] == board[8] == board[9] or
            board[10] == board[11] == board[12] or
            board[11] == board[12] == board[13] or
            board[12] == board[13] == board[14] or
            board[15] == board[16] == board[17] or
            board[16] == board[17] == board[18] or
            board[17] == board[18] == board[19] or
            board[20] == board[21] == board[22] or
            board[21] == board[22] == board[23] or
            board[22] == board[23] == board[24] or
            board[0] == board[5] == board[10] or
            board[5] == board[10] == board[15] or
            board[10] == board[15] == board[20] or
            board[1] == board[6] == board[11] or
            board[6] == board[11] == board[16] or
            board[11] == board[16] == board[21] or
            board[2] == board[7] == board[12] or
            board[7] == board[12] == board[17] or
            board[12] == board[17] == board[22] or
            board[3] == board[8] == board[13] or
            board[8] == board[13] == board[18] or
            board[13] == board[18] == board[23] or
            board[4] == board[9] == board[14] or
            board[9] == board[14] == board[19] or
            board[14] == board[19] == board[24] or
            board[2] == board[8] == board[14] or
            board[1] == board[7] == board[13] or
            board[7] == board[13] == board[19] or
            board[0] == board[6] == board[12] or
            board[6] == board[12] == board[18] or
            board[12] == board[18] == board[24] or
            board[5] == board[11] == board[17] or
            board[11] == board[17] == board[23] or
            board[10] == board[16] == board[22] or
            board[10] == board[6] == board[2] or
            board[15] == board[11] == board[7] or
            board[11] == board[7] == board[3] or
            board[4] == board[8] == board[12] or
            board[8] == board[12] == board[16] or
            board[12] == board[16] == board[20] or
            board[9] == board[13] == board[17] or
            board[13] == board[17] == board[21] or
            board[14] == board[18] == board[22])

def colors(player):
    if player == "x":
        turn = int(input(Fore.BLUE + f"{player}'s turn to choose a square: "))
        return turn
    else:
        turn = int(input(Fore.RED + f"{player}'s turn to choose a square: "))      
        return turn
    
def make_movex3(player, board):
    square = colors(player)
    board[square - 1] = player
    
    
def make_movex4(player, board):
    square = colors(player)
    board[square - 1] = player
    
def make_movex5(player, board):
    square = colors(player)
    board[square - 1] = player
    
def next_player(current):
    x = "x"
    o = "o"
    if current == "" or current == "o":
        return x
    elif current == "x":
        return o
    
if __name__ == "__main__":
    main()
