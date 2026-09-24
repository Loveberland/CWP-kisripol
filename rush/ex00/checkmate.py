def parse_board(board): # validate and prepare board
    if not isinstance(board, str):
        raise ValueError("The board must be a string.")
    board = board.replace("\r\n", "\n") # fix windows style line ending
    if board.endswith("\n"):    # if board end with \n just remove
        board = board[:-1]
    rows = tuple(board.split("\n")) # split board from 1 string to tuple
    size = len(rows)
    if any(len(row) != size for row in rows):   # check board is square
        raise ValueError("The board must be a nonempty square.")
    if sum(row.count("K") for row in rows) != 1:    # check only 1 king on board
        raise ValueError("The board must contain exactly one king.")
    return rows


def _can_attack(piece, row_step, column_step, distance):
    diagonal = row_step != 0 and column_step != 0
    if piece == "Q":
        return True
    if piece == "B":
        return diagonal
    if piece == "R":
        return not diagonal
    if piece == "P":
        return row_step == 1 and diagonal and distance == 1
    return False


def find_attackers(rows):
    king_row, king_column = next((index, row.index("K")) for index, row in enumerate(rows) if "K" in row)   # finding king condinate
    size = len(rows)    # store board size
    attackers = []  
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
    for row_step, column_step in directions:    # choose each direction
        row = king_row + row_step   # set direction around king
        column = king_column + column_step  # set direction around king
        distance = 1
        while 0 <= row < size and 0 <= column < size:   # loop until fell edge
            piece = rows[row][column]
            if piece in "KPBRQ":
                if _can_attack(piece, row_step, column_step, distance):
                    attackers.append((row, column))
                break
            row += row_step
            column += column_step
            distance += 1
    return attackers


def checkmate(board):
    try:
        rows = parse_board(board)
    except ValueError:
        print("Error")
        return
    if find_attackers(rows):
        print("Success")
    else:
        print("Fail")
