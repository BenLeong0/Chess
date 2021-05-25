from CODES import (
    white_pieces,
    black_pieces,
    ranks,
    files
)

def get_pawn_moves(board, i, j, colour):# Check if can move one square
    valid_moves = []
    takeable = {"black": white_pieces, "white": black_pieces}[colour]
    dir = (-1) ** (colour == "white")

    if board[i + dir][j] == " ":
        valid_moves.append(f"{ranks[j]+files[i+dir]}")

    # Check if can move two squares
    if i == {"white": 6, "black": 1}[colour]:
        if board[i + dir][j] == " " and board[i + 2*dir][j] == " ":
            valid_moves.append(f"{ranks[j]+files[i + 2*dir]}")

    # Check if can take left
    if j > 0:
        if board[i + dir][j - 1] in takeable:
            valid_moves.append(f"{ranks[j]}x{ranks[j-1]+files[i+dir]}")

    # Check if can take right
    if j < 7:
        if board[i + dir][j + 1] in takeable:
            valid_moves.append(f"{ranks[j]}x{ranks[j+1]+files[i+dir]}")

    return valid_moves


def get_white_pawn_moves(board, i, j):
    return get_pawn_moves(board, i, j, "white")


def get_black_pawn_moves(board, i, j):
    return get_pawn_moves(board, i, j, "black")


def get_knight_moves(board, i, j, colour):
    valid_moves = []
    takeable = {"black": white_pieces, "white": black_pieces}[colour]

    moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]
    locations = [(i + x, j + y) for (x, y) in moves if (0 <= i + x <= 7 and 0 <= j + y <= 7)]

    for (x, y) in locations:
        if board[x][y] == " ":
            valid_moves.append(f"N{ranks[j]+files[i]}{ranks[y]+files[x]}")
        elif board[x][y] in takeable:
            valid_moves.append(f"N{ranks[j]+files[i]}x{ranks[y]+files[x]}")

    return valid_moves


def get_bishop_moves(board, i, j, colour):
    valid_moves = []
    takeable = {"black": white_pieces, "white": black_pieces}[colour]

    dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    for (dx, dy) in dirs:
        x, y = i + dx, j + dy
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] == " ":
                valid_moves.append(
                    f"B{ranks[j]+files[i]}{ranks[y]+files[x]}"
                )
            elif board[x][y] in takeable:
                valid_moves.append(
                    f"B{ranks[j]+files[i]}x{ranks[y]+files[x]}"
                )
                break
            else:
                break

            x += dx
            y += dy

    return valid_moves


def get_rook_moves(board, i, j, colour):
    valid_moves = []
    takeable = {"black": white_pieces, "white": black_pieces}[colour]

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for (dx, dy) in dirs:
        x, y = i + dx, j + dy
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] == " ":
                valid_moves.append(
                    f"R{ranks[j]+files[i]}{ranks[y]+files[x]}"
                )
            elif board[x][y] in takeable:
                valid_moves.append(
                    f"R{ranks[j]+files[i]}x{ranks[y]+files[x]}"
                )
                break
            else:
                break

            x += dx
            y += dy

    return valid_moves


def get_queen_moves(board, i, j, colour):
    valid_moves = []
    takeable = {"black": white_pieces, "white": black_pieces}[colour]

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for (dx, dy) in dirs:
        x, y = i + dx, j + dy
        while 0 <= x < 8 and 0 <= y < 8:
            if board[x][y] == " ":
                valid_moves.append(
                    f"Q{ranks[j]+files[i]}{ranks[y]+files[x]}"
                )
            elif board[x][y] in takeable:
                valid_moves.append(
                    f"Q{ranks[j]+files[i]}x{ranks[y]+files[x]}"
                )
                break
            else:
                break

            x += dx
            y += dy

    return valid_moves


def get_king_moves(board, i, j, colour):
    valid_moves = []
    takeable = {"black": white_pieces, "white": black_pieces}[colour]

    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for (dx, dy) in dirs:
        x, y = i + dx, j + dy
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            continue
        if board[x][y] == " ":
            valid_moves.append(
                f"K{ranks[j]+files[i]}{ranks[y]+files[x]}"
            )
        elif board[x][y] in takeable:
            valid_moves.append(
                f"K{ranks[j]+files[i]}x{ranks[y]+files[x]}"
            )

    return valid_moves
