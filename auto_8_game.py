import heapq
import random
import openpyxl
write_wb = openpyxl.load_workbook("steps.xlsx")
write_ws = write_wb["Sheet1"]
goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
def manhattan_distance(board):
    distance = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                target_x = (board[i][j] - 1) // 3
                target_y = (board[i][j] - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance
def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
def move_tile(board, direction):
    x_0, y_0 = find_zero(board)
    new_board = [row[:] for row in board]
    if direction == "s" and x_0 > 0:
        new_board[x_0][y_0], new_board[x_0 - 1][y_0] = new_board[x_0 - 1][y_0], new_board[x_0][y_0]
    elif direction == "w" and x_0 < 2:
        new_board[x_0][y_0], new_board[x_0 + 1][y_0] = new_board[x_0 + 1][y_0], new_board[x_0][y_0]
    elif direction == "a" and y_0 < 2:
        new_board[x_0][y_0], new_board[x_0][y_0 + 1] = new_board[x_0][y_0 + 1], new_board[x_0][y_0]
    elif direction == "d" and y_0 > 0:
        new_board[x_0][y_0], new_board[x_0][y_0 - 1] = new_board[x_0][y_0 - 1], new_board[x_0][y_0]
    return new_board
def solve_8_puzzle(board):
    def board_to_tuple(board):
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
        board = random.sample(range(9), 9)
        board = [board[i:i + 3] for i in range(0, 9, 3)]
        if solve_8_puzzle(board)[0] is not None:
            return board
def solve_8_puzzle_10000_times():
    for i in range(10000):
        board = generate_random_solvable_board()
        solution, steps = solve_8_puzzle(board)
        solution_list.append(steps)
        c = write_ws.cell(i + 1, 1)
        c.value = steps
solve_8_puzzle_10000_times()
write_wb.save("steps.xlsx")