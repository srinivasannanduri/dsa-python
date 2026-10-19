import random
from ch5_5_btrees import (bst_ios, BTree, btree_height_bound, btree_ios, BTreeNode, external_binary_search,
                         ExternalArray, random_reads_ios, scan_ios)


def btree(t, keys):
    tree = BTree(t)
    for k in keys:
        tree.insert(k)
    return tree


def test_ex_5_5_1():
    assert scan_ios(1000, 64) == 16 and random_reads_ios(1000) == 1000


def test_ex_5_5_2():
    ext = ExternalArray(range(0, 20000, 2), 100)
    assert external_binary_search(ext, 4242) == 2121 and ext.ios <= 9
    assert external_binary_search(ExternalArray(range(0, 20000, 2), 100), 4243) == -1
    assert external_binary_search(ExternalArray(range(10), 3), 0) == 0
    assert external_binary_search(ExternalArray(range(10), 3), 9) == 9


def test_ex_5_5_3():
    assert bst_ios(10**9) == 30 and btree_ios(10**9, 1000) == 3


def test_ex_5_5_4():
    t = BTree(2)
    assert not t.search(1)
    left, right = BTreeNode(leaf=True), BTreeNode(leaf=True)
    left.keys, right.keys = [1, 2], [4, 5]
    t.root = BTreeNode(leaf=False)
    t.root.keys, t.root.children = [3], [left, right]
    assert all(t.search(k) for k in (1, 2, 3, 4, 5)) and not t.search(0) and not t.search(6)


def test_ex_5_5_5():
    t = btree(2, range(1, 11))
    assert t.search(7) and not t.search(11) and all(t.search(k) for k in range(1, 11))
    assert all(len(n.keys) <= 3 for n in [t.root] + t.root.children)


def test_ex_5_5_6():
    t = BTree(2)
    for k in range(1, 11):
        t.insert(k)
        t.validate()
    assert t.inorder() == list(range(1, 11))


def test_ex_5_5_7():
    assert btree_height_bound(10**6, 50) == 4
    assert btree(3, range(1, 10001)).validate() <= btree_height_bound(10000, 3)


def test_ex_5_5_8():
    t = btree(3, range(1, 101))
    assert t.range_query(40, 45) == [40, 41, 42, 43, 44, 45]
    assert t.range_query(0, 3) == [1, 2, 3] and t.range_query(200, 300) == []


def test_ex_5_5_9():
    rng = random.Random(8)
    for t_deg in (2, 3, 4):
        t, keys = BTree(t_deg), set()
        for _ in range(1500):
            k = rng.randrange(400)
            if rng.random() < 0.55:
                t.insert(k)
                keys.add(k)
            else:
                assert t.delete(k) == (k in keys)
                keys.discard(k)
        t.validate()
        assert t.inorder() == sorted(keys)
    t = btree(3, range(1, 201))
    odds = list(range(1, 201, 2))
    random.Random(3).shuffle(odds)
    for k in odds:
        t.delete(k)
    t.validate()
    assert t.inorder() == list(range(2, 201, 2))
