import pytest
from ch1_2_memory_cost import (is_palindrome_clean, mode_counts, mode_nested, mode_sorted, recursion_limit,
                              rotate_copy, rotate_in_place, scale_in_place, scaled_copy, sum_list_iterative,
                              sum_list_recursive)


def test_ex_1_2_1():
    scores = [10, 20]
    assert scaled_copy(scores, 3) == [30, 60] and scores == [10, 20]
    assert scale_in_place(scores, 3) is scores and scores == [30, 60]
    assert scaled_copy([], 5) == [] and scale_in_place([], 5) == []


def test_ex_1_2_2():
    for fn in (mode_nested, mode_counts, mode_sorted):
        assert fn([4, 1, 4, 2, 1, 4]) == 4
        assert fn([2, 1, 2, 1]) == 1 and fn([7]) == 7 and fn([-3, 5, -3]) == -3


def test_ex_1_2_3():
    big = list(range(50_000))
    assert sum_list_iterative(big) == 1249975000 and recursion_limit() >= 1000
    with pytest.raises(RecursionError):
        sum_list_recursive(big)
    assert sum_list_recursive(list(range(101))) == 5050 and sum_list_recursive([]) == 0


def test_ex_1_2_4():
    orig = [1, 2, 3, 4, 5]
    assert rotate_copy(orig, 2) == [4, 5, 1, 2, 3] and orig == [1, 2, 3, 4, 5]
    assert rotate_in_place(orig, 2) is orig and orig == [4, 5, 1, 2, 3]
    assert rotate_in_place([1, 2, 3], 7) == [3, 1, 2] and rotate_copy([1, 2, 3], 0) == [1, 2, 3]
    assert rotate_in_place([], 3) == [] and rotate_copy([], 3) == []


def test_ex_1_2_5():
    assert is_palindrome_clean('A man, a plan, a canal: Panama') and not is_palindrome_clean('ab')
