import random

BOARD_SIZE = 5
COLUMN_SIZE = 15
BOARD_MIN = 1
BOARD_MAX = 75
PICKED = '★'

def print_board(b):
    # The board is stored by columns, so we print by rows.
    for row in range(BOARD_SIZE):
        print(" | ".join(f"{b[col][row]:2}" for col in range(BOARD_SIZE)))
        print("-" * 23)

def create_board():
    board = []
    for col_index in range(BOARD_SIZE):
        start = (col_index * COLUMN_SIZE) + 1
        end = (col_index * COLUMN_SIZE) + COLUMN_SIZE + 1
        candidates = range(start, end)
        column = random.sample(candidates, BOARD_SIZE)
        board.append(column)
    board[2][2] = PICKED
    return board

def find_bingo(b):
    for row in b:
        if all(num == PICKED for num in row):
            return True
    for col in range(BOARD_SIZE):
        if all(b[row][col] == PICKED for row in range(BOARD_SIZE)):
            return True
    if all(b[i][i] == PICKED for i in range(BOARD_SIZE)):
        return True
    last = BOARD_SIZE - 1
    if all(b[i][last - i] == PICKED for i in range(BOARD_SIZE)):
        return True
    return False

def mark_picked_number(b, picked_number):
    for col in range(BOARD_SIZE):
        for row in range(BOARD_SIZE):
            if b[col][row] == picked_number:
                b[col][row] = PICKED

def game():
    board = create_board()
    picked_numbers = set()
    print_board(board)

    while True:
        try:
            input("Press Enter to pick the next number...")
        except KeyboardInterrupt:
            print("\nGame interrupted.")
            break

        # Simulate picking a random number
        picked_number = random.randint(BOARD_MIN, BOARD_MAX)
        while picked_number in picked_numbers:
            picked_number = random.randint(BOARD_MIN, BOARD_MAX)
        picked_numbers.add(picked_number)
        print(f"Picked number: {picked_number}")

        mark_picked_number(board, picked_number)

        print_board(board)
        if find_bingo(board):
            print("★★★ Bingo! ★★★")
            break

if __name__ == "__main__":
    game()
