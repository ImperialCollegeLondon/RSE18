import pytest

from life import count_neighbours, play, step


@pytest.fixture
def board():
    return [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_count_neighbours(board):
    assert count_neighbours(board).tolist() == [
        [0, 0, 0, 0, 0],
        [1, 2, 3, 2, 1],
        [1, 1, 2, 1, 1],
        [1, 2, 3, 2, 1],
        [0, 0, 0, 0, 0],
    ]


def test_step(board):
    assert step(board).tolist() == [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]


def test_play(board):
    assert play(board, 2) == board


def test_play_performance(board, benchmark):
    benchmark(play, board, 500)
