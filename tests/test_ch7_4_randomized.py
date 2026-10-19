import random
from ch7_4_randomized import (birthday_exact, birthday_simulation, bst_height, estimate_pi, exact_mean, fermat_test,
                             fermat_witness, fisher_yates, fisher_yates_distribution, is_prime_trial,
                             las_vegas_find_one, lcg, lcg_period, make_weighted_picker, max_load_random,
                             max_load_two_choices, miller_rabin, monte_carlo_find_one, naive_distribution,
                             random_quicksort, reservoir, sample_with_seed, sampled_mean)


def test_ex_7_4_1():
    rng = random.Random(0)
    for _ in range(60):
        data = [rng.randint(-30, 30) for _ in range(rng.randint(0, 40))]
        assert random_quicksort(data, random.Random(3)) == sorted(data)
    assert random_quicksort(list(range(10)), random.Random(1)) == list(range(10))


def test_ex_7_4_2():
    assert sample_with_seed(42, range(100), 3) == sample_with_seed(42, range(100), 3)
    assert len(sample_with_seed(42, range(100), 3)) == 3


def test_ex_7_4_3():
    g = lcg(1, 5, 3, 16)
    assert [next(g) for _ in range(3)] == [8, 11, 10]
    assert lcg_period(1, 5, 3, 16) == 16


def test_ex_7_4_4():
    a = fisher_yates([1, 2, 3, 4, 5], random.Random(7))
    assert sorted(a) == [1, 2, 3, 4, 5]
    assert fisher_yates([1, 2, 3, 4, 5], random.Random(7)) == a


def test_ex_7_4_5():
    fy = fisher_yates_distribution(3)
    assert len(fy) == 6 and set(fy.values()) == {1}
    nv = naive_distribution(3)
    assert sum(nv.values()) == 27 and sorted(nv.values()) == [4, 4, 4, 5, 5, 5]
    assert set(fisher_yates_distribution(4).values()) == {1}


def test_ex_7_4_6():
    assert bst_height(list(range(200))) == 200
    keys = list(range(200))
    random.Random(3).shuffle(keys)
    assert bst_height(keys) < 30


def test_ex_7_4_7():
    s = reservoir(range(10**5), 3, random.Random(0))
    assert len(s) == 3 and len(set(s)) == 3
    firsts = [reservoir(range(10), 1, random.Random(i))[0] for i in range(5000)]
    assert all(350 < firsts.count(v) < 650 for v in range(10))


def test_ex_7_4_8():
    one = max_load_random(10000, 1000, random.Random(5))
    two = max_load_two_choices(10000, 1000, random.Random(5))
    assert two < one and two <= 14


def test_ex_7_4_9():
    pick = make_weighted_picker([1, 3, 6], random.Random(2))
    picks = [pick() for _ in range(10000)]
    assert 5600 < picks.count(2) < 6400 and set(picks) == {0, 1, 2}


def test_ex_7_4_10():
    assert abs(estimate_pi(100_000, random.Random(0)) - 3.14159) < 0.02


def test_ex_7_4_11():
    rng = random.Random(4)
    data = [rng.randint(0, 1000) for _ in range(10**6)]
    assert abs(sampled_mean(data, 2000, random.Random(1)) / exact_mean(data) - 1) < 0.04
    assert exact_mean([1, 2, 3, 6]) == 3


def test_ex_7_4_12():
    arr = [i % 2 for i in range(1000)]
    assert arr[las_vegas_find_one(arr, random.Random(2))] == 1
    i = monte_carlo_find_one(arr, random.Random(2), 20)
    assert i == -1 or arr[i] == 1
    assert monte_carlo_find_one([0] * 10, random.Random(2), 20) == -1


def test_ex_7_4_13():
    assert is_prime_trial(999_999_000_001) and not is_prime_trial(1) and not is_prime_trial(999_999_000_001 * 3)
    assert [n for n in range(20) if is_prime_trial(n)] == [2, 3, 5, 7, 11, 13, 17, 19]


def test_ex_7_4_14():
    assert fermat_witness(2, 15) and not fermat_witness(2, 13) and not fermat_witness(2, 561)


def test_ex_7_4_15():
    rng = random.Random(6)
    assert fermat_test(10**9 + 7, 20, rng) and not fermat_test(1_000_000_007 * 998_244_353, 20, rng)


def test_ex_7_4_16():
    assert miller_rabin(999_999_000_001)
    assert not miller_rabin(561) and miller_rabin(2**61 - 1) and not miller_rabin(1)
    for n in range(2, 3000):
        assert miller_rabin(n) == all(n % d for d in range(2, int(n ** 0.5) + 1))
    for c in (561, 1105, 1729, 2465, 2821, 6601):
        assert not miller_rabin(c)


def test_ex_7_4_17():
    assert abs(birthday_exact(23) - 0.5073) < 1e-3
    assert abs(birthday_simulation(23, 20000, random.Random(3)) - 0.5073) < 0.02
