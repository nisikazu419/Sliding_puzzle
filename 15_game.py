import random
print("15-game start")
print("'0' is empty tile")
goal = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
board = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
issetup = True
count = 0
def print_board():
    for i in range(4):
        print(str(board[i][0]) + "   " + str(board[i][1]) + "   " + str(board[i][2]) + "   " + str(board[i][3]))
def find_zero(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i,j
def move_tile(direction):
    global count
    x_0,y_0 = find_zero(board)
    if(direction == "s"):
        if(x_0 == 0):
            if(issetup == False):
                print("you cannot move that direction.")
                print_board()
            return
        else:
            moved_tile = board[x_0 - 1][y_0]
            board[x_0 - 1][y_0] = board[x_0][y_0]
            board[x_0][y_0] = moved_tile
            if(issetup == False):
                print_board()
                count = count + 1
    elif(direction == "w"):
        if(x_0 == 3):
            if(issetup == False):
                print("you cannot move that direction.")
                print_board()
            return
        else:
            moved_tile = board[x_0 + 1][y_0]
            board[x_0 + 1][y_0] = board[x_0][y_0]
            board[x_0][y_0] = moved_tile
        if(issetup == False):
            print_board()
            count = count + 1
    elif(direction == "a"):
        if(y_0 == 3):
            if(issetup == False):
                print("you cannot move that direction.")
                print_board()
            return
        else:
            moved_tile = board[x_0][y_0 + 1]
            board[x_0][y_0 + 1] = board[x_0][y_0]
            board[x_0][y_0] = moved_tile
        if(issetup == False):
            print_board()
            count = count + 1
    elif(direction == "d"):
        if(y_0 == 0):
            if(issetup == False):
                print("you cannot move that direction.")
                print_board()
            return
        else:
            moved_tile = board[x_0][y_0 - 1]
            board[x_0][y_0 - 1] = board[x_0][y_0]
            board[x_0][y_0] = moved_tile
        if(issetup == False):
            print_board()
            count = count + 1
    else:
        print("please enter the collect direction.")
        print_board()
        return
def setup():
    global issetup
    while(random.randint(1,999) != 1):
        setup_wasd = random.choice(["w","a","s","d"])
        move_tile(setup_wasd)
    issetup = False
    print_board()
setup()
while(not ((goal[0][0] == board[0][0]) and (goal[0][1] == board[0][1]) and (goal[0][2] == board[0][2]) and (goal[0][3] == board[0][3]) and (goal[1][0] == board[1][0]) and (goal[1][1] == board[1][1]) and (goal[1][2] == board[1][2]) and (goal[1][3] == board[1][3]) and (goal[2][0] == board[2][0]) and (goal[2][1] == board[2][1]) and (goal[2][2] == board[2][2]) and (goal[2][3] == board[2][3]) and (goal[3][0] == board[3][0]) and (goal[3][1] == board[3][1]) and (goal[3][2] == board[3][2]) and (goal[3][3] == board[3][3]))):
    wasd = input("w,a,s or d\n")
    move_tile(wasd)
print("You cleared the 15-game! You took " + str(count) + " times to move.")