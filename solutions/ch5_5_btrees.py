"""Chapter 5.5: B-trees and block storage."""
import bisect
import math


# ==== EX 5.5.1 | Count I/Os, not steps | Core
# PROMPT: Memory moves in blocks of B items. Write `scan_ios(n, B)` for reading n items in order, and `random_reads_ios(k)` for k reads that each land in a different block.
# EXAMPLE: `scan_ios(1000, 64)` -> `16`; `random_reads_ios(1000)` -> `1000`
# BIGO: A scan costs O(N / B) I/Os; scattered access costs one I/O per item. On disk, I/Os dominate the running time.
def scan_ios(n, B):
    raise NotImplementedError


def random_reads_ios(k):
    raise NotImplementedError
# ==== END


# ==== EX 5.5.2 | Binary search over blocks | Core
# PROMPT: Write `ExternalArray(data, B)` whose `read_block(i)` returns block i and counts one I/O, and `external_binary_search(ext, target)` that binary-searches the blocks by their first item, then searches inside one block in memory.
# EXAMPLE: 10,000 sorted items with B = 100 -> a lookup costs about 8 I/Os, versus about 14 for plain binary search touching one block per probe
# BIGO: O(log(N / B)) I/Os, a small saving; the B-tree (5.5.4) does much better with O(log_B N).
class ExternalArray:
    def __init__(self, data, B):
        raise NotImplementedError

    def read_block(self, i):
        raise NotImplementedError


def external_binary_search(ext, target):
    raise NotImplementedError
# ==== END


# ==== EX 5.5.3 | Lookups: BST versus B-tree | Core
# PROMPT: Write `bst_ios(n)` (one I/O per level of a balanced binary tree, log2 N) and `btree_ios(n, B)` (log base B of N) and compare them for a billion keys.
# EXAMPLE: `bst_ios(10**9)` -> `30`; `btree_ios(10**9, 1000)` -> `3`
# BIGO: O(log_2 N) versus O(log_B N) I/Os: a factor of log2 B fewer.
def bst_ios(n):
    raise NotImplementedError


def btree_ios(n, B):
    raise NotImplementedError
# ==== END


# ==== EX 5.5.4 | B-tree nodes and search | Core | class=BTree
# PROMPT: Create `BTreeNode(leaf)` with sorted `keys` and `children`, and `BTree(t)` with a `search(key)` that binary-searches each node's keys and descends into the right child.
# EXAMPLE: in a B-tree holding 1..100 -> `search(42)` is `True`, `search(101)` is `False`
# BIGO: O(log_t N) nodes visited, O(log t) comparisons in each.
class BTreeNode:
    def __init__(self, leaf=True):
        raise NotImplementedError


class BTree:
    def __init__(self, t=3):
        raise NotImplementedError

    def search(self, key, node=None):
        raise NotImplementedError
# ==== END

    # ==== EX 5.5.5 | Insert with proactive splits | Core | class=BTree
    # PROMPT: Add `insert(key)`: if the root is full (2t - 1 keys), split it and grow a new root. Walk down, splitting any full child before entering it, so a leaf always has room.
    # EXAMPLE: t = 2, insert 1..10 -> `validate()` passes and every leaf sits at the same depth
    # BIGO: O(t log_t N) CPU, O(log_t N) node reads. The tree grows only at the root, which keeps it perfectly balanced.
    def split_child(self, parent, i):
        raise NotImplementedError

    def insert(self, key):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.5.6 | Validate and walk in order | Core | class=BTree
    # PROMPT: Add `inorder()` returning all keys sorted, and `validate()` that checks key counts per node, sorted keys, child counts, and that all leaves share one depth. Return the height.
    # EXAMPLE: after random inserts and deletes -> `inorder()` equals the sorted set of keys and `validate()` returns the height
    # BIGO: O(N).
    def inorder(self, node=None):
        raise NotImplementedError

    def validate(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.5.8 | Range queries, like a database index | Practice | class=BTree
    # PROMPT: Add `range_query(lo, hi)` returning the keys in [lo, hi] in order, skipping whole subtrees that cannot contain them.
    # EXAMPLE: B-tree of 1..100 -> `range_query(40, 45)` is `[40, 41, 42, 43, 44, 45]`
    # BIGO: O(log_t N + K / t) node visits for K results. This is why databases index with B-trees.
    def range_query(self, lo, hi, node=None, out=None):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.5.9 | Deletion | Stretch | class=BTree
    # PROMPT: Add `delete(key)`. Before descending into a child with only t - 1 keys, top it up by borrowing from a sibling or merging with one. Delete from a leaf directly; for an internal key, replace it with its predecessor or successor, or merge. Shrink the root when it empties.
    # EXAMPLE: t = 3, insert 1..200, delete the odd keys in shuffled order -> `validate()` passes and `inorder()` is the even keys
    # BIGO: O(log_t N) node visits.
    def delete(self, key):
        raise NotImplementedError

    def _delete(self, node, key):
        raise NotImplementedError

    def _merge(self, node, i):
        raise NotImplementedError
    # ==== END


# ==== EX 5.5.7 | How tall can a B-tree get? | Core
# PROMPT: Write `btree_height_bound(n, t)` returning the most levels a B-tree of minimum degree t with n keys can have: 1 + floor(log_t((n + 1) / 2)). Check it against real trees.
# EXAMPLE: `btree_height_bound(10**6, 50)` -> `4`; a real tree of 1..10,000 with t = 3 stays within its bound of 8
# BIGO: O(1). With t in the hundreds, a billion keys fit in 4 or 5 levels.
def btree_height_bound(n, t):
    raise NotImplementedError
# ==== END
