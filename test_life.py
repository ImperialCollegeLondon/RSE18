from life import count_neighbours


def test_count_neighbours():
    board = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    assert count_neighbours(board).tolist() == [
        [0, 0, 0, 0, 0],
        [1, 2, 3, 2, 1],
        [1, 1, 2, 1, 1],
        [1, 2, 3, 2, 1],
        [0, 0, 0, 0, 0],
    ]
