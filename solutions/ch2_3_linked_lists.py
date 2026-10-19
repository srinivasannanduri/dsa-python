"""Chapter 2.3: Linked lists."""


# ==== EX 2.3.1 | Node and LinkedList skeleton | Core | class=LinkedList
# PROMPT: Create `Node(data)` with `data` and `next`, and `LinkedList` with `head`. Add `__len__` and `to_list()` that walk the chain, plus a `from_list(values)` class method for tests.
# EXAMPLE: `LinkedList.from_list([1, 2, 3]).to_list()` -> `[1, 2, 3]`
# BIGO: `__len__` and `to_list` are O(N): there is no length stored, so every node must be visited.
# NOTE: Nodes can live anywhere in memory; each one only knows where the next one is. That is what makes reading slow and insertion at the head fast.
class Node:
    def __init__(self, data, next_node=None):
        raise NotImplementedError


class LinkedList:
    def __init__(self, head=None):
        raise NotImplementedError

    @classmethod
    def from_list(cls, values):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def to_list(self):
        raise NotImplementedError
# ==== END

    # ==== EX 2.3.2 | Read by index | Core | class=LinkedList
    # PROMPT: Add `read(index)`: follow `next` links `index` times. Return `None` if the list is too short.
    # EXAMPLE: `[10, 20, 30]` -> `read(2)` is `30`; `read(5)` is `None`
    # BIGO: O(N). An array reads in O(1); this is the linked list's biggest cost.
    def read(self, index):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.3 | Search for a value | Core | class=LinkedList
    # PROMPT: Add `index_of(value)` returning the position of the first match, or `None`.
    # EXAMPLE: `[10, 20, 30]` -> `index_of(20)` is `1`
    # BIGO: O(N), the same as linear search in an array.
    def index_of(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.4 | Insert at the start | Core | class=LinkedList
    # PROMPT: Add `insert_at_start(value)`: the new node points at the old head and becomes the head.
    # EXAMPLE: `[2, 3]` -> `insert_at_start(1)` -> `[1, 2, 3]`
    # BIGO: O(1). The array's worst case is the linked list's best case.
    def insert_at_start(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.5 | Insert at the end | Core | class=LinkedList
    # PROMPT: Add `insert_at_end(value)`: walk to the last node and attach the new one. Handle the empty list.
    # EXAMPLE: `[1, 2]` -> `insert_at_end(3)` -> `[1, 2, 3]`
    # BIGO: O(N) without a tail pointer (see 2.3.15 for O(1)).
    def insert_at_end(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.6 | Insert at an index | Core | class=LinkedList
    # PROMPT: Add `insert_at(index, value)`: walk to the node just before `index`, then rewire two links. Raise `IndexError` if `index` is past the end.
    # EXAMPLE: `[1, 2, 4]` -> `insert_at(2, 3)` -> `[1, 2, 3, 4]`
    # BIGO: O(N) to find the spot, then O(1) to insert. No shifting, unlike an array.
    # NOTE: Set `new_node.next` before changing `prev.next`, or the rest of the list is lost.
    def insert_at(self, index, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.7 | Delete at the start | Core | class=LinkedList
    # PROMPT: Add `delete_at_start()` returning the removed value (or `None` if empty): move `head` to `head.next`.
    # EXAMPLE: `[1, 2, 3]` -> returns `1`, leaves `[2, 3]`
    # BIGO: O(1). Arrays need O(N) here.
    def delete_at_start(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.8 | Delete at the end | Core | class=LinkedList
    # PROMPT: Add `delete_at_end()` returning the removed value: find the second-to-last node and cut its link. Handle 0 and 1 nodes.
    # EXAMPLE: `[1, 2, 3]` -> returns `3`, leaves `[1, 2]`
    # BIGO: O(N) in a singly linked list, because you need the node before the last one.
    def delete_at_end(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.9 | Delete at an index | Core | class=LinkedList
    # PROMPT: Add `delete_at(index)` returning the removed value: point the previous node's `next` past the doomed node. Raise `IndexError` if out of range.
    # EXAMPLE: `[1, 2, 9, 3]` -> `delete_at(2)` returns `9`, leaves `[1, 2, 3]`
    # BIGO: O(N) to reach it, O(1) to unlink.
    def delete_at(self, index):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.10 | Delete by value | Core | class=LinkedList
    # PROMPT: Add `delete_value(value)` that removes the first matching node and returns `True`, or `False`.
    # EXAMPLE: `[4, 5, 4]` -> `delete_value(4)` -> `[5, 4]`
    # BIGO: O(N).
    def delete_value(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.11 | Split a list into halves | Practice | class=LinkedList
    # PROMPT: Add `split_half()`: cut the list after its middle node (the first half keeps the extra node when the count is odd) and return a new `LinkedList` holding the second half. Find the cut with a slow pointer that moves one step and a fast pointer that moves two.
    # EXAMPLE: `[1, 2, 3, 4, 5]` -> the list keeps `[1, 2, 3]`, the result is `[4, 5]`
    # BIGO: O(N) time, O(1) extra space: one walk with two pointers, and no nodes are copied.
    def split_half(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.12 | Reverse in place | Core | class=LinkedList
    # PROMPT: Add `reverse()` that flips every `next` link using `previous`, `current` and `next` variables.
    # EXAMPLE: `[1, 2, 3]` -> `[3, 2, 1]`
    # BIGO: O(N) time, O(1) space.
    def reverse(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.3.14 | Detect a cycle | Stretch | class=LinkedList
    # PROMPT: Add `has_cycle()` using Floyd's slow/fast pointers: if they ever meet, the list loops.
    # EXAMPLE: A list whose last node points back to its second node -> `True`
    # BIGO: O(N) time, O(1) space (a set of visited nodes would be O(N) space).
    def has_cycle(self):
        raise NotImplementedError
    # ==== END


# ==== EX 2.3.13 | Merge two sorted lists by relinking | Practice
# PROMPT: Write `merge_sorted_lists(a, b)` for two `LinkedList`s sorted in increasing order, returning a `LinkedList` that holds every node of both in order. Relink the existing nodes (a placeholder node at the front keeps the code short); do not create a node per value.
# EXAMPLE: `[1, 4, 7]`, `[2, 3, 9]` -> `[1, 2, 3, 4, 7, 9]`
# BIGO: O(N + M) time, O(1) extra space: the existing nodes are relinked, never copied.
def merge_sorted_lists(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.15 | Doubly linked list | Core | class=DoublyLinkedList
# PROMPT: Build `DoublyLinkedList` with `head` and `tail` and nodes holding `prev` and `next`. Implement `insert_at_start`, `insert_at_end`, `delete_at_start`, `delete_at_end`, `to_list()` and `to_list_reversed()` (walk back from the tail).
# EXAMPLE: insert_at_end 2, insert_at_start 1, insert_at_end 3 -> `[1, 2, 3]`; reversed `[3, 2, 1]`
# BIGO: O(1) at both ends, because the tail pointer and `prev` links remove the walk.
class DNode:
    def __init__(self, data):
        raise NotImplementedError


class DoublyLinkedList:
    def __init__(self):
        raise NotImplementedError

    def insert_at_start(self, value):
        raise NotImplementedError

    def insert_at_end(self, value):
        raise NotImplementedError

    def delete_at_start(self):
        raise NotImplementedError

    def delete_at_end(self):
        raise NotImplementedError

    def to_list(self):
        raise NotImplementedError

    def to_list_reversed(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.3.16 | Queue on a doubly linked list | Core | class=LinkedQueue
# PROMPT: Build `LinkedQueue` with `enqueue`, `dequeue` and `read` on top of your `DoublyLinkedList`.
# EXAMPLE: enqueue 1, 2, 3 -> dequeue `1`, read `2`
# BIGO: O(1) for every operation: insert at the tail, remove from the head.
class LinkedQueue:
    def __init__(self):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.3.17 | Remove the k-th node from the end | Core
# PROMPT: Write `remove_kth_from_end(lst, k)` that unlinks the `k`-th node from the end of a `LinkedList` (`1 <= k <= len`) in one pass and returns its value: move a lead pointer `k` steps ahead of a trailing one, then move both until the lead reaches the last node. A placeholder node in front handles removing the head.
# EXAMPLE: `[1, 2, 3, 4, 5], 2` -> returns `4`; the list is `[1, 2, 3, 5]`
# BIGO: O(N) time, O(1) space, one pass: a lead pointer k nodes ahead reaches the end exactly when the trailing pointer sits before the node to remove.
def remove_kth_from_end(lst, k):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.18 | Add numbers stored as lists | Practice
# PROMPT: Each `LinkedList` holds the digits of a non-negative number, least significant first (`[9, 4, 1]` is 149). Write `add_digit_lists(a, b)` that returns a new `LinkedList` holding the digits of the sum in the same order, walking both lists once with a carry.
# EXAMPLE: `[9, 4, 1]`, `[3, 8]` -> `[2, 3, 2]` (149 + 83 = 232)
# BIGO: O(N + M) time and O(max(N, M)) space for the result: one walk down both lists with a carry, like adding on paper.
def add_digit_lists(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.19 | Where two lists meet | Practice
# PROMPT: Two `LinkedList`s may share their tail nodes. Write `meeting_node(a, b)` that returns the first node they share (the same object), or `None`, with O(1) extra space: walk one pointer down each list, and when a pointer runs off the end, restart it at the head of the other list.
# EXAMPLE: `[1, 2]` then shared `[8, 9]`, and `[5]` then the same `[8, 9]` -> the node holding `8`
# BIGO: O(N + M) time, O(1) space: after switching lists once, both pointers have walked the same distance when they reach the shared part.
def meeting_node(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.20 | Palindrome list | Practice
# PROMPT: Write `is_palindrome_list(lst)`: `True` when the values of a `LinkedList` read the same both ways, using O(1) extra space. Find the middle, reverse the second half, compare the halves, and reverse the second half again so the list ends up unchanged.
# EXAMPLE: `[1, 2, 3, 2, 1]` -> `True`; `[1, 2]` -> `False`
# BIGO: O(N) time, O(1) space: find the middle with slow and fast pointers, reverse the second half to compare, then reverse it back.
def is_palindrome_list(lst):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.21 | Rotate a list by k | Core
# PROMPT: Write `rotate_right(lst, k)` that rotates a `LinkedList` right by `k` places in place: the last `k` nodes move to the front in order. `k` may exceed the length. Find the length and tail, close the ring, and cut it before the new head.
# EXAMPLE: `[1, 2, 3, 4, 5], 2` -> `[4, 5, 1, 2, 3]`
# BIGO: O(N) time, O(1) space: one walk finds the length and tail, a second finds the new tail; three link changes do the rest.
def rotate_right(lst, k):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.22 | Interleave with the reversed second half | Stretch
# PROMPT: Write `interleave_ends(lst)` that reorders a `LinkedList` in place to first, last, second, second-to-last, and so on, by relinking nodes: cut the list at its middle, reverse the second half, then alternate nodes from the two halves.
# EXAMPLE: `[1, 2, 3, 4, 5]` -> `[1, 5, 2, 4, 3]`; `[1, 2, 3, 4]` -> `[1, 4, 2, 3]`
# BIGO: O(N) time, O(1) space: split at the middle, reverse the second half, then zip the two halves together by relinking.
def interleave_ends(lst):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.23 | Swap adjacent pairs | Practice
# PROMPT: Write `swap_pairs(lst)` that swaps every two neighbouring nodes of a `LinkedList` in place by relinking them (not by swapping values); an odd last node stays put.
# EXAMPLE: `[1, 2, 3, 4, 5]` -> `[2, 1, 4, 3, 5]`
# BIGO: O(N) time, O(1) space: each pair needs three link changes, and a placeholder node in front makes the first pair like the rest.
def swap_pairs(lst):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.24 | Mergesort a linked list | Stretch
# PROMPT: Write `sort_list(lst)` that sorts a `LinkedList` in place by relinking its nodes, in O(N log N): split the chain at its middle with slow and fast pointers, sort each half recursively, and merge the two sorted chains (equal values keep their order).
# EXAMPLE: `[5, 1, 4, 2, 3, 1]` -> `[1, 1, 2, 3, 4, 5]`
# BIGO: O(N log N) time, O(log N) stack: splitting at the middle costs a walk, and merging relinks nodes, so no buffer is needed.
# NOTE: Mergesort suits linked lists better than arrays: the merge needs no extra array, and nothing needs random access.
def sort_list(lst):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.25 | Drop duplicates from a sorted list | Core
# PROMPT: Write `drop_sorted_duplicates(lst)` that unlinks repeated values from a sorted `LinkedList` in place, keeping the first node of each value.
# EXAMPLE: `[1, 1, 2, 3, 3, 3]` -> `[1, 2, 3]`
# BIGO: O(N) time, O(1) space: in a sorted list every copy of a value sits next to the first one, so each node is compared once with its successor.
def drop_sorted_duplicates(lst):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.26 | Partition a list around a value | Practice
# PROMPT: Write `partition_list(lst, x)` that relinks a `LinkedList` in place so every node below `x` comes before every node at or above `x`, keeping the original order within each group. Build two chains behind two placeholder nodes, then join them.
# EXAMPLE: `[4, 1, 6, 2, 5, 2], 4` -> `[1, 2, 2, 4, 6, 5]`
# BIGO: O(N) time, O(1) space: nodes are relinked onto two chains, which are then joined.
def partition_list(lst, x):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.27 | Flatten a multilevel list | Stretch
# PROMPT: Create `MultiNode(data, next_node=None, child=None)`: a node whose `child` may start another list, which may have children of its own. Write `flatten(head)` that relinks everything into one list through `next`, in place, with each child list inserted right after its parent and before the parent's old `next`; set every `child` to `None` and return `head`. Save pending `next` nodes on a stack.
# EXAMPLE: `1-2-3-4`, `2` has child `5-6`, `5` has child `7`, `4` has child `8` -> `[1, 2, 5, 7, 6, 3, 4, 8]`
# BIGO: O(N) time, O(D) space for nesting depth D: each node is visited once, and the stack holds one saved `next` per open level.
class MultiNode:
    def __init__(self, data, next_node=None, child=None):
        raise NotImplementedError


def flatten(head):
    raise NotImplementedError
# ==== END


# ==== EX 2.3.28 | Cycle in a number sequence | Practice
# PROMPT: Repeatedly applying `step` to `x0` gives a sequence that must eventually repeat. Write `cycle_start_and_length(step, x0)` that returns `[mu, length]`: the index where the cycle starts and its length, in O(1) space. Use a slow and a fast walker like a linked-list cycle check, then walk again from `x0` to find the entry.
# EXAMPLE: `step = lambda x: (x * x + 1) % 11`, `x0 = 0` (sequence `0, 1, 2, 5, 4, 6, 4, ...`) -> `[4, 2]`
# BIGO: O(mu + lambda) steps and O(1) space: the slow and fast walkers meet inside the cycle, and a second walk from the start meets the first at the cycle's entry.
# NOTE: The same walk decides whether repeated sums of squared digits ever reach 1: the sequence either settles at 1 or loops.
def cycle_start_and_length(step, x0):
    raise NotImplementedError
# ==== END
