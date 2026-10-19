from ch6_3_union_find import (DisjointSet, earliest_connected, group_count, has_cycle_undirected, is_tree,
                             kruskal_cost, prim_cost, redundant_edge)


def test_ex_6_3_1():
    ds = DisjointSet(5)
    assert ds.union(0, 1) and not ds.union(1, 0) and ds.size(1) == 2 and ds.groups == 4
    ds = DisjointSet(6)
    assert ds.union(0, 1) and ds.union(2, 1) and not ds.union(0, 2) and ds.find(2) == ds.find(0) and ds.size(2) == 3
    root = ds.find(0)
    assert ds.union(3, 0) and ds.find(3) == root and ds.size(3) == 4 and ds.groups == 3
    chain = DisjointSet(4)
    chain.parent = [0, 0, 1, 2]
    assert chain.find(3) == 0 and chain.parent == [0, 0, 0, 0]


def test_ex_6_3_2():
    assert group_count(5, [[0, 1], [1, 2], [3, 4]]) == 2 and group_count(3, []) == 3 and group_count(4, [[0, 1], [1, 0], [2, 3], [3, 1]]) == 1


def test_ex_6_3_3():
    assert has_cycle_undirected(4, [[0, 1], [1, 2], [2, 0], [2, 3]]) and not has_cycle_undirected(4, [[0, 1], [1, 2], [2, 3]])
    assert not has_cycle_undirected(3, []) and has_cycle_undirected(5, [[3, 4], [0, 1], [1, 3], [4, 0]])


def test_ex_6_3_4():
    assert is_tree(4, [[0, 1], [0, 2], [2, 3]]) and not is_tree(4, [[0, 1], [2, 3]]) and is_tree(1, [])
    assert not is_tree(4, [[0, 1], [1, 2], [2, 0]]) and not is_tree(3, [[0, 1], [1, 2], [2, 0]])


def test_ex_6_3_5():
    assert kruskal_cost(4, [[0, 1, 4], [1, 2, 2], [0, 2, 5], [2, 3, 1], [1, 3, 7]]) == 7 and kruskal_cost(1, []) == 0
    assert kruskal_cost(3, [[0, 1, 3]]) == -1 and kruskal_cost(3, [[0, 1, -2], [1, 2, 6], [0, 2, 6]]) == 4


def test_ex_6_3_6():
    assert prim_cost(4, [[0, 1, 4], [1, 2, 2], [0, 2, 5], [2, 3, 1], [1, 3, 7]]) == 7 and prim_cost(1, []) == 0
    assert prim_cost(3, [[0, 1, 3]]) == -1 and prim_cost(3, [[0, 1, -2], [1, 2, 6], [0, 2, 6]]) == 4
    edges = [[0, 1, 9], [0, 2, 3], [1, 2, 1], [1, 3, 8], [2, 3, 7], [3, 4, 2], [2, 4, 6]]
    assert prim_cost(5, edges) == 12


def test_ex_6_3_7():
    assert redundant_edge([[0, 1], [1, 2], [2, 3], [1, 3], [3, 4]]) == [1, 3] and redundant_edge([[0, 1], [1, 2], [0, 2]]) == [0, 2]
    assert redundant_edge([[2, 3], [0, 1], [1, 3], [0, 2]]) == [0, 2]


def test_ex_6_3_8():
    assert earliest_connected(4, [[7, 2, 3], [2, 0, 1], [5, 1, 2], [9, 0, 3]]) == 7 and earliest_connected(3, [[1, 0, 1]]) == -1
    assert earliest_connected(2, [[4, 1, 0], [3, 0, 1]]) == 3 and earliest_connected(3, [[5, 0, 1], [6, 1, 0], [8, 2, 1]]) == 8
