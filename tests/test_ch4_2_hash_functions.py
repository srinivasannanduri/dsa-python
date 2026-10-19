import random
import string
from ch4_2_hash_functions import (adversarial_keys, buckets_used, division_hash, fullest, max_bucket, mult_hash,
                                 poly_hash, RandomizedHashTable, sum_hash, UniversalHash)


KEYS = range(0, 8000, 8)


def random_words():
    rng = random.Random(1)
    return {"".join(rng.choice(string.ascii_lowercase) for _ in range(6)) for _ in range(10000)}


def test_ex_4_2_1():
    assert sum_hash("stop", 101) == sum_hash("pots", 101) == sum_hash("tops", 101)
    assert 0 <= sum_hash("anything", 7) < 7


def test_ex_4_2_2():
    assert poly_hash("stop", 10**9 + 7) != poly_hash("pots", 10**9 + 7)
    assert 0 <= poly_hash("anything", 7) < 7


def test_ex_4_2_3():
    assert buckets_used(KEYS, 64, division_hash) == 8 and buckets_used(KEYS, 61, division_hash) == 61
    assert division_hash(130, 64) == 2


def test_ex_4_2_4():
    words = random_words()
    assert max_bucket(words, 1000, poly_hash) < 30
    assert max_bucket(words, 1000, sum_hash) > 3 * max_bucket(words, 1000, poly_hash)


def test_ex_4_2_5():
    h1, h2 = UniversalHash(1000, random.Random(1)), UniversalHash(1000, random.Random(2))
    assert any(h1(k) != h2(k) for k in range(10)) and all(0 <= h1(k) < 1000 for k in range(1000))


def test_ex_4_2_6():
    adv = adversarial_keys(1000, 5000)
    assert len(adv) == 5000
    assert fullest(adv, lambda k: k % 1000) == 5000 and fullest(adv, UniversalHash(1000, random.Random(3))) < 25


def test_ex_4_2_7():
    table = RandomizedHashTable(random.Random(4))
    for k in adversarial_keys(1024, 10000):
        table.put(k, k + 1)
    assert len(table) == 10000 and all(table.get(k) == k + 1 for k in adversarial_keys(1024, 10000))
    assert table.longest_chain() < 12 and table.get(-5) is None
    table.put(0, "zero")
    assert table.get(0) == "zero" and len(table) == 10000


def test_ex_4_2_8():
    assert buckets_used(KEYS, 64, mult_hash) == 64 and all(0 <= mult_hash(k, 64) < 64 for k in KEYS)
