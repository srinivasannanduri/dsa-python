import pytest
from ch4_1_hash_tables import (can_build, count_sum_runs, disjoint, distinct_per_day, group_anagrams,
                              has_zero_sum_run, HashTable, in_exactly_one, invert, longest_consecutive,
                              most_common_word, most_on_a_line, positions, same_pattern, symmetric_pairs,
                              trace_journey, two_sum_indices, word_counts)


def test_ex_4_1_1():
    t = HashTable(2)
    t.put('bad', 'evil')
    t.put('bad', 'awful')
    assert t.get('bad') == 'awful' and len(t) == 1
    for i in range(100):
        t.put(i, i * i)
    assert len(t) == 101 and t.get(42) == 1764 and len(t.buckets) >= 128
    assert 7 in t and t.delete(7) and 7 not in t and not t.delete(7)
    with pytest.raises(KeyError):
        t.get('missing')


def test_ex_4_1_2():
    assert can_build('abba', 'aabbc') and not can_build('abc', 'ab')
    assert can_build('', 'xyz') and not can_build('aa', 'a') and can_build('cab', 'bac')


def test_ex_4_1_3():
    assert in_exactly_one([1, 2, 3], [2, 3, 4]) == [1, 4]
    assert in_exactly_one([5, 5, 1], [1]) == [5] and in_exactly_one([], [2, 2]) == [2] and in_exactly_one([1], [1]) == []


def test_ex_4_1_4():
    assert distinct_per_day([1, 1, 1, 2], ['ana', 'bo', 'ana', 'ana']) == {1: 2, 2: 1}
    assert distinct_per_day([], []) == {} and distinct_per_day([7, 7], ['x', 'x']) == {7: 1}


def test_ex_4_1_5():
    assert same_pattern('egg', 'add') and not same_pattern('foo', 'bar')
    assert same_pattern('paper', 'title') and not same_pattern('ab', 'aa') and not same_pattern('aa', 'ab')
    assert not same_pattern('a', 'ab') and same_pattern('', '')


def test_ex_4_1_6():
    assert positions(['a', 'b', 'a']) == {'a': [0, 2], 'b': [1]}
    assert positions([]) == {} and positions(['x'] * 3) == {'x': [0, 1, 2]}


def test_ex_4_1_7():
    assert word_counts('the cat and the hat') == {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
    assert most_common_word('the cat and the hat') == 'the'


def test_ex_4_1_8():
    assert group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


def test_ex_4_1_9():
    assert two_sum_indices([2, 7, 11, 15], 9) == (0, 1) and two_sum_indices([1], 2) is None
    assert two_sum_indices([3, 3], 6) == (0, 1)


def test_ex_4_1_10():
    assert invert({'fries': 2, 'soda': 2, 'burger': 5}) == {2: ['fries', 'soda'], 5: ['burger']}


def test_ex_4_1_11():
    assert longest_consecutive([10, 4, 20, 1, 3, 2, 11]) == 4 and longest_consecutive([]) == 0
    assert longest_consecutive([5, 5, 5]) == 1 and longest_consecutive([0, -1, 1, 9, 8]) == 3


def test_ex_4_1_12():
    assert has_zero_sum_run([4, 2, -3, 1, 6]) and not has_zero_sum_run([4, 2, 1]) and has_zero_sum_run([0])
    assert not has_zero_sum_run([]) and has_zero_sum_run([1, -1]) and has_zero_sum_run([3, 5, -8, 2]) and not has_zero_sum_run([-2, 5])


def test_ex_4_1_13():
    assert count_sum_runs([1, 2, 3, -2, 2], 3) == 4 and count_sum_runs([1, 1, 1], 2) == 2 and count_sum_runs([], 0) == 0
    assert count_sum_runs([0, 0], 0) == 3 and count_sum_runs([5], -5) == 0 and count_sum_runs([2, -2, 2], 2) == 3


def test_ex_4_1_14():
    assert symmetric_pairs([[1, 2], [3, 4], [5, 6], [4, 3], [2, 1]]) == [[3, 4], [1, 2]] and symmetric_pairs([]) == []
    assert symmetric_pairs([[1, 2], [2, 3]]) == [] and symmetric_pairs([[7, 8], [8, 7], [9, 7], [7, 9]]) == [[7, 8], [9, 7]]


def test_ex_4_1_15():
    assert trace_journey([["MAA", "BOM"], ["DEL", "MAA"], ["BOM", "GOI"]]) == ["DEL", "MAA", "BOM", "GOI"]
    assert trace_journey([]) == [] and trace_journey([["A", "B"]]) == ["A", "B"]
    assert trace_journey([["C", "D"], ["B", "C"], ["D", "E"], ["A", "B"]]) == ["A", "B", "C", "D", "E"]


def test_ex_4_1_16():
    assert disjoint([1, 5, 9], [2, 6]) and not disjoint([1, 5], [5]) and disjoint([], [1])
    assert disjoint([], []) and not disjoint([3, 3], [4, 3])


def test_ex_4_1_17():
    assert most_on_a_line([[0, 0], [1, 1], [2, 2], [3, 1], [0, 3]]) == 3 and most_on_a_line([]) == 0 and most_on_a_line([[1, 1]]) == 1
    assert most_on_a_line([[1, 1], [1, 1], [2, 3]]) == 3 and most_on_a_line([[2, 0], [2, 5], [2, -1], [3, 3]]) == 3
    assert most_on_a_line([[0, 0], [2, 1], [4, 2], [6, 3], [1, 0]]) == 4 and most_on_a_line([[0, 0], [-2, 1], [2, -1]]) == 3
