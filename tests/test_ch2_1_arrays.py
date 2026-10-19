import pytest
from ch2_1_arrays import (Array, ArraySet, count_occurrences, DynamicArray, find_all_indices, find_min_max,
                         first_repeat_in_place, longest_mountain, lowest_missing_positive, majority,
                         missing_from_range, products_except_self, reverse_in_place, smallest_unmakeable, steps_table)


def build(values, capacity=None):
    """An Array holding `values`, filled directly so a test needs only 2.1.1 and its own exercise."""
    a = Array(capacity or len(values) + 2)
    a.data[:len(values)] = values
    a.length = len(values)
    return a


def test_ex_2_1_1():
    a = Array(5)
    assert len(a) == 0 and a.is_empty() and not a.is_full() and a.to_list() == []
    assert a.capacity == 5 and a.data == [None] * 5 and a.steps == 0
    full = build([1, 2], capacity=2)
    assert full.is_full() and not full.is_empty() and len(full) == 2 and full.to_list() == [1, 2]
    full.steps = 7
    full.reset_steps()
    assert full.steps == 0


def test_ex_2_1_2():
    a = build([10, 20, 30])
    assert a.read(1) == 20 and a.steps == 1
    with pytest.raises(IndexError):
        a.read(3)
    with pytest.raises(IndexError):
        a.read(-1)


def test_ex_2_1_3():
    a = build([4, 8, 15])
    assert a.first() == 4 and a.last() == 15
    assert Array(3).first() is None and Array(3).last() is None


def test_ex_2_1_4():
    a = build([1, 2, 3])
    a.update(0, 9)
    assert a.to_list() == [9, 2, 3] and a.steps == 1
    with pytest.raises(IndexError):
        a.update(3, 0)


def test_ex_2_1_5():
    a = build([5, 3, 7])
    assert a.search(7) == 2 and a.steps == 3
    a.reset_steps()
    assert a.search(9) == -1 and a.steps == 3
    a.reset_steps()
    assert a.search(5) == 0 and a.steps == 1


def test_ex_2_1_6():
    a = build([5, 3, 7])
    assert a.contains(3) and not a.contains(4)


def test_ex_2_1_7():
    a = build([1, 2])
    a.insert_at_end(3)
    assert a.to_list() == [1, 2, 3] and a.steps == 1
    a = build([1], capacity=1)
    with pytest.raises(OverflowError):
        a.insert_at_end(2)


def test_ex_2_1_8():
    a = build([2, 3, 4])
    a.insert_at_start(1)
    assert a.to_list() == [1, 2, 3, 4] and a.steps == 4


def test_ex_2_1_9():
    a = build([1, 2, 4], capacity=5)
    a.insert_at(2, 3)
    assert a.to_list() == [1, 2, 3, 4] and a.steps == 2
    a.insert_at(4, 5)
    assert a.to_list() == [1, 2, 3, 4, 5]
    with pytest.raises(OverflowError):
        a.insert_at(0, 0)
    with pytest.raises(IndexError):
        build([1]).insert_at(5, 0)


def test_ex_2_1_10():
    a = build([1, 2, 3])
    assert a.delete_at_end() == 3 and a.to_list() == [1, 2] and a.steps == 1
    with pytest.raises(IndexError):
        Array(2).delete_at_end()


def test_ex_2_1_11():
    a = build([1, 2, 3, 4])
    assert a.delete_at_start() == 1 and a.to_list() == [2, 3, 4] and a.steps == 4


def test_ex_2_1_12():
    a = build([1, 2, 9, 3])
    assert a.delete_at(2) == 9 and a.to_list() == [1, 2, 3]
    with pytest.raises(IndexError):
        a.delete_at(3)


def test_ex_2_1_13():
    a = build([4, 5, 4])
    assert a.delete_value(4) and a.to_list() == [5, 4]
    assert not a.delete_value(8) and a.to_list() == [5, 4]


def test_ex_2_1_14():
    assert count_occurrences([3, 1, 3, 3], 3) == 3
    assert find_all_indices([3, 1, 3, 3], 3) == [0, 2, 3]
    assert count_occurrences([], 1) == 0 and find_all_indices([1, 2], 9) == []


def test_ex_2_1_15():
    assert find_min_max([7, -2, 9, 4]) == (-2, 9)
    assert find_min_max([5]) == (5, 5)
    assert find_min_max([]) is None


def test_ex_2_1_16():
    assert reverse_in_place([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
    assert reverse_in_place([1, 2]) == [2, 1]
    assert reverse_in_place([]) == []


def test_ex_2_1_17():
    s = ArraySet(4)
    assert s.add(3) and not s.add(3) and len(s) == 1
    s.reset_steps()
    s.add(4)
    assert s.steps == 2  # 1 search step + 1 write
    assert s.insert_at_end(4) is False and s.to_list() == [3, 4]


def test_ex_2_1_18():
    assert steps_table(5) == {'read': 1, 'search_missing': 5, 'insert_end': 1,
                              'insert_start': 6, 'delete_end': 1, 'delete_start': 5}


def test_ex_2_1_19():
    d = DynamicArray(2)
    for v in (1, 2, 3):
        d.insert_at_end(v)
    assert d.capacity == 4 and d.to_list() == [1, 2, 3]


def test_ex_2_1_20():
    assert majority([3, 1, 3, 3, 2, 3]) == 3 and majority([7]) == 7
    assert majority([2, 2, 1]) == 2 and majority([1, 2, 1, 2, 1]) == 1 and majority([5, 9, 9]) == 9


def test_ex_2_1_21():
    assert products_except_self([2, 3, 4, 5]) == [60, 40, 30, 24]
    assert products_except_self([1, 0, 3]) == [0, 3, 0] and products_except_self([0, 0]) == [0, 0] and products_except_self([5]) == [1]
    assert products_except_self([-1, 2, -3]) == [-6, 3, -2]


def test_ex_2_1_22():
    assert longest_mountain([1, 3, 5, 4, 2, 2, 6, 1]) == 5
    assert longest_mountain([1, 2, 3]) == 0 and longest_mountain([3, 2, 1]) == 0 and longest_mountain([]) == 0
    assert longest_mountain([1, 3, 2, 4, 1]) == 3 and longest_mountain([1, 2, 1, 2, 3, 2, 1]) == 5 and longest_mountain([2, 2, 2]) == 0


def test_ex_2_1_23():
    assert smallest_unmakeable([2, 1, 6]) == 4 and smallest_unmakeable([1, 1, 3]) == 6
    assert smallest_unmakeable([]) == 1 and smallest_unmakeable([2]) == 1 and smallest_unmakeable([1, 2, 4, 8]) == 16


def test_ex_2_1_24():
    assert lowest_missing_positive([4, -2, 1, 9, 2]) == 3 and lowest_missing_positive([2, 3]) == 1
    assert lowest_missing_positive([1, 2, 3]) == 4 and lowest_missing_positive([]) == 1 and lowest_missing_positive([1, 1, 1]) == 2
    assert lowest_missing_positive([0, -5, 3, 2, 1, 5]) == 4


def test_ex_2_1_25():
    assert missing_from_range([4, 1, 6], 6) == [2, 3, 5]
    assert missing_from_range([], 3) == [1, 2, 3] and missing_from_range([2, 1], 2) == [] and missing_from_range([1], 1) == []


def test_ex_2_1_26():
    data = [3, 1, 4, 4, 1]
    assert first_repeat_in_place(data) == 4 and data == [3, 1, 4, 4, 1]
    assert first_repeat_in_place([1, 2, 3]) == -1 and first_repeat_in_place([2, 2]) == 2 and first_repeat_in_place([1, 3, 3, 1]) == 3
