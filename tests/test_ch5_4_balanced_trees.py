import random
from ch5_4_balanced_trees import (BLACK, inorder, is_valid_treap, merge, RBNode, RED, RedBlackTree, rotate_left,
                                 rotate_right, rotations_for, split, treap_contains, treap_delete, treap_height,
                                 treap_insert, TreapNode)


def tree(keys):
    t = RedBlackTree()
    for k in keys:
        t.insert(k)
    return t


def test_ex_5_4_1():
    t = RedBlackTree()
    assert t.root is t.NIL and t.NIL.color == BLACK
    x = RBNode(2, BLACK, t.NIL)
    a, y = RBNode(1, RED, t.NIL), RBNode(4, RED, t.NIL)
    b, c = RBNode(3, BLACK, t.NIL), RBNode(5, BLACK, t.NIL)
    x.left, x.right, a.parent, y.parent = a, y, x, x
    y.left, y.right, b.parent, c.parent = b, c, y, y
    t.root = x
    t.rotate_left(x)
    assert t.root is y and y.left is x and x.parent is y and y.parent is t.NIL
    assert x.left is a and x.right is b and b.parent is x and y.right is c
    t.rotate_right(y)
    assert t.root is x and x.right is y and y.parent is x and y.left is b and b.parent is y
    assert t.rotations == 2


def test_ex_5_4_2():
    t = tree(range(1, 8))
    assert t.root.key == 2 and t.root.color == BLACK and t.size == 7
    assert not t.insert(5) and t.size == 7


def test_ex_5_4_3():
    t = RedBlackTree()
    for k in range(1, 8):
        t.insert(k)
        t.validate()
    assert tree(range(1, 1001)).validate() > 0


def test_ex_5_4_4():
    t = tree([5, 2, 8, 1])
    assert t.contains(8) and not t.contains(3) and t.inorder() == [1, 2, 5, 8]
    assert tree(range(1, 8)).inorder() == list(range(1, 8))


def test_ex_5_4_5():
    assert tree(range(1, 8)).height() == 4
    t = tree(range(1, 1001))
    assert t.height() <= t.height_bound() and t.height() <= 19


def test_ex_5_4_6():
    t = tree([20, 10, 30, 25])
    assert t.minimum().key == 10 and t.maximum() == 30
    assert t.successor(20) == 25 and t.successor(30) is None and t.successor(10) == 20


def test_ex_5_4_7():
    assert rotations_for(range(1000)) < 1000


def test_ex_5_4_8():
    rng = random.Random(11)
    for _ in range(20):
        t, keys = RedBlackTree(), set()
        for _ in range(200):
            k = rng.randrange(300)
            if rng.random() < 0.6:
                t.insert(k)
                keys.add(k)
            else:
                assert t.delete(k) == (k in keys)
                keys.discard(k)
            t.validate()
        assert t.inorder() == sorted(keys) and t.size == len(keys)
    t = tree(range(1, 101))
    for k in range(2, 101, 2):
        t.delete(k)
    t.validate()
    assert t.inorder() == list(range(1, 101, 2))


def treap(keys, rng):
    root = None
    for k in keys:
        root = treap_insert(root, k, rng)
    return root


def keys_of(node):
    return [] if node is None else keys_of(node.left) + [node.key] + keys_of(node.right)


def test_ex_5_4_9():
    top, left, a, b, c = TreapNode(5, 0.5), TreapNode(3, 0.9), TreapNode(1, 0.1), TreapNode(4, 0.2), TreapNode(7, 0.3)
    top.left, top.right, left.left, left.right = left, c, a, b
    root = rotate_right(top)
    assert root is left and root.right is top and top.left is b and keys_of(root) == [1, 3, 4, 5, 7]
    root = rotate_left(root)
    assert root is top and top.left is left and left.right is b and keys_of(root) == [1, 3, 4, 5, 7]


def test_ex_5_4_10():
    root = treap(range(10), random.Random(1))
    assert keys_of(root) == list(range(10))
    stack = [root]
    while stack:
        n = stack.pop()
        for child in (n.left, n.right):
            if child:
                assert child.priority <= n.priority
                stack.append(child)


def test_ex_5_4_11():
    root = None
    for k in [5, 2, 8]:
        root = treap_insert(root, k, random.Random(k))
    assert treap_contains(root, 8) and not treap_contains(root, 3) and not treap_contains(None, 1)


def test_ex_5_4_12():
    root = treap(range(100), random.Random(2))
    for k in range(0, 100, 3):
        root = treap_delete(root, k)
    assert keys_of(root) == [k for k in range(100) if k % 3]
    assert keys_of(treap_delete(root, 1000)) == [k for k in range(100) if k % 3]


def test_ex_5_4_13():
    root = treap(range(10), random.Random(1))
    assert inorder(root) == list(range(10)) and is_valid_treap(root)
    bad = TreapNode(5, 0.1)
    bad.left = TreapNode(2, 0.9)
    assert not is_valid_treap(bad)
    unordered = TreapNode(5, 0.9)
    unordered.left = TreapNode(7, 0.1)
    assert not is_valid_treap(unordered)


def test_ex_5_4_14():
    assert treap_height(range(1, 1001), random.Random(0)) < 40


def test_ex_5_4_15():
    root = treap(range(10), random.Random(5))
    a, b = split(root, 4)
    assert keys_of(a) == [0, 1, 2, 3] and keys_of(b) == [4, 5, 6, 7, 8, 9]
    assert is_valid_treap(a) and is_valid_treap(b)
    m = merge(a, b)
    assert keys_of(m) == list(range(10)) and is_valid_treap(m)
