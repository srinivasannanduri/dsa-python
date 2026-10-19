from ch7_2_dynamic_programming import (best_streak, best_without_neighbours, can_split, change_ways,
                                      common_subsequence_length, count_fib_calls, decode_ways, dice_ways_memo,
                                      edit_distance, fewest_jumps, fib_bottom_up, fib_memo, fib_naive, grid_paths,
                                      knapsack, largest_square, longest_increasing_length, max_profit_k, min_coins,
                                      min_max, min_palindrome_cuts, tilings_memo)


def test_ex_7_2_1():
    assert fib_naive(10) == fib_memo(10) == fib_bottom_up(10) == 55
    assert fib_memo(80) == fib_bottom_up(80) == 23416728348467685
    assert fib_bottom_up(0) == 0 and fib_bottom_up(1) == 1


def test_ex_7_2_2():
    assert min_max([4, -2, 9, 0]) == (-2, 9) and min_max([7]) == (7, 7) and min_max([3, 3]) == (3, 3)
    assert min_max(list(range(60))) == (0, 59)


def test_ex_7_2_3():
    assert tilings_memo(10) == 28 and tilings_memo(60) == 5582216355 and tilings_memo(90) == 533352837917926
    assert [tilings_memo(n) for n in range(8)] == [1, 1, 1, 2, 3, 4, 6, 9]


def test_ex_7_2_4():
    assert dice_ways_memo(2, 7) == 6 and dice_ways_memo(3, 10) == 27 and dice_ways_memo(1, 7) == 0
    assert dice_ways_memo(20, 70) == 189456975899496 and dice_ways_memo(10, 35) == 4395456


def test_ex_7_2_5():
    assert count_fib_calls(10) == (177, 19)


def test_ex_7_2_6():
    assert min_coins([1, 5, 10, 25], 63) == 6 and min_coins([2], 3) == -1
    assert min_coins([1, 3, 4], 6) == 2 and min_coins([1], 0) == 0


def test_ex_7_2_7():
    assert [best_without_neighbours(v) for v in ([5, 1, 2, 9, 3], [], [4], [2, 7, 9, 3, 1], [3, 1, 1, 3])] == [14, 0, 4, 12, 6]


def test_ex_7_2_8():
    assert [change_ways(c, a) for c, a in (([2, 3, 5], 10), ([2, 3, 5], 0), ([3], 7), ([1], 4), ([1, 2], 4))] == [4, 1, 0, 1, 3]


def test_ex_7_2_9():
    assert [decode_ways(s) for s in ("1213", "", "06", "10", "27", "101", "0", "2626")] == [5, 1, 0, 1, 1, 1, 0, 4]


def test_ex_7_2_10():
    assert [best_streak(v) for v in ([3, -4, 5, -1, 2, -6, 4], [-3, -1, -2], [1], [2, 3, -1, 4])] == [6, -1, 1, 8]


def test_ex_7_2_11():
    cases = [(["...", ".#.", "..."], 2), (["#"], 0), (["."], 1), (["..", ".."], 2), (["...", "...", "..."], 6), ([".#", "#."], 0), (["..#", "..."], 2)]
    assert [grid_paths(g) for g, _ in cases] == [w for _, w in cases]


def test_ex_7_2_12():
    cases = [("garden", "pardon", 2), ("", "abc", 3), ("abc", "abc", 0), ("abc", "yabd", 2), ("flour", "floor", 1), ("abc", "", 3)]
    assert [edit_distance(a, b) for a, b, _ in cases] == [w for _, _, w in cases]


def test_ex_7_2_13():
    cases = [("stone", "longest", 3), ("abc", "def", 0), ("", "a", 0), ("abcde", "ace", 3), ("aaaa", "aa", 2)]
    assert [common_subsequence_length(a, b) for a, b, _ in cases] == [w for _, _, w in cases]


def test_ex_7_2_14():
    assert [longest_increasing_length(v) for v in ([4, 1, 3, 2, 8, 5, 6], [], [5, 5, 5], [1, 2, 3], [3, 2, 1], [2, 9, 3, 10, 4, 5])] == [4, 0, 1, 3, 1, 4]


def test_ex_7_2_15():
    w, v = [3, 4, 2, 6], [30, 50, 15, 60]
    assert [knapsack(w, v, c) for c in (8, 0, 10, 2, 1)] == [80, 0, 110, 15, 0] and knapsack([], [], 5) == 0


def test_ex_7_2_16():
    assert [fewest_jumps(v) for v in ([3, 1, 2, 1, 1, 4], [0], [1, 0, 2], [5, 1, 1], [1, 1, 1], [2, 0, 0])] == [3, 0, -1, 1, 2, 1]


def test_ex_7_2_17():
    cases = [(["0111", "1111", "0111"], 9), (["0"], 0), (["1"], 1), (["11", "10"], 1), (["110", "111", "011"], 4), ([], 0)]
    assert [largest_square(g) for g, _ in cases] == [w for _, w in cases]


def test_ex_7_2_18():
    words = ["sun", "flower", "field", "sunflow", "er"]
    assert can_split("sunflowerfield", words) and not can_split("sunfield", ["sun", "flower"]) and can_split("", [])
    assert can_split("erersun", words) and not can_split("sunflowe", words)


def test_ex_7_2_19():
    cases = [("noonabbad", 2), ("racecarx", 1), ("abcb", 1), ("abc", 2), ("", 0), ("aaaa", 0), ("ab", 1)]
    assert [min_palindrome_cuts(s) for s, _ in cases] == [w for _, w in cases]


def test_ex_7_2_20():
    p = [3, 8, 2, 6, 1, 9]
    assert [max_profit_k(p, k) for k in (2, 1, 3, 0)] == [13, 8, 17, 0] and max_profit_k([], 2) == 0 and max_profit_k([5, 4, 3], 2) == 0
