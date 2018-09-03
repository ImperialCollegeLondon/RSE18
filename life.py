import numpy as np


def count_neighbours(board):
    """Return an array of neighbour counts for each element of `board`"""
    return sum(
        np.roll(np.roll(board, i, 0), j, 1)
        for i in (-1, 0, 1)
        for j in (-1, 0, 1)
        if (i != 0 or j != 0)
    )


def step(board):
    """Return a new board corresponding to one step of the game"""
    nbrs_count = count_neighbours(board)
    return (nbrs_count == 3) | (board & (nbrs_count == 2))


def play(board, iterations):
    """Return a new board corresponding to `iterations` steps of the game"""
    for _ in range(iterations):
        board = step(board)
    return board.tolist()
