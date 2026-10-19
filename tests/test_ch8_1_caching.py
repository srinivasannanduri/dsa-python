import random
from ch8_1_caching import (blocked_transpose, cyclic_requests, FIFOCache, hit_rate, LinkedLRU, lru_memo, LRUCache,
                          RandomCache, sum_columns_first, sum_rows_first)


def check_lru(cls):
    c = cls(2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1
    c.put("c", 3)
    assert c.get("b") is None and c.get("a") == 1 and c.get("c") == 3
    c.put("a", 10)
    assert c.get("a") == 10


def test_ex_8_1_1():
    check_lru(LRUCache)


def test_ex_8_1_2():
    check_lru(LinkedLRU)
    rng = random.Random(4)
    ref, test = LRUCache(5), LinkedLRU(5)
    for _ in range(2000):
        k = rng.randrange(12)
        if rng.random() < 0.5:
            assert ref.get(k) == test.get(k)
        else:
            v = rng.random()
            ref.put(k, v)
            test.put(k, v)


def test_ex_8_1_3():
    assert abs(hit_rate(LRUCache(2), ["a", "b", "a", "a", "c", "b"]) - 2 / 6) < 1e-9


def test_ex_8_1_4():
    c = FIFOCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a")
    c.put("c", 3)
    assert c.get("a") is None and c.get("b") == 2 and c.get("c") == 3
    rng = random.Random(9)
    hot = [rng.choice("ab") if rng.random() < 0.7 else str(rng.randrange(50)) for _ in range(3000)]
    assert hit_rate(LRUCache(5), hot) > hit_rate(FIFOCache(5), hot)


def test_ex_8_1_5():
    rc = RandomCache(3, random.Random(1))
    for k in range(20):
        rc.put(k, k)
        assert len(rc.data) <= 3 and len(rc.keys) == len(rc.data) == len(rc.pos)
        assert all(rc.keys[rc.pos[x]] == x for x in rc.keys)
    assert all(rc.get(k) == k for k in rc.keys)


def test_ex_8_1_6():
    req = cyclic_requests(10, 100)
    assert hit_rate(LRUCache(10), req) == 0.0 and hit_rate(RandomCache(10, random.Random(1)), req) > 0.5


def test_ex_8_1_7():
    @lru_memo(2)
    def square(x):
        return x * x

    assert [square(1), square(2), square(1)] == [1, 4, 1] and (square.hits, square.misses) == (1, 2)

    @lru_memo(4)
    def nothing(x):
        return None

    nothing(1)
    nothing(1)
    assert nothing.hits == 1


def test_ex_8_1_8():
    g = [[1, 2], [3, 4]]
    assert sum_rows_first(g) == 10 == sum_columns_first(g)
    assert blocked_transpose([[1, 2, 3], [4, 5, 6]], 2) == [[1, 4], [2, 5], [3, 6]]
    m = [[r * 7 + c for c in range(7)] for r in range(5)]
    assert blocked_transpose(m, 3) == [list(col) for col in zip(*m)]
