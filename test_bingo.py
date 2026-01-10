import pytest
from bingo import (
    BOARD_MAX,
    BOARD_MIN,
    BOARD_SIZE,
    COLUMN_SIZE,
    PICKED,
    create_board,
)

def test_board_shape_and_center_picked():
    board = create_board()
    assert isinstance(board, list)
    assert len(board) == BOARD_SIZE
    for col in board:
        assert isinstance(col, list)
        assert len(col) == BOARD_SIZE
    # center must be the PICKED marker
    assert board[2][2] == PICKED
    # only the center should be PICKED
    picked_count = sum(
        1
        for i in range(BOARD_SIZE)
        for j in range(BOARD_SIZE)
        if board[i][j] == PICKED
    )
    assert picked_count == 1

def test_column_ranges_and_uniqueness():
    board = create_board()
    for i, col in enumerate(board):
        start = (i * COLUMN_SIZE) + 1
        end = (i * COLUMN_SIZE) + COLUMN_SIZE + 1
        expected_range = set(range(start, end))
        values = [v for v in col if v != PICKED]
        # all non-picked values are ints within the expected column range
        assert all(isinstance(v, int) for v in values)
        assert set(values).issubset(expected_range)
        # values in a column are unique
        assert len(values) == len(set(values))
        # middle column has one PICKED replaced, so 4 numbers there, others have 5
        if i == 2:
            assert len(values) == 4
        else:
            assert len(values) == 5

def test_all_numbers_in_valid_global_range():
    board = create_board()
    numbers = [v for col in board for v in col if v != PICKED]
    assert all(BOARD_MIN <= v <= BOARD_MAX for v in numbers)
