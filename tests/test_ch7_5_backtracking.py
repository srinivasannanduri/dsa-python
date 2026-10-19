from ch7_5_backtracking import (address_splits, combinations_to, keypad_letters, orderings, queen_placements,
                               solve_sudoku, unique_subsets)


def test_ex_7_5_1():
    assert orderings([1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    assert orderings([]) == [[]] and orderings([7]) == [[7]] and len(orderings([1, 2, 3, 4, 5])) == 120


def test_ex_7_5_2():
    assert keypad_letters("23") == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"] and keypad_letters("") == []
    assert keypad_letters("7") == ["p", "q", "r", "s"] and len(keypad_letters("79")) == 16 and keypad_letters("99")[-1] == "zz"


def test_ex_7_5_3():
    assert combinations_to([3, 4, 5], 11) == [[3, 3, 5], [3, 4, 4]] and combinations_to([2], 1) == []
    assert combinations_to([1], 3) == [[1, 1, 1]] and combinations_to([5, 2], 7) == [[2, 5]] and len(combinations_to([1, 2], 6)) == 4


def test_ex_7_5_4():
    assert [queen_placements(n) for n in (4, 1, 2, 3, 5, 6, 8)] == [2, 1, 0, 0, 10, 4, 92]


def test_ex_7_5_5():
    assert unique_subsets([2, 1, 2]) == [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]] and unique_subsets([]) == [[]]
    assert unique_subsets([3, 3]) == [[], [3], [3, 3]] and len(unique_subsets([1, 2, 3])) == 8 and len(unique_subsets([1, 1, 2, 2])) == 9


def test_ex_7_5_6():
    assert address_splits("101023") == ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]
    assert address_splits("0000") == ["0.0.0.0"] and address_splits("1111") == ["1.1.1.1"] and address_splits("123") == []
    assert address_splits("256256256256") == [] and address_splits("255255255255") == ["255.255.255.255"]


def test_ex_7_5_7():
    def solved(b):
        groups = [b[r] for r in range(9)] + [[b[r][c] for r in range(9)] for c in range(9)]
        groups += [[b[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)] for br in (0, 3, 6) for bc in (0, 3, 6)]
        return all(sorted(g) == list(range(1, 10)) for g in groups)

    full = [[(r * 3 + r // 3 + c) % 9 + 1 for c in range(9)] for r in range(9)]
    puzzle = [[0 if (r * 7 + c * 3) % 9 < 5 else full[r][c] for c in range(9)] for r in range(9)]
    given = [row[:] for row in puzzle]
    assert sum(row.count(0) for row in puzzle) == 45 and solve_sudoku(puzzle) and solved(puzzle)
    assert all(given[r][c] in (0, puzzle[r][c]) for r in range(9) for c in range(9))
    stuck = [[0] * 9 for _ in range(9)]
    stuck[0][:8] = [1, 2, 3, 4, 5, 6, 7, 8]
    stuck[1][8] = 9
    before = [row[:] for row in stuck]
    assert not solve_sudoku(stuck) and stuck == before
    empty = [[0] * 9 for _ in range(9)]
    assert solve_sudoku(empty) and solved(empty)
