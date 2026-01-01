import random

PICKED = '★'

def print_board(b):
    for row in range(5):
        print(" | ".join(f"{b[col][row]:2}" for col in range(5)))
        print("-" * 23)

def create_board():
    board = []
    for i in range(5):
        candidates = range((i*15)+1, (i*15)+16)
        row = random.sample(candidates, 5)
        board.append(row)
    board[2][2] = PICKED
    return board

def find_bingo(b):
    for row in b:
        if all(num == PICKED for num in row):
            return True
    for col in range(5):
        if all(b[row][col] == PICKED for row in range(5)):
            return True
    if all(b[i][i] == PICKED for i in range(5)):
        return True
    if all(b[i][4-i] == PICKED for i in range(5)):
        return True
    return False

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
        picked_number = random.randint(1, 75)
        while picked_number in picked_numbers:
            picked_number = random.randint(1, 75)
        picked_numbers.add(picked_number)
        print(f"Picked number: {picked_number}")

        for i in range(5):
            for j in range(5):
                if board[i][j] == picked_number:
                    board[i][j] = PICKED

        print_board(board)
        if find_bingo(board):
            print("★★★ Bingo! ★★★")
            break

if __name__ == "__main__":
    game()
