import heapq
import random
goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
def manhattan_distance(board):
    distance = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                target_x = (board[i][j] - 1) // 4
                target_y = (board[i][j] - 1) % 4
                distance += abs(i - target_x) + abs(j - target_y)
    return distance
def find_zero(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return i, j
def move_tile(board, direction):
    x_0, y_0 = find_zero(board)
    new_board = [row[:] for row in board]
    if direction == "s" and x_0 > 0:
        new_board[x_0][y_0], new_board[x_0 - 1][y_0] = new_board[x_0 - 1][y_0], new_board[x_0][y_0]
    elif direction == "w" and x_0 < 3:
        new_board[x_0][y_0], new_board[x_0 + 1][y_0] = new_board[x_0 + 1][y_0], new_board[x_0][y_0]
    elif direction == "a" and y_0 < 3:
        new_board[x_0][y_0], new_board[x_0][y_0 + 1] = new_board[x_0][y_0 + 1], new_board[x_0][y_0]
    elif direction == "d" and y_0 > 0:
        new_board[x_0][y_0], new_board[x_0][y_0 - 1] = new_board[x_0][y_0 - 1], new_board[x_0][y_0]
    return new_board
def solve_15_puzzle(board):
    def board_to_tuple(board):au
        return tuple(tuple(row) for row in board)
    def is_solvable(board):
        inversion_count = 0
        flat_board = [tile for row in board for tile in row if tile != 0]
        for i in range(len(flat_board)):
            for j in range(i + 1, len(flat_board)):
                if flat_board[i] > flat_board[j]:
                    inversion_count += 1
        return inversion_count % 2 == 0
    if not is_solvable(board):
        return None, None
    open_list = []
    heapq.heappush(open_list, (manhattan_distance(board), 0, board, []))
    closed_set = set()
    while open_list:
        _, cost, current_board, path = heapq.heappop(open_list)
        if board_to_tuple(current_board) in closed_set:
            continue
        closed_set.add(board_to_tuple(current_board))
        if current_board == goal:
            return path, len(path)
        for direction in ['s', 'w', 'a', 'd']:
            new_board = move_tile(current_board, direction)
            if board_to_tuple(new_board) not in closed_set:
                new_cost = cost + 1
                new_path = path + [new_board]
                heapq.heappush(open_list, (new_cost + manhattan_distance(new_board), new_cost, new_board, new_path))
    return None, None
def generate_random_solvable_board():
    while True:
        board = random.sample(range(16), 16)
        board = [board[i:i + 4] for i in range(0, 16, 4)]
        if solve_15_puzzle(board)[0] is not None:
            return board
solution_list = []
def solve_15_puzzle_500_times():
    for i in range(500):
        board = generate_random_solvable_board()
        solution, steps = solve_15_puzzle(board)
        print(f"Initial board #{i + 1}:")
        for row in board:
            print(row)
        print(f"Solved in {steps} steps.\n")
        for step in solution:
            print()
        print("------\n")
        solution_list.append(steps)
solve_15_puzzle_500_times()
print(solution_list)