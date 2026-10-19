import random
from ch1_3_timing import bench, bench_sort, count_runs, growth_exponent, quicksort_comparisons, race, time_once


def test_ex_1_3_1():
    r, secs = time_once(sum, range(10**5))
    assert r == sum(range(10**5)) and secs >= 0


def test_ex_1_3_2():
    assert bench(lambda: sorted(range(100)), number=10, repeat=2) > 0


def test_ex_1_3_3():
    data = list(range(1000, 0, -1))
    assert bench_sort(list.sort, data, repeat=2) > 0
    assert data == list(range(1000, 0, -1))  # each run sorts a fresh copy


def test_ex_1_3_4():
    assert abs(growth_exponent({1000: 0.01, 2000: 0.04, 4000: 0.16}) - 2.0) < 1e-9
    assert abs(growth_exponent({10: 1.0, 100: 10.0, 1000: 100.0}) - 1.0) < 1e-9


def test_ex_1_3_5():
    data = [random.Random(1).random() for _ in range(2000)]
    names = race({"builtin": sorted, "reverse_twice": lambda a: sorted(a, reverse=True)[::-1]}, data)
    assert set(names) == {"builtin", "reverse_twice"} and len(names) == 2


def test_ex_1_3_6():
    assert quicksort_comparisons(list(range(100))) == 4950
    shuffled = list(range(100))
    random.Random(1).shuffle(shuffled)
    assert quicksort_comparisons(shuffled) < 1500


def test_ex_1_3_7():
    assert count_runs([1, 2, 3, 2, 5, 6, 1]) == 3 and count_runs(list(range(9))) == 1 and count_runs([]) == 0
