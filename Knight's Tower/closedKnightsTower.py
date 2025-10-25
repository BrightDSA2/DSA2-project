import random
import matplotlib.pyplot as plt
import numpy as np

# Knight moves
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def is_safe(x, y, board, size=8):
    return 0 <= x < size and 0 <= y < size and board[x][y] == 0

def get_degree(x, y, board, size=8):
    count = 0
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_safe(nx, ny, board, size):
            count += 1
    return count

def knights_tour_bt_util(board, curr_x, curr_y, move_num, start_x, start_y, size=8):
    if move_num == size * size:
        # Check if closed
        for dx, dy in moves:
            if curr_x + dx == start_x and curr_y + dy == start_y:
                return True
        return False
    # Sort next moves by Warnsdorff's rule (fewest onward moves)
    next_moves = []
    for dx, dy in moves:
        next_x = curr_x + dx
        next_y = curr_y + dy
        if is_safe(next_x, next_y, board, size):
            deg = get_degree(next_x, next_y, board, size)
            next_moves.append((deg, next_x, next_y))
    next_moves.sort(key=lambda t: t[0])
    for _, next_x, next_y in next_moves:
        board[next_x][next_y] = move_num + 1
        if knights_tour_bt_util(board, next_x, next_y, move_num + 1, start_x, start_y, size):
            return True
        board[next_x][next_y] = 0  # Backtrack
    return False

def KnightsTourBacktracking(startingPosition: tuple[int, int]) -> tuple[bool, list[list[int]]]:
    size = 8
    start_x, start_y = startingPosition
    board = [[0 for _ in range(size)] for _ in range(size)]
    board[start_x][start_y] = 1
    success = knights_tour_bt_util(board, start_x, start_y, 1, start_x, start_y, size)
    return success, board

def KnightsTourLasVegas(startingPosition: tuple[int, int]) -> tuple[bool, list[list[int]]]:
    size = 8
    start_x, start_y = startingPosition
    board = [[0 for _ in range(size)] for _ in range(size)]
    curr_x, curr_y = start_x, start_y
    board[curr_x][curr_y] = 1
    for move_num in range(2, size * size + 1):
        valid_moves = []
        for dx, dy in moves:
            next_x = curr_x + dx
            next_y = curr_y + dy
            if is_safe(next_x, next_y, board, size):
                valid_moves.append((next_x, next_y))
        if not valid_moves:
            return False, board
        next_x, next_y = random.choice(valid_moves)
        board[next_x][next_y] = move_num
        curr_x, curr_y = next_x, next_y
    # Check if closed
    can_close = any(curr_x + dx == start_x and curr_y + dy == start_y for dx, dy in moves)
    return can_close, board

def visualize_board(board, title="Knight's Tour Board"):
    board_np = np.array(board)
    fig, ax = plt.subplots()
    ax.imshow(board_np, cmap='viridis')
    for i in range(len(board)):
        for j in range(len(board[0])):
            ax.text(j, i, board[i][j], ha='center', va='center', color='black' if board[i][j] > 0 else 'white')
    plt.title(title)
    plt.show()

# Main program with user input
if __name__ == "__main__":
    while True:
        approach = input("Choose approach (Backtracking, Las Vegas, or exit): ").strip().lower()
        if approach == 'exit':
            break
        if approach not in ['backtracking', 'las vegas']:
            print("Invalid input. Try again.")
            continue
        start_input = input("Enter starting position (e.g., 0,0): ").strip()
        try:
            start = tuple(map(int, start_input.split(',')))
            if len(start) != 2 or not all(0 <= s < 8 for s in start):
                raise ValueError
        except ValueError:
            print("Invalid position. Must be two integers between 0 and 7.")
            continue
        if approach == 'backtracking':
            success, board = KnightsTourBacktracking(start)
        else:
            success, board = KnightsTourLasVegas(start)
        print(f"Tour successful: {success}")
        visualize_board(board, title=f"{approach.capitalize()} Approach - Success: {success}")
