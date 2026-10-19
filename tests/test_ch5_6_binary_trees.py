from ch5_6_binary_trees import (diameter, evaluate, ExprNode, has_path_sum, inorder_iterative, is_balanced,
                               is_symmetric, leaf_paths, level_averages, lowest_common_ancestor, max_path_sum,
                               mirror, nodes_at_distance, parse, rebuild, right_view, serialize, total_depth,
                               TreeNode, vertical_columns, widest_level)


def tree(values):
    """Build a tree from level-order `values`, `None` for a missing child (children of a missing node are not listed)."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue, i = [root], 1
    for node in queue:
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                setattr(node, side, TreeNode(values[i]))
                queue.append(getattr(node, side))
            i += 1
        if i >= len(values):
            break
    return root


def sample():
    """1(2(4, 5(7)), 3(-, 6)), used by most tests."""
    return tree([1, 2, 3, 4, 5, None, 6, None, None, 7])


def inorder(node):
    return inorder(node.left) + [node.value] + inorder(node.right) if node else []


def preorder(node):
    return [node.value] + preorder(node.left) + preorder(node.right) if node else []


def test_ex_5_6_1():
    root = sample()
    assert [has_path_sum(root, t) for t in (10, 15, 7, 8, 3)] == [True, True, True, False, False]
    assert not has_path_sum(None, 0) and has_path_sum(TreeNode(5), 5)


def test_ex_5_6_2():
    assert total_depth(sample()) == 11 and total_depth(None) == 0 and total_depth(TreeNode(1)) == 0
    assert total_depth(tree([1, 2, None, 3])) == 3 and total_depth(tree([1, 2, 3, 4, 5, 6, 7])) == 10


def test_ex_5_6_3():
    root = sample()
    assert mirror(root) is root and inorder(root) == [6, 3, 1, 5, 7, 2, 4] and root.left.value == 3
    assert mirror(None) is None and inorder(mirror(mirror(sample()))) == inorder(sample())


def test_ex_5_6_4():
    assert is_symmetric(tree([1, 2, 2, 3, 4, 4, 3])) and not is_symmetric(tree([1, 2, 2, None, 3, None, 3]))
    assert is_symmetric(None) and is_symmetric(TreeNode(1)) and not is_symmetric(tree([1, 2, 3])) and not is_symmetric(sample())


def test_ex_5_6_5():
    assert right_view(sample()) == [1, 3, 6, 7] and right_view(tree([1, 2, 3, 4])) == [1, 3, 4] and right_view(None) == []


def test_ex_5_6_6():
    assert level_averages(sample()) == [1.0, 2.5, 5.0, 7.0] and level_averages(None) == []
    assert level_averages(tree([3, -1, 2])) == [3.0, 0.5]


def test_ex_5_6_7():
    assert leaf_paths(sample()) == [[1, 2, 4], [1, 2, 5, 7], [1, 3, 6]] and leaf_paths(None) == [] and leaf_paths(TreeNode(9)) == [[9]]


def test_ex_5_6_8():
    assert inorder_iterative(sample()) == [4, 2, 7, 5, 1, 3, 6] and inorder_iterative(None) == []
    deep = tree([1, 2, None, 3, None, 4])
    assert inorder_iterative(deep) == inorder(deep) == [4, 3, 2, 1]


def test_ex_5_6_9():
    E = ExprNode
    assert evaluate(E("*", E("+", E("3"), E("4")), E("-", E("5"), E("2")))) == 21 and evaluate(E("7")) == 7
    assert evaluate(E("-", E("2"), E("-9"))) == 11 and evaluate(E("-", E("-", E("10"), E("4")), E("3"))) == 3


def test_ex_5_6_10():
    assert diameter(sample()) == 5 and diameter(None) == 0 and diameter(TreeNode(1)) == 0 and diameter(tree([1, 2, 3])) == 2
    assert diameter(tree([1, 2, None, 3, 4, 5, None, None, 6])) == 4


def test_ex_5_6_11():
    assert is_balanced(sample()) and not is_balanced(tree([1, 2, None, 3])) and is_balanced(None)
    assert not is_balanced(tree([1, 2, 3, 4, None, None, None, 5])) and is_balanced(tree([1, 2, 3, 4]))


def test_ex_5_6_12():
    assert widest_level(sample()) == 4 and widest_level(tree([1, 2, 3, 4, None, None, 5])) == 4 and widest_level(None) == 0
    assert widest_level(tree([1, 2, None, 3])) == 1 and widest_level(tree([1, 2, 3])) == 2


def test_ex_5_6_13():
    root = sample()
    pairs = [(4, 7), (7, 6), (5, 7), (3, 6), (4, 4)]
    assert [lowest_common_ancestor(root, a, b).value for a, b in pairs] == [2, 1, 5, 3, 4]


def test_ex_5_6_14():
    text = "1,2,4,#,#,5,7,#,#,#,3,#,6,#,#"
    assert serialize(sample()) == text and serialize(parse(text)) == text and inorder(parse(text)) == inorder(sample())
    assert serialize(None) == "#" and parse("#") is None and serialize(parse(serialize(tree([-1, 20])))) == "-1,20,#,#,#"


def test_ex_5_6_15():
    assert vertical_columns(sample()) == [[4], [2, 7], [1, 5], [3], [6]] and vertical_columns(None) == []
    assert vertical_columns(tree([1, 2, 3, None, 4, 5])) == [[2], [1, 4, 5], [3]]


def test_ex_5_6_16():
    root = sample()
    cases = [(5, 2, [1, 4]), (5, 0, [5]), (4, 3, [3, 7]), (1, 2, [4, 5, 6]), (7, 5, [6]), (7, 9, [])]
    assert [nodes_at_distance(root, target, k) for target, k, _ in cases] == [want for _, _, want in cases]


def test_ex_5_6_17():
    assert max_path_sum(tree([2, -1, 3, 4, -6, None, 5])) == 13 and max_path_sum(tree([-5, -2, -7])) == -2
    assert max_path_sum(TreeNode(7)) == 7 and max_path_sum(sample()) == 24 and max_path_sum(tree([1, -9, -9])) == 1


def test_ex_5_6_18():
    root = rebuild([1, 2, 4, 5, 7, 3, 6], [4, 2, 7, 5, 1, 3, 6])
    assert root.left.right.left.value == 7 and root.right.right.value == 6 and rebuild([], []) is None
    for t in (sample(), tree([1, 2, None, 3]), tree([5, None, 8, 6]), TreeNode(4)):
        again = rebuild(preorder(t), inorder(t))
        assert preorder(again) == preorder(t) and inorder(again) == inorder(t)
