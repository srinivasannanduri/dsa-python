from ch7_3_greedy_transforms import (best_schedule_profit, can_reach_end, can_take_photo, fewest_rewards,
                                    has_pair_with_difference, least_total_waiting, lone_value, longest_unique_run,
                                    loop_start, max_meetings, pair_finish_time, RangeSum, rooms_needed,
                                    stable_matching, tandem_total, top_k_frequent, window_with_sum)


def test_ex_7_3_1():
    assert has_pair_with_difference([1, 8, 4, 11], 3) and not has_pair_with_difference([1, 5], 3)
    assert has_pair_with_difference([3, 3], 0) and not has_pair_with_difference([3], 0) and has_pair_with_difference([10, -2], 12)


def test_ex_7_3_2():
    assert window_with_sum([2, 4, 3, 5, 1], 8) == (2, 3) and window_with_sum([1, 2], 7) is None
    assert window_with_sum([5], 5) == (0, 0) and window_with_sum([1, 2, 3], 6) == (0, 2) and window_with_sum([], 1) is None


def test_ex_7_3_3():
    assert can_reach_end([2, 3, 1, 1, 4]) and not can_reach_end([3, 2, 1, 0, 4])
    assert can_reach_end([0]) and not can_reach_end([0, 1]) and can_reach_end([1, 1, 1])


def test_ex_7_3_4():
    assert rooms_needed([[9, 11], [10, 12], [11, 13], [9, 10]]) == 2
    assert rooms_needed([]) == 0 and rooms_needed([[1, 5], [2, 6], [3, 7]]) == 3 and rooms_needed([[1, 2], [2, 3]]) == 1


def test_ex_7_3_5():
    assert max_meetings([[1, 4], [3, 5], [0, 6], [5, 7], [8, 9], [5, 9]]) == 3
    assert max_meetings([]) == 0 and max_meetings([[1, 10], [2, 3], [3, 4], [4, 5]]) == 3 and max_meetings([[1, 2], [1, 2]]) == 1


def test_ex_7_3_6():
    r = RangeSum([3, 1, 4, 1, 5])
    assert r.total(1, 3) == 6 and r.total(0, 4) == 14 and r.total(2, 2) == 4 and r.total(0, 0) == 3
    assert RangeSum([-2, 2]).total(0, 1) == 0


def test_ex_7_3_7():
    assert top_k_frequent(['b', 'a', 'b', 'c', 'a', 'b'], 2) == ['b', 'a']
    assert top_k_frequent(['x', 'y', 'z'], 2) == ['x', 'y'] and top_k_frequent(['q'], 5) == ['q'] and top_k_frequent([], 1) == []
    assert top_k_frequent(['m', 'n', 'n', 'm', 'o'], 3) == ['m', 'n', 'o']


def test_ex_7_3_8():
    assert lone_value([4, 1, 2, 1, 2]) == 4 and lone_value([7]) == 7 and lone_value([0, 9, 9]) == 0 and lone_value([-3, 5, 5]) == -3


def test_ex_7_3_9():
    assert longest_unique_run('abcadbe') == 5 and longest_unique_run('aaaa') == 1 and longest_unique_run('') == 0
    assert longest_unique_run('abba') == 2 and longest_unique_run('xyz') == 3 and longest_unique_run('tmmzuxt') == 5


def test_ex_7_3_10():
    assert [least_total_waiting(v) for v in ([3, 2, 1, 2, 6], [], [5], [4, 1], [2, 2, 2])] == [17, 0, 0, 1, 6]


def test_ex_7_3_11():
    assert [pair_finish_time(v) for v in ([5, 2, 1, 6, 4, 4], [1, 2], [3, 3, 3, 3], [1, 9, 2, 8])] == [8, 3, 6, 10]


def test_ex_7_3_12():
    assert can_take_photo([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]) and not can_take_photo([1, 2], [1, 3])
    assert not can_take_photo([3], [3]) and can_take_photo([6, 5], [4, 4]) and not can_take_photo([1, 9], [5, 5])


def test_ex_7_3_13():
    r, b = [5, 5, 3, 9, 2], [3, 6, 7, 2, 1]
    assert tandem_total(r, b, True) == 32 and tandem_total(r, b, False) == 25 and tandem_total([1], [1], True) == 1
    assert tandem_total([1, 4], [5, 2], True) == 9 and tandem_total([1, 4], [5, 2], False) == 7


def test_ex_7_3_14():
    assert loop_start([1, 5, 3, 3, 1], [3, 2, 4, 1, 1]) == 1 and loop_start([2, 2], [3, 3]) == -1
    assert loop_start([3], [2]) == 0 and loop_start([1, 2, 3], [2, 3, 1]) == 2


def test_ex_7_3_15():
    assert [fewest_rewards(v) for v in ([4, 2, 6, 3, 3, 1], [], [5], [1, 2, 3], [3, 3, 3], [1, 3, 2], [5, 4, 3, 2, 1])] == [9, 0, 1, 6, 3, 4, 15]


def test_ex_7_3_16():
    assert best_schedule_profit([[2, 50], [1, 10], [2, 40], [1, 30], [3, 20]]) == 110 and best_schedule_profit([]) == 0
    assert best_schedule_profit([[1, 5], [1, 9]]) == 9 and best_schedule_profit([[3, 1], [3, 2], [3, 3], [3, 4]]) == 9


def test_ex_7_3_17():
    P, A = [[0, 1, 2], [0, 2, 1], [1, 0, 2]], [[1, 0, 2], [0, 1, 2], [0, 1, 2]]
    assert stable_matching(P, A) == [1, 0, 2] and stable_matching([[0]], [[0]]) == [0]
    assert stable_matching([[0, 1], [0, 1]], [[1, 0], [1, 0]]) == [1, 0]
    P = [[2, 0, 1, 3], [1, 2, 0, 3], [0, 1, 3, 2], [2, 3, 0, 1]]
    A = [[3, 1, 0, 2], [0, 2, 3, 1], [1, 0, 3, 2], [2, 3, 1, 0]]
    match = stable_matching(P, A)
    partner = {a: p for p, a in enumerate(match)}
    for p in range(4):
        for a in P[p][:P[p].index(match[p])]:
            assert A[a].index(partner[a]) < A[a].index(p)
