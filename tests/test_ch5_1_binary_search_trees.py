import random
from ch5_1_binary_search_trees import (balanced_bst, bst_from_preorder, build_bst, closest_value, count_nodes, delete,
                                      find_max, find_min, height, inorder, insert, is_valid_bst, kth_largest,
                                      level_order, postorder, preorder, repair_swapped, search, successor, tree_sort,
                                      TreeNode)


def sample_tree():
    """50 -> (25 -> 10, 33), 75, built by hand so tests don't depend on insert."""
    return TreeNode(50, TreeNode(25, TreeNode(10), TreeNode(33)), TreeNode(75))


def grow(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


def test_ex_5_1_1():
    root = sample_tree()
    assert search(root, 33).value == 33 and search(root, 40) is None and search(None, 1) is None


def test_ex_5_1_2():
    root = grow([50, 25, 75, 10, 33])
    assert root.value == 50 and root.left.value == 25 and root.right.value == 75
    assert root.left.left.value == 10 and root.left.right.value == 33


def test_ex_5_1_3():
    r = grow([50, 25, 75, 61, 89, 52])
    r = delete(r, 50)
    assert r.value == 52 and inorder(r) == [25, 52, 61, 75, 89]
    r = delete(r, 25)  # leaf
    r = delete(r, 89)
    assert inorder(r) == [52, 61, 75]
    assert inorder(delete(r, 99)) == [52, 61, 75]
    rng = random.Random(1)
    for _ in range(100):
        vals = rng.sample(range(200), 30)
        t = grow(vals)
        for v in rng.sample(vals, 15):
            t = delete(t, v)
            vals.remove(v)
        assert inorder(t) == sorted(vals)


def test_ex_5_1_4():
    root = sample_tree()
    assert inorder(root) == [10, 25, 33, 50, 75]
    assert preorder(root) == [50, 25, 10, 33, 75]
    assert postorder(root) == [10, 33, 25, 75, 50]
    assert inorder(None) == []


def test_ex_5_1_5():
    root = sample_tree()
    assert find_min(root) == 10 and find_max(root) == 75 and find_min(None) is None


def test_ex_5_1_6():
    assert height(grow([50, 25, 75, 10])) == 3 and height(grow([1, 2, 3, 4])) == 4 and height(None) == 0


def test_ex_5_1_7():
    assert inorder(build_bst([50, 25, 75, 10, 33])) == [10, 25, 33, 50, 75]
    assert build_bst([50, 25, 75, 10, 33]).value == 50
    assert tree_sort([5, 3, 8, 1, 4]) == [1, 3, 4, 5, 8]


def test_ex_5_1_8():
    assert is_valid_bst(sample_tree())
    assert not is_valid_bst(TreeNode(10, TreeNode(5, None, TreeNode(12)), TreeNode(15)))


def test_ex_5_1_9():
    assert level_order(sample_tree()) == [[50], [25, 75], [10, 33]]


def test_ex_5_1_10():
    assert count_nodes(sample_tree()) == 5 and count_nodes(None) == 0


def test_ex_5_1_11():
    root = grow([50, 25, 75, 10, 33])
    assert [closest_value(root, t) for t in (30, 60, 29, 100, 0, 50)] == [33, 50, 25, 75, 10, 50]


def test_ex_5_1_12():
    root = balanced_bst([1, 2, 3, 4, 5, 6, 7])
    assert (root.value, root.left.value, root.right.value) == (4, 2, 6) and height(root) == 3
    ten = balanced_bst(list(range(10)))
    assert inorder(ten) == list(range(10)) and height(ten) == 4 and balanced_bst([]) is None


def test_ex_5_1_13():
    root = grow([50, 25, 75, 10, 33])
    assert [kth_largest(root, k) for k in range(1, 6)] == [75, 50, 33, 25, 10] and kth_largest(TreeNode(7), 1) == 7


def test_ex_5_1_14():
    values = [40, 20, 10, 30, 60, 70]
    root = bst_from_preorder(values)
    assert (root.value, root.left.value, root.left.left.value, root.left.right.value) == (40, 20, 10, 30)
    assert root.right.value == 60 and root.right.left is None and root.right.right.value == 70
    for values in ([40, 20, 10, 30, 60, 70], [5, 4, 3, 2, 1], [1, 2, 3], [8, 3, 1, 6, 4, 7, 10, 14, 13]):
        root = bst_from_preorder(values)
        assert preorder(root) == values and inorder(root) == sorted(values)
    assert bst_from_preorder([]) is None


def test_ex_5_1_15():
    root = grow([50, 25, 75, 10, 33])
    assert [successor(root, v) for v in (10, 25, 33, 50, 75)] == [25, 33, 50, 75, None]
    assert successor(root, 40) == 50 and successor(root, 0) == 10 and successor(None, 3) is None


def test_ex_5_1_16():
    root = TreeNode(50, TreeNode(75, TreeNode(10), TreeNode(33)), TreeNode(25))
    repair_swapped(root)
    assert (root.left.value, root.right.value) == (25, 75) and is_valid_bst(root)
    for a, b in [(10, 33), (50, 52), (10, 89), (61, 75)]:
        root = grow([50, 25, 75, 61, 89, 52, 10, 33])
        x, y = search(root, a), search(root, b)
        x.value, y.value = b, a
        repair_swapped(root)
        assert inorder(root) == [10, 25, 33, 50, 52, 61, 75, 89] and is_valid_bst(root)
