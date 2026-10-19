from ch2_6_two_pointers import (interval_overlaps, is_monotonic, merge_intervals, most_water, move_to_end,
                               negatives_first, next_arrangement, pair_sum_sorted, quads_to_target, smallest_gap,
                               sorted_squares, trapped_water, triples_to_target, unsorted_stretch)


def test_ex_2_6_1():
    nums = [1, 3, 4, 6, 9]
    assert pair_sum_sorted(nums, 10) == [0, 4] and pair_sum_sorted(nums, 13) == [2, 4]
    assert pair_sum_sorted(nums, 2) == [] and pair_sum_sorted([], 0) == []


def test_ex_2_6_2():
    assert sorted_squares([-4, -1, 0, 3]) == [0, 1, 9, 16] and sorted_squares([-3, -2]) == [4, 9]
    assert sorted_squares([2, 5]) == [4, 25] and sorted_squares([]) == []


def test_ex_2_6_3():
    assert smallest_gap([5, 19, 31], [12, 29, 1]) == 2 and smallest_gap([4], [4]) == 0
    assert smallest_gap([-10, 50], [7]) == 17


def test_ex_2_6_4():
    nums = [2, 1, 2, 3, 2, 4]
    assert move_to_end(nums, 2) is nums and nums == [1, 3, 4, 2, 2, 2]
    assert move_to_end([7, 7], 7) == [7, 7] and move_to_end([1, 2], 9) == [1, 2] and move_to_end([], 1) == []


def test_ex_2_6_5():
    assert is_monotonic([1, 2, 2, 5]) and not is_monotonic([3, 1, 2])
    assert is_monotonic([]) and is_monotonic([5, 5, 4, 0]) and is_monotonic([1, 1]) and not is_monotonic([1, 2, 1])


def test_ex_2_6_6():
    given = [[6, 8], [1, 3], [2, 4], [8, 9]]
    assert merge_intervals(given) == [[1, 4], [6, 9]] and given == [[6, 8], [1, 3], [2, 4], [8, 9]]
    assert merge_intervals([]) == [] and merge_intervals([[1, 10], [2, 3]]) == [[1, 10]]
    assert merge_intervals([[4, 5], [1, 2]]) == [[1, 2], [4, 5]]


def test_ex_2_6_7():
    assert triples_to_target([4, -1, 2, 0, -3, 1], 1) == [[-3, 0, 4], [-1, 0, 2]]
    assert triples_to_target([0, 0, 0, 0], 0) == [[0, 0, 0]] and triples_to_target([1, 2], 3) == []
    assert triples_to_target([2, 2, 1, 1, 0], 4) == [[0, 2, 2], [1, 1, 2]]


def test_ex_2_6_8():
    assert most_water([2, 7, 3, 6, 1, 5]) == 20 and most_water([1, 1]) == 1
    assert most_water([4]) == 0 and most_water([3, 1, 1, 3]) == 9


def test_ex_2_6_9():
    assert interval_overlaps([[1, 4], [6, 9]], [[3, 7], [9, 12]]) == [[3, 4], [6, 7], [9, 9]]
    assert interval_overlaps([[1, 2]], [[3, 4]]) == [] and interval_overlaps([], [[1, 5]]) == []
    assert interval_overlaps([[0, 10]], [[1, 2], [4, 5]]) == [[1, 2], [4, 5]]


def test_ex_2_6_10():
    assert unsorted_stretch([1, 3, 7, 5, 6, 9]) == [2, 4] and unsorted_stretch([1, 2, 3]) == [-1, -1]
    assert unsorted_stretch([3, 2, 1]) == [0, 2] and unsorted_stretch([1, 2, 4, 3, 3, 5]) == [2, 4]
    assert unsorted_stretch([2, 2]) == [-1, -1] and unsorted_stretch([]) == [-1, -1]


def test_ex_2_6_11():
    nums = [3, -1, 4, -5, 9, -2]
    assert negatives_first(nums) is nums and nums == [-1, -5, -2, 3, 4, 9]
    assert negatives_first([]) == [] and negatives_first([1, 2]) == [1, 2] and negatives_first([-1, -2]) == [-1, -2]
    assert negatives_first([0, -3, 0, -4, 7]) == [-3, -4, 0, 0, 7]


def test_ex_2_6_12():
    nums = [1, 3, 2]
    assert next_arrangement(nums) is nums and nums == [2, 1, 3]
    assert next_arrangement([3, 2, 1]) == [1, 2, 3] and next_arrangement([1, 1, 5]) == [1, 5, 1]
    assert next_arrangement([2, 4, 3, 1]) == [3, 1, 2, 4] and next_arrangement([]) == []


def test_ex_2_6_13():
    assert quads_to_target([2, -1, 0, 3, -2, 1], 2) == [[-2, -1, 2, 3], [-2, 0, 1, 3], [-1, 0, 1, 2]]
    assert quads_to_target([1, 1, 1, 1, 1], 4) == [[1, 1, 1, 1]] and quads_to_target([1, 2, 3], 6) == []


def test_ex_2_6_14():
    assert trapped_water([3, 0, 2, 0, 4]) == 7 and trapped_water([]) == 0 and trapped_water([1, 2, 3]) == 0
    assert trapped_water([5, 1, 1, 5]) == 8 and trapped_water([4, 1, 3, 1, 2]) == 3
