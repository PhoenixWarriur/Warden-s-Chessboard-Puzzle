import numpy as np
import time

start = time.perf_counter()
# warden creates board:
board = np.random.randint(0, 2, 64)
key = np.random.randint(0, 64)


def calculate_board_key(board):
    result = 0
    for j in [i for i, bit in enumerate(board) if bit]:
        result ^= j
    return result


# prisoner 1:
board_key = calculate_board_key(board)
coin_loc = board_key ^ key
board[coin_loc] ^= 1
print(f"prisoner 1 flips coin {coin_loc} from {board[coin_loc] ^ 1} to {board[coin_loc]}")

# prisoner 2 guess:
print(f"prisoner 2 guess: {calculate_board_key(board)}\nkey: {key}")

print(time.perf_counter() - start)