import random
from ch8_3_compact_sets import (bit_positions, BitVector, BloomFilter, BoolArraySet, confirmed_duplicates,
                               CountingBloomFilter, false_positive_rate, first_duplicate, IntBitSet,
                               measured_fp_rate, missing, optimal_params, space_report, stream_duplicates)


def vector(size, members):
    bv = BitVector(size)
    for x in members:
        bv.add(x)
    return bv


def test_ex_8_3_1():
    s = BoolArraySet(10)
    s.add(3)
    s.add(7)
    s.remove(3)
    s.add(7)
    assert 7 in s and 3 not in s and len(s) == 1


def test_ex_8_3_2():
    bv = BitVector(100)
    bv.add(42)
    assert 42 in bv and 41 not in bv and bv.data[5] == 4
    bv.remove(42)
    assert 42 not in bv
    bv.remove(42)
    assert 42 not in bv


def test_ex_8_3_3():
    bv = vector(100, (1, 5, 99))
    assert len(bv) == 3
    bv.add(5)
    assert len(bv) == 3 and len(BitVector(10)) == 0


def test_ex_8_3_4():
    a, b = vector(10, (1, 2, 3)), vector(10, (2, 3, 4))
    u, i, d = a.union(b), a.intersection(b), a.difference(b)
    assert [x for x in range(10) if x in u] == [1, 2, 3, 4]
    assert [x for x in range(10) if x in i] == [2, 3]
    assert [x for x in range(10) if x in d] == [1]


def test_ex_8_3_5():
    assert list(vector(70, (9, 2, 63))) == [2, 9, 63]
    members = set(random.Random(3).sample(range(5000), 700))
    big = vector(5000, members)
    assert list(big) == sorted(members) and len(big) == 700


def test_ex_8_3_6():
    rep = space_report(100_000)
    assert rep["bit_vector"] == 12500 and rep["bit_vector"] * 50 < rep["bool_list"] < rep["set"]


def test_ex_8_3_7():
    assert first_duplicate([4, 9, 1, 9, 4], 10) == 9 and first_duplicate([1, 2, 3], 10) is None


def test_ex_8_3_8():
    x, y = IntBitSet([1, 5]), IntBitSet([5, 7])
    assert list(x | y) == [1, 5, 7] and len(x & y) == 1 and 5 in x and 7 not in x


def test_ex_8_3_9():
    assert missing([0, 3, 1, 6], 7) == [2, 4, 5] and missing(list(range(5)), 5) == []


def test_ex_8_3_10():
    assert bit_positions("cat", 3, 32) == bit_positions("cat", 3, 32)
    assert len(bit_positions("cat", 3, 32)) == 3 and all(0 <= p < 32 for p in bit_positions("cat", 3, 32))


def test_ex_8_3_11():
    bf = BloomFilter(1000, 5)
    bf.add("apple")
    bf.add("pear")
    assert bf.might_contain("apple") and bf.might_contain("pear") and not bf.might_contain("grape")
    bf2 = BloomFilter(5000, 4)
    for i in range(300):
        bf2.add(f"w{i}")
    assert all(bf2.might_contain(f"w{i}") for i in range(300))


def test_ex_8_3_12():
    assert abs(false_positive_rate(1000, 10_000, 7) - 0.0082) < 0.0005


def test_ex_8_3_13():
    assert optimal_params(1_000_000, 0.01) == (9585059, 7)


def test_ex_8_3_14():
    measured = measured_fp_rate(1000, 10_000, 7, 20_000)
    assert abs(measured - 0.0082) < 0.005


def test_ex_8_3_15():
    items = [f"u{i}" for i in range(5000)] + [f"u{i}" for i in range(0, 5000, 50)]
    reported = stream_duplicates(items, 64_000, 6)
    real, false_alarms = confirmed_duplicates(items, 64_000, 6)
    assert len(real) == 100 and false_alarms < 20 and len(reported) >= 100


def test_ex_8_3_16():
    a, b = BloomFilter(512, 3), BloomFilter(512, 3)
    a.add("x")
    b.add("y")
    u = a.union(b)
    assert u.might_contain("x") and u.might_contain("y")


def test_ex_8_3_17():
    cb = CountingBloomFilter(1000, 4)
    cb.add("a")
    cb.add("b")
    assert cb.remove("a") and not cb.might_contain("a") and cb.might_contain("b") and not cb.remove("zzz")
