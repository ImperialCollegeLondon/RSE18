from scipy import signal


def count_neighbours(board):
    """Return an array of neighbour counts for each element of `board`"""
    return signal.convolve2d(board, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], mode="same")


def step(board):
    """Return a new board corresponding to one step of the game"""
    nbrs_count = count_neighbours(board)
    return (nbrs_count == 3) | (board & (nbrs_count == 2))
