"""Chapter 5.1: Binary search trees."""
from collections import deque


# ==== EX 5.1.1 | Tree node and search | Core
# PROMPT: Create `TreeNode(value, left=None, right=None)`. Write `search(node, value)` returning the node holding `value`, or `None`: go left if smaller, right if larger.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> `search(root, 33).value` is `33`; `search(root, 40)` is `None`
# BIGO: O(log N) in a balanced tree; O(N) in a degenerate one (sorted inserts make a linked list).
class TreeNode:
    def __init__(self, value, left=None, right=None):
        raise NotImplementedError


def search(node, value):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.2 | Insert | Core
# PROMPT: Write `insert(node, value)` that returns the (possibly new) root. Walk down as in search; attach a new leaf at the first empty child. Ignore duplicates.
# EXAMPLE: `root = None; for v in [50, 25, 75]: root = insert(root, v)` -> root 50, left 25, right 75
# BIGO: O(log N) balanced, O(N) worst case.
def insert(node, value):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.3 | Delete (all three cases) | Core
# PROMPT: Write `delete(node, value)` returning the new subtree root. Handle: no children (remove it), one child (the child takes its place), two children (replace the value with its successor, the smallest value in the right subtree, then delete the successor from there).
# EXAMPLE: Deleting 50 from `[50, 25, 75, 61, 89, 52]` makes 52 the new root value
# BIGO: O(log N) balanced.
def delete(node, value):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.4 | Traversals | Core
# PROMPT: Write `inorder(node)`, `preorder(node)` and `postorder(node)`, each returning a list of values.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> inorder `[10, 25, 33, 50, 75]`, preorder `[50, 25, 10, 33, 75]`, postorder `[10, 33, 25, 75, 50]`
# BIGO: O(N): every node is visited once.
# NOTE: In-order traversal of a BST always yields sorted values.
def inorder(node):
    raise NotImplementedError


def preorder(node):
    raise NotImplementedError


def postorder(node):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.5 | Minimum and maximum | Core
# PROMPT: Write `find_min(node)` and `find_max(node)` by walking only left or only right.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> `10` and `75`
# BIGO: O(log N) balanced (the height of the tree).
def find_min(node):
    raise NotImplementedError


def find_max(node):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.6 | Height | Core
# PROMPT: Write `height(node)`: the number of nodes on the longest root-to-leaf path (empty tree = 0).
# EXAMPLE: Tree from `[50, 25, 75, 10]` -> `3`; from sorted `[1, 2, 3, 4]` -> `4`
# BIGO: O(N). Compare log2(N) to the height to see how balanced a tree is.
def height(node):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.7 | Build a tree and tree-sort | Practice
# PROMPT: Write `build_bst(values)` returning the root, and `tree_sort(values)` = build, then in-order. Try sorted input and see `height`.
# EXAMPLE: `tree_sort([5, 3, 8, 1, 4])` -> `[1, 3, 4, 5, 8]`
# BIGO: O(N log N) on random input, O(N^2) on sorted input (the tree degenerates).
def build_bst(values):
    raise NotImplementedError


def tree_sort(values):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.8 | Validate a BST | Practice
# PROMPT: Write `is_valid_bst(node)`. Checking only each node's direct children is not enough: pass down the allowed `(low, high)` range.
# EXAMPLE: `TreeNode(10, TreeNode(5, None, TreeNode(12)), TreeNode(15))` -> `False` (12 sits left of 10)
# BIGO: O(N).
def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.9 | Level-order traversal | Practice
# PROMPT: Write `level_order(node)` returning a list of levels (each a list of values), using a queue.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> `[[50], [25, 75], [10, 33]]`
# BIGO: O(N) time, O(W) space for the widest level.
def level_order(node):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.10 | Count the nodes | Core
# PROMPT: Write `count_nodes(node)` recursively.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> `5`
# BIGO: O(N).
def count_nodes(node):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.11 | Closest value | Core
# PROMPT: Write `closest_value(root, target)` that returns the value in a non-empty BST nearest to `target` (on a tie, the smaller value), walking one path down as a search would.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]`, `30` -> `33`
# BIGO: O(H) time for height H, O(1) space: the search path is the only place a closer value can be, because each step away from it moves further from the target.
def closest_value(root, target):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.12 | Balanced tree from a sorted array | Practice
# PROMPT: Write `balanced_bst(values)` that builds a BST of minimum height from sorted, distinct `values` and returns its root (`None` when empty): the middle value (index `(lo + hi) // 2`) becomes the root, and each half builds a subtree the same way.
# EXAMPLE: `[1, 2, 3, 4, 5, 6, 7]` -> root `4` with children `2` and `6`
# BIGO: O(N) time, O(log N) stack: each value becomes a node once, and taking the middle each time keeps both sides within one node of each other.
def balanced_bst(values):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.13 | K-th largest value | Practice
# PROMPT: Write `kth_largest(root, k)` that returns the `k`-th largest value in a BST (`1 <= k <=` number of nodes) without visiting the whole tree: walk right subtree, node, left subtree with an explicit stack, and stop at the `k`-th node visited.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]`, `2` -> `50`
# BIGO: O(H + K) time, O(H) space: a reverse in-order walk meets values from largest down and stops at the k-th.
def kth_largest(root, k):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.14 | Rebuild a BST from its preorder | Practice
# PROMPT: `values` is the preorder listing of a BST with distinct values. Write `bst_from_preorder(values)` that rebuilds the tree in O(N) and returns its root: read values in order, and let each recursive call accept only values below the bound its parent gives it.
# EXAMPLE: `[40, 20, 10, 30, 60, 70]` -> root `40`, left `20` (children `10`, `30`), right `60` (right child `70`)
# BIGO: O(N) time, O(H) stack: each value is read once, and the upper bound passed down says when a subtree has ended.
def bst_from_preorder(values):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.15 | In-order successor | Practice
# PROMPT: Write `successor(root, value)` that returns the next larger value after `value` in a BST, or `None` when `value` is the largest. `value` need not be in the tree. Walk down from the root, remembering the last node where you turned left.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]`, `33` -> `50`; `75` -> `None`
# BIGO: O(H) time, O(1) space: every time the search turns left, that node is the best successor so far.
def successor(root, value):
    raise NotImplementedError
# ==== END


# ==== EX 5.1.16 | Repair two swapped values | Stretch
# PROMPT: Exactly two values of a BST were swapped. Write `repair_swapped(root)` that swaps them back in place without rebuilding the tree. Walk in order with an explicit stack: the first descent's larger value is one culprit, and the last descent's smaller value is the other.
# EXAMPLE: `50 -> (75 -> 10, 33), 25` (`25` and `75` swapped) -> `50 -> (25 -> 10, 33), 75`
# BIGO: O(N) time, O(H) space: in-order, a BST reads ascending, so the swapped pair shows up as one or two descents in that sequence.
def repair_swapped(root):
    raise NotImplementedError
# ==== END
