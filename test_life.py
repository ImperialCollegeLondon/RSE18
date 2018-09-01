import numpy as np
import pytest
from hypothesis import given
from hypothesis.extra.numpy import arrays
from hypothesis.strategies import integers

from life import count_neighbours, play, step


@pytest.fixture()
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


def test_play(board) -> None:
    assert play(board, 2) == board


# @given(lists(lists(integers(0, 1))), integers(max_value=20))
# @given(lists(lists(integers(0, 1))), integers(min_value=1, max_value=20))
# @given(
#     lists(lists(integers(0, 1), min_size=1), min_size=1),
#     integers(min_value=1, max_value=20),
# )
@given(
    arrays(np.int8, integers(min_value=1, max_value=10).map(lambda i: (i, i))),
    integers(min_value=1, max_value=20),
)
def test_play_fuzz(board, iterations):
    play(board, iterations)
