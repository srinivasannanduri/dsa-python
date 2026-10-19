"""Chapter 5.2: Heaps and priority queues."""
import heapq
import itertools


# ==== EX 5.2.1 | Array-backed max-heap skeleton | Core | class=MaxHeap
# PROMPT: Create `MaxHeap` storing nodes in a list `data`. Add `root()`, `last()`, `__len__`, and static helpers `left_child(i)`, `right_child(i)`, `parent(i)`.
# EXAMPLE: `left_child(0)` -> `1`, `right_child(0)` -> `2`, `parent(4)` -> `1`
# BIGO: All O(1). Storing the heap in an array solves "find the last node" for free: it is the last element.
# NOTE: For index i: left child 2i + 1, right child 2i + 2, parent (i - 1) // 2.
class MaxHeap:
    def __init__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def root(self):
        raise NotImplementedError

    def last(self):
        raise NotImplementedError

    @staticmethod
    def left_child(i):
        raise NotImplementedError

    @staticmethod
    def right_child(i):
        raise NotImplementedError

    @staticmethod
    def parent(i):
        raise NotImplementedError
# ==== END

    # ==== EX 5.2.2 | Insert and trickle up | Core | class=MaxHeap
    # PROMPT: Add `insert(value)`: append it as the new last node, then swap it with its parent while it is larger than the parent.
    # EXAMPLE: insert 3, 9, 5, 12 -> `root()` is `12`
    # BIGO: O(log N): at most one swap per level of the tree.
    def insert(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.2.3 | Delete the root and trickle down | Core | class=MaxHeap
    # PROMPT: Add `delete()` returning the root: move the last node into the root, then swap it with its larger child while a child is larger.
    # EXAMPLE: After inserting 3, 9, 5, 12 -> `delete()` returns 12, 9, 5, 3 in that order
    # BIGO: O(log N).
    # NOTE: Always swap with the larger child; swapping with the smaller one would put a smaller value above a larger one.
    def delete(self):
        raise NotImplementedError
    # ==== END


# ==== EX 5.2.4 | Heap sort with your heap | Practice
# PROMPT: Write `heap_sort(values)`: insert everything into a `MaxHeap`, delete repeatedly, reverse.
# EXAMPLE: `[5, 1, 9, 3, 7]` -> `[1, 3, 5, 7, 9]`
# BIGO: O(N log N) time, O(N) space as written.
def heap_sort(values):
    raise NotImplementedError
# ==== END


# ==== EX 5.2.5 | Jobs by deadline | Core | class=DeadlineQueue
# PROMPT: Build `DeadlineQueue` with `add(job, deadline)` and `next_job()`, serving the earliest deadline first and, on a tie, whichever job was added first; `next_job()` returns `None` when empty. Use `heapq` (a min-heap) by pushing `(deadline, arrival_number, job)`.
# EXAMPLE: add ('report', 5), ('backup', 2), ('email', 2) -> next is 'backup', then 'email', then 'report'
# BIGO: O(log N) per add and per next. A sorted list would be O(N) to add.
# NOTE: A heap is not stable: without the arrival number, two jobs with the same deadline could come out in either order.
class DeadlineQueue:
    def __init__(self):
        raise NotImplementedError

    def add(self, job, deadline):
        raise NotImplementedError

    def next_job(self):
        raise NotImplementedError
# ==== END


# ==== EX 5.2.6 | Top K largest | Practice
# PROMPT: Write `top_k(nums, k)` keeping a min-heap of size k: push each number, pop when the heap grows past k. Return the k largest, largest first.
# EXAMPLE: `[3, 1, 9, 7, 5, 8]`, k = 3 -> `[9, 8, 7]`
# BIGO: O(N log K) time, O(K) space. Better than sorting when K is much smaller than N.
def top_k(nums, k):
    raise NotImplementedError
# ==== END


# ==== EX 5.2.7 | Is this array a max-heap? | Core
# PROMPT: Write `is_max_heap(arr)` checking that every parent is at least as large as its children, using the index formulas.
# EXAMPLE: `[100, 88, 25, 87, 16]` -> `True`; `[10, 20]` -> `False`
# BIGO: O(N).
def is_max_heap(arr):
    raise NotImplementedError
# ==== END


# ==== EX 5.2.8 | Merge K sorted lists | Stretch
# PROMPT: Write `merge_k_sorted(lists)` using a heap holding one `(value, list_index, element_index)` entry per list.
# EXAMPLE: `[[1, 4, 7], [2, 5], [0, 9]]` -> `[0, 1, 2, 4, 5, 7, 9]`
# BIGO: O(N log K) for N total values across K lists.
def merge_k_sorted(lists):
    raise NotImplementedError
# ==== END


# ==== EX 5.2.9 | Running median | Practice | class=RunningMedian
# PROMPT: Build `RunningMedian` with `add(x)` and `median()` (a float; at least one value has been added). Keep the lower half in a max-heap (store negatives with `heapq`) and the upper half in a min-heap, rebalancing so the lower half has the same size or one more.
# EXAMPLE: add 5 -> `5.0`; add 15 -> `10.0`; add 1 -> `5.0`; add 3 -> `4.0`
# BIGO: O(log N) per `add`, O(1) per `median`, O(N) space: a max-heap holds the lower half and a min-heap the upper half, and their tops straddle the median.
class RunningMedian:
    def __init__(self):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError

    def median(self):
        raise NotImplementedError
# ==== END


# ==== EX 5.2.10 | Sort a nearly sorted array with a heap | Practice
# PROMPT: Every value in `nums` is at most `k` positions from where it belongs in sorted order. Write `sort_nearly_sorted(nums, k)` that returns a new sorted list in O(N log K): keep a min-heap of the next `k + 1` values and repeatedly move its smallest to the output.
# EXAMPLE: `[3, 1, 2, 6, 4, 5, 9, 7, 8], 2` -> `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
# BIGO: O(N log K) time, O(K) space: the smallest remaining value is always among the next K + 1, so a heap of that size can hand it out.
# NOTE: Compare 3.1.16, which handles the same input with insertion sort in O(N * K).
def sort_nearly_sorted(nums, k):
    raise NotImplementedError
# ==== END
