from ch1_1_counting_steps import (all_pairs_steps, array_sum, busiest_hour, closest_gap, committees, count_vowels,
                                 final_balance, halving_steps, is_leap_year, is_symmetric, newest, pairings,
                                 rounds_to_reach, shared_hours, switch_settings, unique_pairs_steps, weekly_slots)


def test_ex_1_1_1():
    assert is_leap_year(2024) and not is_leap_year(1900) and is_leap_year(2000)
    assert not is_leap_year(2023)


def test_ex_1_1_2():
    assert array_sum([1, 2, 3, 4]) == 10 and array_sum([]) == 0


def test_ex_1_1_3():
    assert halving_steps(8) == 3 and halving_steps(1024) == 10 and halving_steps(1) == 0


def test_ex_1_1_4():
    assert rounds_to_reach(1) == 0 and rounds_to_reach(2) == 1 and rounds_to_reach(3) == 2
    assert rounds_to_reach(1000) == 10 and rounds_to_reach(1024) == 10 and rounds_to_reach(1025) == 11


def test_ex_1_1_5():
    assert all_pairs_steps(4) == 16 and unique_pairs_steps(4) == 6


def test_ex_1_1_6():
    assert final_balance([50, -20, -40, 10]) == 40
    assert final_balance([]) == 0 and final_balance([-5]) == 0 and final_balance([5, -5, -1]) == 0


def test_ex_1_1_7():
    assert pairings(['ana', 'bo', 'cy']) == ['ana-bo', 'ana-cy', 'bo-cy']
    assert pairings(['solo']) == [] and len(pairings([str(i) for i in range(10)])) == 45


def test_ex_1_1_8():
    assert committees(['a', 'b', 'c', 'd']) == ['a,b,c', 'a,b,d', 'a,c,d', 'b,c,d']
    assert committees(['a', 'b']) == [] and len(committees([str(i) for i in range(10)])) == 120


def test_ex_1_1_9():
    assert newest(['a', 'b', 'c', 'd'], 2) == ['c', 'd']
    assert newest(['a'], 5) == ['a'] and newest(['a', 'b'], 0) == []


def test_ex_1_1_10():
    assert busiest_hour(['09:15', '10:02', '09:40', '11:00']) == 9
    assert busiest_hour(['10:00', '09:00']) == 9 and busiest_hour(['23:59', '23:00', '00:10']) == 23


def test_ex_1_1_11():
    assert weekly_slots(['ana']) == ['ana Mon', 'ana Tue', 'ana Wed', 'ana Thu', 'ana Fri', 'ana Sat', 'ana Sun']
    slots = weekly_slots(['ana', 'bo'])
    assert len(slots) == 14 and slots[7] == 'bo Mon' and weekly_slots([]) == []


def test_ex_1_1_12():
    assert count_vowels(['Hello', 'World']) == 3
    assert count_vowels(['AEIOU xyz', '']) == 5 and count_vowels([]) == 0


def test_ex_1_1_13():
    assert is_symmetric([[1, 2], [2, 1]]) and not is_symmetric([[1, 2], [3, 1]])
    assert is_symmetric([]) and is_symmetric([[7]])
    assert is_symmetric([[1, 2, 3], [2, 5, 6], [3, 6, 9]]) and not is_symmetric([[1, 2, 3], [2, 5, 6], [3, 0, 9]])


def test_ex_1_1_14():
    assert closest_gap([10, 4, 15, 7]) == 3
    assert closest_gap([1, 100]) == 99 and closest_gap([5, 5, 9]) == 0 and closest_gap([-3, 8, -1]) == 2


def test_ex_1_1_15():
    assert shared_hours([9, 10, 13, 15], [10, 11, 15]) == [10, 15]
    assert shared_hours([], [1]) == [] and shared_hours([8], []) == [] and shared_hours([7, 8], [8, 7]) == [7, 8]


def test_ex_1_1_16():
    assert switch_settings(2) == ['00', '01', '10', '11']
    assert switch_settings(0) == [''] and switch_settings(1) == ['0', '1']
    three = switch_settings(3)
    assert len(three) == 8 and three[0] == '000' and three[5] == '101' and three[-1] == '111'
