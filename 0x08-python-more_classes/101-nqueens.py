#!/usr/bin/python3

"""Solves the N-queens puzzle.

Determines all possible my_solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    my_board (list): A list of lists representing the chessboard.
    my_solutions (list): A list of lists containing my_solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    my_board = []
    [my_board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in my_board]
    return (my_board)


def board_deepcopy(my_board):
    """Return a deepcopy of a chessboard."""
    if isinstance(my_board, list):
        return list(map(board_deepcopy, my_board))
    return (my_board)


def get_solution(my_board):
    """Return the list of lists representation of a solved chessboard."""
    my_solution = []
    for r in range(len(my_board)):
        for c in range(len(my_board)):
            if my_board[r][c] == "Q":
                my_solution.append([r, c])
                break
    return (my_solution)


def xout(my_board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        my_board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for c in range(col + 1, len(my_board)):
        my_board[row][c] = "x"
    # X out all backwards spots
    for c in range(col - 1, -1, -1):
        my_board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(my_board)):
        my_board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        my_board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(my_board)):
        if c >= len(my_board):
            break
        my_board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        my_board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(my_board):
            break
        my_board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(my_board)):
        if c < 0:
            break
        my_board[r][c] = "x"
        c -= 1


def recursive_solve(my_board, row, queens, my_solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        my_board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        my_solutions (list): A list of lists of my_solutions.
    Returns:
        my_solutions
    """
    if queens == len(my_board):
        my_solutions.append(get_solution(my_board))
        return (my_solutions)

    for c in range(len(my_board)):
        if my_board[row][c] == " ":
            current_board = board_deepcopy(my_board)
            current_board[row][c] = "Q"
            xout(current_board, row, c)
            my_solutions = recursive_solve(current_board, row + 1,
                                        queens + 1, my_solutions)

    return (my_solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    my_board = init_board(int(sys.argv[1]))
    my_solutions = recursive_solve(my_board, 0, 0, [])
    for my_sol in my_solutions:
        print(my_sol)
