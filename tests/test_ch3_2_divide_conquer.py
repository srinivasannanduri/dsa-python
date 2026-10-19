import random
from ch3_2_divide_conquer import (any_overlap, closest_gap_sorted, count_distinct_sorted, count_inversions,
                                 hybrid_sort, median, merge, merge_comparisons, mergesort, mergesort_bottom_up,
                                 mergesort_by, mergesort_in_place, partition, quickselect, quicksort, quicksort3)


def random_lists(seed, n=200):
    rng = random.Random(seed)
    return [[rng.randint(0, 9) for _ in range(rng.randint(0, 25))] for _ in range(n)]


def test_ex_3_2_1():
    a = [0, 5, 2, 1, 6, 3]
    p = partition(a, 0, 5)
    assert p == 3 and all(x < 3 for x in a[:p]) and all(x > 3 for x in a[p + 1:])


def test_ex_3_2_2():
    for data in random_lists(1):
        assert quicksort(list(data)) == sorted(data)


def test_ex_3_2_3():
    assert quickselect([0, 50, 20, 10, 60, 30], 1) == 10
    rng = random.Random(2)
    for data in random_lists(3):
        if data:
            k = rng.randrange(len(data))
            assert quickselect(list(data), k) == sorted(data)[k]


def test_ex_3_2_4():
    data = [10, 4, 15, 7]
    assert closest_gap_sorted(data) == 3 and data == [10, 4, 15, 7]
    assert closest_gap_sorted([1, 100]) == 99 and closest_gap_sorted([5, 5, 9]) == 0 and closest_gap_sorted([-3, 8, -1]) == 2


def test_ex_3_2_5():
    assert any_overlap([[9, 11], [13, 15], [10, 12]]) and not any_overlap([[9, 10], [10, 11]])
    assert not any_overlap([]) and not any_overlap([[1, 5]]) and any_overlap([[1, 10], [2, 3], [11, 12]])


def test_ex_3_2_6():
    assert count_distinct_sorted([5, 9, 3, 5, 9, 9]) == 3
    assert count_distinct_sorted([]) == 0 and count_distinct_sorted([7, 7, 7]) == 1 and count_distinct_sorted([3, -3, 0]) == 3


def test_ex_3_2_7():
    assert median([7, 1, 3]) == 3 and median([4, 1, 3, 2]) == 2.5


def test_ex_3_2_8():
    data = [3, 1, 3, 2, 3, 1]
    assert quicksort3(data) is data and data == [1, 1, 2, 3, 3, 3]
    many = [(i * 7919) % 5 for i in range(500)]
    assert quicksort3(list(many)) == sorted(many) and quicksort3([]) == [] and quicksort3([4]) == [4]
    for data in random_lists(5):
        assert quicksort3(list(data)) == sorted(data)


def rand_lists(n=60, seed=0):
    rng = random.Random(seed)
    return [[rng.randint(-30, 30) for _ in range(rng.randint(0, 40))] for _ in range(n)]


def test_ex_3_2_9():
    assert merge([1, 4, 9], [2, 3, 10, 11]) == [1, 2, 3, 4, 9, 10, 11] and merge([], [1]) == [1]
    assert merge([], []) == []


def test_ex_3_2_10():
    assert merge_comparisons([1, 2, 3], [4, 5, 6])[1] == 3 and merge_comparisons([1, 3, 5], [2, 4, 6])[1] == 5
    assert merge_comparisons([1, 3, 5], [2, 4, 6])[0] == [1, 2, 3, 4, 5, 6]


def test_ex_3_2_11():
    assert mergesort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    for data in rand_lists(seed=1):
        assert mergesort(data) == sorted(data)


def test_ex_3_2_12():
    a = [5, 2, 4, 6, 1, 3]
    mergesort_in_place(a)
    assert a == [1, 2, 3, 4, 5, 6]
    for data in rand_lists(seed=2):
        a = list(data)
        mergesort_in_place(a)
        assert a == sorted(data)


def test_ex_3_2_13():
    for data in rand_lists(seed=3):
        assert mergesort_bottom_up(data) == sorted(data)


def test_ex_3_2_14():
    assert count_inversions([2, 4, 1, 3, 5]) == 3 and count_inversions([5, 4, 3, 2, 1]) == 10
    for data in rand_lists(seed=4):
        brute = sum(1 for i in range(len(data)) for j in range(i + 1, len(data)) if data[i] > data[j])
        assert count_inversions(data) == brute


def test_ex_3_2_15():
    records = [("ann", 3), ("bo", 1), ("cy", 3), ("di", 1)]
    assert mergesort_by(records, key=lambda r: r[1]) == [('bo', 1), ('di', 1), ('ann', 3), ('cy', 3)]


def test_ex_3_2_16():
    assert hybrid_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], cutoff=4) == list(range(10))
    for data in rand_lists(seed=5):
        assert hybrid_sort(data, 4) == sorted(data)
