from ch2_2_sorted_search import (binary_search, binary_search_recursive, find_peak, first_and_last, fixed_point,
                                int_sqrt, linear_search_ordered, lower_bound, median_of_two, OrderedArray,
                                search_rotated, search_steps, smallest_max_load, WeightedPicker)


def test_ex_2_2_1():
    o = OrderedArray([3, 17, 80, 202])
    o.insert(75)
    assert o.items == [3, 17, 75, 80, 202]
    o.insert(1)
    o.insert(500)
    assert o.items == [1, 3, 17, 75, 80, 202, 500]
    e = OrderedArray()
    e.insert(4)
    assert e.items == [4]


def test_ex_2_2_2():
    assert linear_search_ordered([3, 17, 75, 80, 202], 22) == -1
    assert linear_search_ordered([3, 17, 75, 80, 202], 75) == 2
    assert linear_search_ordered([], 1) == -1


def check_binary_search(fn):
    assert fn([3, 17, 75, 80, 202], 80) == 3
    assert fn([1, 3, 5, 7, 9], 1) == 0 and fn([1, 3, 5, 7, 9], 9) == 4
    assert fn([1, 3, 5], 4) == -1 and fn([], 1) == -1


def test_ex_2_2_3():
    check_binary_search(binary_search)


def test_ex_2_2_4():
    check_binary_search(binary_search_recursive)


def test_ex_2_2_5():
    assert lower_bound([10, 20, 20, 30], 20) == 1
    assert lower_bound([10, 20, 20, 30], 25) == 3
    assert lower_bound([10, 20, 20, 30], 99) == 4
    assert lower_bound([10, 20], 5) == 0 and lower_bound([], 5) == 0


def test_ex_2_2_6():
    f = OrderedArray()
    for v in [5, 1, 4, 1, 9]:
        f.insert_fast(v)
    assert f.items == [1, 1, 4, 5, 9]
    g = OrderedArray([3, 17, 80, 202])
    g.insert_fast(75)
    assert g.items == [3, 17, 75, 80, 202]


def test_ex_2_2_7():
    assert first_and_last([1, 2, 2, 2, 5], 2) == (1, 3)
    assert first_and_last([1, 2, 5], 3) == (-1, -1)
    assert first_and_last([2.5, 2.5], 2.5) == (0, 1)


def test_ex_2_2_8():
    d = OrderedArray([2, 4, 6, 8])
    assert d.delete(4) and d.items == [2, 6, 8] and not d.delete(5)
    assert d.delete(8) and d.items == [2, 6]


def test_ex_2_2_9():
    assert search_steps(100) == (100, 7)
    assert search_steps(10_000) == (10000, 14)


def test_ex_2_2_10():
    assert int_sqrt(27) == 5 and int_sqrt(36) == 6 and int_sqrt(0) == 0 and int_sqrt(1) == 1


def test_ex_2_2_11():
    nums = [15, 18, 22, 3, 7, 9]
    assert [search_rotated(nums, x) for x in nums] == list(range(6))
    assert search_rotated(nums, 10) == -1 and search_rotated(nums, 1) == -1 and search_rotated([], 4) == -1
    assert search_rotated([5], 5) == 0 and search_rotated([1, 2, 3], 3) == 2 and search_rotated([3, 1], 1) == 1


def test_ex_2_2_12():
    def is_peak(nums, i):
        return (i == 0 or nums[i - 1] < nums[i]) and (i == len(nums) - 1 or nums[i + 1] < nums[i])

    assert find_peak([1, 3, 2, 5, 4]) == 3
    for nums in ([7], [1, 2, 3, 4], [4, 3, 2, 1], [2, 9, 1, 8, 0, 7, 6], [5, 1]):
        assert is_peak(nums, find_peak(nums))


def test_ex_2_2_13():
    loads = [4, 9, 3, 6, 2, 8]
    assert smallest_max_load(loads, 3) == 13 and smallest_max_load(loads, 1) == 32 and smallest_max_load(loads, 6) == 9
    assert smallest_max_load([5, 5, 5, 5], 2) == 10 and smallest_max_load([7], 3) == 7


def test_ex_2_2_14():
    assert fixed_point([-4, -1, 2, 5, 9]) == 2 and fixed_point([1, 2, 3]) == -1 and fixed_point([0, 1, 2]) == 0
    assert fixed_point([-3, -1, 1, 3, 4]) == 3 and fixed_point([]) == -1 and fixed_point([-5, 0, 7]) == -1


def test_ex_2_2_15():
    assert median_of_two([1, 4, 9], [2, 3]) == 3.0 and median_of_two([1, 4], [2, 3]) == 2.5
    assert median_of_two([], [5]) == 5.0 and median_of_two([1, 2], [3, 4, 5, 6]) == 3.5 and median_of_two([7], [1, 2, 3]) == 2.5
    assert median_of_two([10, 20, 30], []) == 20.0 and median_of_two([1, 1], [1, 1]) == 1.0


def test_ex_2_2_16():
    picker = WeightedPicker([3, 1, 2])
    assert picker.total() == 6 and [picker.pick(r) for r in range(6)] == [0, 0, 0, 1, 2, 2]
    weights = [5, 1, 4, 2]
    picker = WeightedPicker(weights)
    counts = [0] * len(weights)
    for r in range(picker.total()):
        counts[picker.pick(r)] += 1
    assert counts == weights and WeightedPicker([9]).pick(8) == 0
