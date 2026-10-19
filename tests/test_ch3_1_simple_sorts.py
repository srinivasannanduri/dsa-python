import random
from ch3_1_simple_sorts import (bubble_counts, bubble_sort, bubble_sort_optimized, contains_all, equal_pairs_linear,
                               equal_pairs_quadratic, insert_sorted, insertion_sort, insertion_sort_steps, is_sorted,
                               k_smallest, largest_pair_sum_linear, largest_pair_sum_quadratic, neighbour_gaps,
                               second_largest, selection_counts, selection_sort, sort_nearly_sorted)


def random_data(seed):
    rng = random.Random(seed)
    return [rng.randint(-50, 50) for _ in range(60)]


def test_ex_3_1_1():
    assert bubble_sort([4, 2, 7, 1, 3]) == [1, 2, 3, 4, 7]
    data = random_data(1)
    assert bubble_sort(list(data)) == sorted(data)
    assert bubble_sort([]) == []


def test_ex_3_1_2():
    data = random_data(2)
    assert bubble_sort_optimized(list(data))[0] == sorted(data)
    assert bubble_sort_optimized([1, 2, 3, 4]) == ([1, 2, 3, 4], 1)
    assert bubble_sort_optimized([4, 3, 2, 1])[1] == 3
    assert bubble_sort_optimized([]) == ([], 0)


def test_ex_3_1_3():
    assert equal_pairs_quadratic([1, 2, 1, 1, 2]) == 4
    assert equal_pairs_quadratic([1, 2, 3]) == 0 and equal_pairs_quadratic([]) == 0 and equal_pairs_quadratic([5] * 5) == 10


def test_ex_3_1_4():
    assert equal_pairs_linear([1, 2, 1, 1, 2]) == 4
    assert equal_pairs_linear([1, 2, 3]) == 0 and equal_pairs_linear([]) == 0 and equal_pairs_linear([5] * 5) == 10
    assert equal_pairs_linear([7] * 2000) == 1999000


def test_ex_3_1_5():
    for fn in (largest_pair_sum_quadratic, largest_pair_sum_linear):
        assert fn([3, 9, 1, 7]) == 16 and fn([5, 5]) == 10 and fn([-4, -1, -9]) == -5 and fn([9, 1, 9]) == 18


def test_ex_3_1_6():
    assert is_sorted([1, 2, 2, 5]) and not is_sorted([1, 3, 2])
    assert is_sorted([]) and is_sorted([7])


def test_ex_3_1_7():
    rng = random.Random(1)
    data = [rng.randint(-50, 50) for _ in range(60)]
    assert selection_sort(list(data)) == sorted(data)
    assert selection_sort([]) == []


def test_ex_3_1_8():
    rev = list(range(10, 0, -1))
    assert bubble_counts(rev) == (45, 45) and selection_counts(rev) == (45, 5)


def test_ex_3_1_9():
    assert neighbour_gaps([3, 7, 4, 10]) == [4, -3, 6]
    assert neighbour_gaps([5]) == [] and neighbour_gaps([]) == [] and neighbour_gaps([1, 1]) == [0]


def test_ex_3_1_10():
    assert second_largest([5, 1, 9, 7, 9]) == 7 and second_largest([3, 3]) is None
    assert second_largest([1, 2]) == 1 and second_largest([9, 8, 10]) == 9


def test_ex_3_1_11():
    assert k_smallest([8, 3, 5, 1, 9], 2) == [1, 3]


def test_ex_3_1_12():
    rng = random.Random(1)
    data = [rng.randint(-50, 50) for _ in range(60)]
    assert insertion_sort(list(data)) == sorted(data)
    assert insertion_sort([]) == []


def test_ex_3_1_13():
    assert insertion_sort_steps(list(range(100))) == 99
    assert insertion_sort_steps(list(range(100, 0, -1))) == 9900
    assert 99 < insertion_sort_steps(random.Random(2).sample(range(100), 100)) < 9900


def test_ex_3_1_14():
    assert contains_all([4, 8, 15, 16], [8, 16]) and not contains_all([4, 8], [8, 5])
    assert contains_all([1], []) and not contains_all([], [1]) and contains_all([3, 3], [3, 3])


def test_ex_3_1_15():
    assert insert_sorted([1, 4, 9], 5) == [1, 4, 5, 9]
    assert insert_sorted([], 5) == [5] and insert_sorted([2], 1) == [1, 2]


def test_ex_3_1_16():
    data = [2, 1, 3, 5, 4]
    assert sort_nearly_sorted(data, 1) is data and data == [1, 2, 3, 4, 5]
    assert sort_nearly_sorted([3, 1, 2, 6, 4, 5], 2) == [1, 2, 3, 4, 5, 6] and sort_nearly_sorted([], 3) == []
