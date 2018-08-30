from scipy import signal


def count_neighbours(board):
    """Return an array of neighbour counts for each element of `board`"""
    return signal.convolve2d(board, [[1, 1, 1], [1, 0, 1], [1, 1, 1]], mode="same")
