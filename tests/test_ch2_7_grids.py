from ch2_7_grids import (find_in_sorted_grid, rotate_clockwise, spiral_order, transpose, valid_board, zero_rows_cols,
                        zigzag_order)


def test_ex_2_7_1():
    assert transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
    assert transpose([[7]]) == [[7]] and transpose([]) == [] and transpose([[1], [2]]) == [[1, 2]]


def test_ex_2_7_2():
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3], [4, 5, 6]]) == [1, 2, 3, 6, 5, 4] and spiral_order([[1, 2], [3, 4], [5, 6]]) == [1, 2, 4, 6, 5, 3]
    assert spiral_order([[1, 2, 3, 4]]) == [1, 2, 3, 4] and spiral_order([[1], [2], [3]]) == [1, 2, 3] and spiral_order([]) == []


def test_ex_2_7_3():
    grid = [[1, 4, 7, 11], [2, 5, 8, 12], [3, 6, 9, 16], [10, 13, 14, 17]]
    assert find_in_sorted_grid(grid, 9) == [2, 2] and find_in_sorted_grid(grid, 15) == [-1, -1]
    assert find_in_sorted_grid(grid, 1) == [0, 0] and find_in_sorted_grid(grid, 17) == [3, 3] and find_in_sorted_grid(grid, 10) == [3, 0]
    assert find_in_sorted_grid([], 3) == [-1, -1]


def test_ex_2_7_4():
    assert zigzag_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 4, 7, 5, 3, 6, 8, 9]
    assert zigzag_order([[1, 2, 3], [4, 5, 6]]) == [1, 2, 4, 5, 3, 6] and zigzag_order([[1], [2], [3]]) == [1, 2, 3]
    assert zigzag_order([[1, 2, 3]]) == [1, 2, 3] and zigzag_order([]) == []


def test_ex_2_7_5():
    grid = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    assert zero_rows_cols(grid) is grid and grid == [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
    assert zero_rows_cols([[0, 1], [1, 1]]) == [[0, 0], [0, 1]] and zero_rows_cols([[1, 1], [1, 1]]) == [[1, 1], [1, 1]]
    assert zero_rows_cols([[5, 0, 7]]) == [[0, 0, 0]] and zero_rows_cols([[1, 2], [3, 4], [0, 6]]) == [[0, 2], [0, 4], [0, 0]]


def test_ex_2_7_6():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert rotate_clockwise(grid) is grid and grid == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    assert rotate_clockwise([[1, 2], [3, 4]]) == [[3, 1], [4, 2]] and rotate_clockwise([[5]]) == [[5]] and rotate_clockwise([]) == []


def test_ex_2_7_7():
    def board(*cells):
        b = [[0] * 9 for _ in range(9)]
        for r, c, d in cells:
            b[r][c] = d
        return b

    full = [[(r * 3 + r // 3 + c) % 9 + 1 for c in range(9)] for r in range(9)]
    assert valid_board(board()) and valid_board(full) and valid_board(board((0, 0, 5), (4, 4, 5)))
    assert not valid_board(board((0, 0, 5), (1, 1, 5))) and not valid_board(board((0, 4, 3), (8, 4, 3)))
    assert not valid_board(board((4, 0, 7), (4, 8, 7)))
    full[8][8] = full[8][7]
    assert not valid_board(full)
