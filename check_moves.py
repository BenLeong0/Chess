from CODES import (
    white_pieces,
    black_pieces,
    ranks,
    files
)

def get_pawn_moves(board, i, j, colour):# Check if can move one square
    valid_moves = []
    dir = (-1) ** (colour == "white")

    if board[i + dir][j] == " ":
        valid_moves.append(f"{ranks[j]+files[i+dir]}")

    # Check if can move two squares
    if i == 1:
        if board[i + dir][j] == " " and board[i + 2*dir][j] == " ":
            valid_moves.append(f"{ranks[j]+files[i + 2*dir]}")

    # Check if can take left
    if j > 0:
        if board[i + dir][j - 1] in black_pieces:
            valid_moves.append(f"{ranks[j]}x{ranks[j-1]+files[i+dir]}")

    # Check if can take right
    if j < 7:
        if board[i + dir][j + 1] in black_pieces:
            valid_moves.append(f"{ranks[j]}x{ranks[j+1]+files[i+dir]}")

    return valid_moves


def get_white_pawn_moves(board, i, j):
    return get_pawn_moves(board, i, j, "white")


def get_black_pawn_moves(board, i, j):
    return get_pawn_moves(board, i, j, "black")


def get_knight_moves(board, i, j):
    valid_moves = []

    moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
    locations = [(i + x, j + y) for (x, y) in moves if (0 <= i + x <= 7 and 0 <= j + y <= 7)]

    for (x, y) in locations:
        if board[x][y] == " ":
            valid_moves.append(f"N{ranks[j]+files[i]}{ranks[y]+files[x]}")
        elif board[x][y] in black_pieces:
            valid_moves.append(f"N{ranks[j]+files[i]}x{ranks[y]+files[x]}")

    return valid_moves


def get_bishop_moves(board, i, j):
    valid_moves = []

    dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for (dx, dy) in dirs:
        x, y = i + dx, j + dy
        while 0 <= i + x < 8 and 0 <= j + y < 8:
            if board[x][y] == " ":
                valid_moves.append(
                    f"B{ranks[j]+files[i]}{ranks[y]+files[x]}"
                )
            elif board[x][y] in black_pieces:
                valid_moves.append(
                    f"B{ranks[j]+files[i]}x{ranks[y]+files[x]}"
                )
                break
            x += dx
            y += dy

    return valid_moves


def get_rook_moves(board, i, j):
    valid_moves = []

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for (dx, dy) in dirs:
        x, y = i + dx, j + dy
        while 0 <= i + x < 8 and 0 <= j + y < 8:
            if board[x][y] == " ":
                valid_moves.append(
                    f"R{ranks[j]+files[i]}{ranks[y]+files[x]}"
                )
            elif board[x][y] in black_pieces:
                valid_moves.append(
                    f"R{ranks[j]+files[i]}x{ranks[y]+files[x]}"
                )
                break
            x += dx
            y += dy

    return valid_moves


def get_queen_moves(board, i, j):
    valid_moves = []

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for (dx, dy) in dirs:
        x, y = i + dx, j + dy
        while 0 <= i + x < 8 and 0 <= j + y < 8:
            if board[x][y] == " ":
                valid_moves.append(
                    f"Q{ranks[j]+files[i]}{ranks[y]+files[x]}"
                )
            elif board[x][y] in black_pieces:
                valid_moves.append(
                    f"Q{ranks[j]+files[i]}x{ranks[y]+files[x]}"
                )
                break
            x += dx
            y += dy

    return valid_moves


def get_king_moves(board, i, j):
    valid_moves = []

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for (dx, dy) in dirs:
        x, y = i + dx, j + dy
        if board[x][y] == " ":
            valid_moves.append(
                f"K{ranks[j]+files[i]}{ranks[y]+files[x]}"
            )
        elif board[x][y] in black_pieces:
            valid_moves.append(
                f"K{ranks[j]+files[i]}x{ranks[y]+files[x]}"
            )

    return valid_moves
