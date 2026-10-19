from ch7_1_recursion import (collapse_runs, collatz_steps, dice_ways, digit_count, digit_sum, factorial, gcd,
                            headcount, is_palindrome_rec, last_standing, longest_word, max_depth, paren_strings,
                            power, running_totals, subsets, sum_recursive, tilings, to_binary)


def test_ex_7_1_1():
    assert digit_count(12345) == 5 and digit_count(0) == 1 and digit_count(9) == 1 and digit_count(10) == 2
    assert digit_count(10 ** 30) == 31


def test_ex_7_1_2():
    assert factorial(5) == 120 and factorial(0) == 1


def test_ex_7_1_3():
    assert sum_recursive([1, 2, 3, 4]) == 10 and sum_recursive([]) == 0


def test_ex_7_1_4():
    assert max_depth([1, [2, [3]], 4]) == 3 and max_depth([]) == 1 and max_depth([1, 2]) == 1
    assert max_depth([[[[]]], [1]]) == 4


def test_ex_7_1_5():
    assert power(2, 10) == 1024 and power(3, 0) == 1 and power(5, 3) == 125


def test_ex_7_1_6():
    org = ('ana', [('bo', []), ('cy', [('di', []), ('ed', [('fi', [])])])])
    assert headcount(org) == 6 and headcount(('solo', [])) == 1
    assert headcount(('ana', [('bo', []), ('cy', [('di', [])])])) == 4


def test_ex_7_1_7():
    assert to_binary(5) == '101' and to_binary(0) == '0' and to_binary(1) == '1' and to_binary(8) == '1000'
    assert to_binary(255) == '11111111'


def test_ex_7_1_8():
    data = [1, 2, 3, 4]
    assert running_totals(data) is data and data == [1, 3, 6, 10]
    assert running_totals([]) == [] and running_totals([5]) == [5] and running_totals([2, -2, 2]) == [2, 0, 2]


def test_ex_7_1_9():
    assert is_palindrome_rec('level') and not is_palindrome_rec('levels')
    assert is_palindrome_rec('') and is_palindrome_rec('x') and is_palindrome_rec('abba') and not is_palindrome_rec('abca')


def test_ex_7_1_10():
    assert digit_sum(9045) == 18 and digit_sum(0) == 0 and digit_sum(7) == 7 and digit_sum(99999) == 45


def test_ex_7_1_11():
    assert longest_word(['go', 'java', 'py', 'rust']) == 'java'
    assert longest_word([]) == '' and longest_word(['a', 'bb', 'cc']) == 'bb' and longest_word(['solo']) == 'solo'


def test_ex_7_1_12():
    assert collapse_runs([1, 1, 2, 2, 2, 3, 1]) == [1, 2, 3, 1]
    assert collapse_runs([]) == [] and collapse_runs([4, 4, 4]) == [4] and collapse_runs([1, 2, 1]) == [1, 2, 1]


def test_ex_7_1_13():
    assert collatz_steps(6) == 8 and collatz_steps(1) == 0 and collatz_steps(2) == 1 and collatz_steps(27) == 111


def test_ex_7_1_14():
    assert gcd(48, 18) == 6 and gcd(7, 0) == 7 and gcd(0, 5) == 5 and gcd(17, 5) == 1 and gcd(270, 192) == 6


def test_ex_7_1_15():
    assert [tilings(n) for n in range(8)] == [1, 1, 1, 2, 3, 4, 6, 9] and tilings(10) == 28


def test_ex_7_1_16():
    assert paren_strings(2) == ['(())', '()()'] and paren_strings(0) == ['']
    assert paren_strings(3) == ['((()))', '(()())', '(())()', '()(())', '()()()'] and len(paren_strings(5)) == 42


def test_ex_7_1_17():
    assert dice_ways(2, 7) == 6 and dice_ways(1, 7) == 0 and dice_ways(0, 0) == 1 and dice_ways(2, 2) == 1
    assert dice_ways(3, 10) == 27 and dice_ways(2, 13) == 0


def test_ex_7_1_18():
    assert sorted(map(sorted, subsets([1, 2]))) == [[], [1], [1, 2], [2]]
    assert len(subsets([1, 2, 3, 4])) == 16


def test_ex_7_1_19():
    assert last_standing(5, 2) == 3 and last_standing(1, 3) == 1 and last_standing(7, 3) == 4
    assert last_standing(6, 1) == 6 and last_standing(10, 2) == 5 and last_standing(2, 2) == 1
