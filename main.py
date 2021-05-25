from CODES import (
    white_pieces,
    black_pieces,
    ranks,
    files
)

from collections import defaultdict
import check_moves

empty_board = [[" " for _ in range(8)] for _ in range(8)]

start_board = (
    [["r", "n", "b", "q", "k", "b", "n", "r"], ["p" for _ in range(8)]]
    + [[" " for _ in range(8)] for _ in range(4)]
    + [[" " for _ in range(8)], ["R", "N", "B", "Q", "K", "B", "N", "R"]]
)

white_pieces = ["P", "R", "N", "B", "K", "Q"]
black_pieces = ["p", "r", "n", "b", "k", "q"]

ranks = ["a", "b", "c", "d", "e", "f", "g", "h"]
files = ["8", "7", "6", "5", "4", "3", "2", "1"]


def get_white_moves(board):
    valid_moves = []
    switcher = {
        "P": check_moves.get_white_pawn_moves,
        "N": check_moves.get_knight_moves,
        "B": check_moves.get_bishop_moves,
        "R": check_moves.get_rook_moves,
        "Q": check_moves.get_queen_moves,
        "K": check_moves.get_king_moves,
    }
    for i in range(8):
        for j in range(8):
            valid_moves += switcher.get(board[i][j], lambda x, y, z: [])(board, i, j)

    return valid_moves


def get_black_moves(board):
    valid_moves = []
    switcher = {
        "p": check_moves.get_black_pawn_moves,
        "n": check_moves.get_knight_moves,
        "b": check_moves.get_bishop_moves,
        "r": check_moves.get_rook_moves,
        "q": check_moves.get_queen_moves,
        "k": check_moves.get_king_moves,
    }
    for i in range(8):
        for j in range(8):
            valid_moves += switcher.get(board[i][j], lambda x, y, z: [])(board, i, j)

    return valid_moves





if __name__ == '__main__':
    print(get_white_moves(start_board))
    for file in start_board:
        print(file)
