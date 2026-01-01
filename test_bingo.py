import pytest
from bingo import create_board, PICKED

def test_board_shape_and_center_picked():
    board = create_board()
    assert isinstance(board, list)
    assert len(board) == 5
    for col in board:
        assert isinstance(col, list)
        assert len(col) == 5
    # center must be the PICKED marker
    assert board[2][2] == PICKED
    # only the center should be PICKED
    picked_count = sum(1 for i in range(5) for j in range(5) if board[i][j] == PICKED)
    assert picked_count == 1

def test_column_ranges_and_uniqueness():
    board = create_board()
    for i, col in enumerate(board):
        expected_range = set(range(i * 15 + 1, i * 15 + 16))
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
    assert all(1 <= v <= 75 for v in numbers)