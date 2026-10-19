"""Chapter 2.1: Arrays and dynamic arrays."""


# ==== EX 2.1.1 | Fixed-capacity Array skeleton | Core | class=Array
# PROMPT: Create class `Array(capacity)` backed by `[None] * capacity` with a `length` counter and a `steps` counter. Add `__len__`, `is_empty()`, `is_full()`, `to_list()` and `reset_steps()`.
# EXAMPLE: `a = Array(5); len(a) -> 0; a.is_full() -> False`
# BIGO: All O(1) except `to_list()`, which is O(N).
# NOTE: Capacity is fixed, like a real block of memory. Python lists hide this by over-allocating; this class makes the cost of every shift visible.
class Array:
    def __init__(self, capacity):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def is_full(self):
        raise NotImplementedError

    def to_list(self):
        raise NotImplementedError

    def reset_steps(self):
        raise NotImplementedError
# ==== END

    # ==== EX 2.1.2 | Read by index | Core | class=Array
    # PROMPT: Add `read(index)` that returns the element at `index` in one step. Raise `IndexError` if the index is outside `0 .. length-1`.
    # EXAMPLE: `[10, 20, 30]` -> `read(1)` returns `20`; `read(3)` raises `IndexError`
    # BIGO: O(1) time. The computer jumps straight to the memory address.
    # NOTE: Check against `length`, not `capacity`: slots past the length hold no real data.
    def read(self, index):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.3 | Read the first and last element | Core | class=Array
    # PROMPT: Add `first()` and `last()`. Both return `None` on an empty array.
    # EXAMPLE: `[4, 8, 15]` -> `first()` is `4`, `last()` is `15`
    # BIGO: O(1) each. Knowing `length` makes the last slot one jump away.
    # NOTE: The edges matter: insertion and deletion at the end are cheap only because the end is found in one step.
    def first(self):
        raise NotImplementedError

    def last(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.4 | Update by index | Core | class=Array
    # PROMPT: Add `update(index, value)` that overwrites one slot. Same bounds rule as `read`.
    # EXAMPLE: `[1, 2, 3]` -> `update(0, 9)` -> `[9, 2, 3]`
    # BIGO: O(1) time.
    def update(self, index, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.5 | Linear search | Core | class=Array
    # PROMPT: Add `search(value)` that returns the index of the first match, or `-1`. Count one step per element inspected.
    # EXAMPLE: `[5, 3, 7]` -> `search(7)` is `2` after 3 steps; `search(9)` is `-1` after 3 steps
    # BIGO: O(N) worst case, O(1) best case (match in slot 0).
    def search(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.6 | Membership test | Core | class=Array
    # PROMPT: Add `contains(value)` returning `True` or `False`, built on `search`.
    # EXAMPLE: `[5, 3, 7]` -> `contains(3)` is `True`
    # BIGO: O(N). This is what `x in some_list` costs in Python.
    def contains(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.7 | Insert at the end | Core | class=Array
    # PROMPT: Add `insert_at_end(value)`. Raise `OverflowError` when full.
    # EXAMPLE: `[1, 2]` -> `insert_at_end(3)` -> `[1, 2, 3]` in 1 step
    # BIGO: O(1). Nothing has to move.
    def insert_at_end(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.8 | Insert at the start | Core | class=Array
    # PROMPT: Add `insert_at_start(value)`. Shift every element one slot right, starting from the end, then write the new value into slot 0.
    # EXAMPLE: `[2, 3, 4]` -> `insert_at_start(1)` -> `[1, 2, 3, 4]` in 4 steps (3 shifts + 1 write)
    # BIGO: O(N). Worst case for array insertion: N shifts + 1 write = N + 1 steps.
    # NOTE: Shift from the right end backwards. Shifting from the left would overwrite values before they move.
    def insert_at_start(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.9 | Insert at an index | Core | class=Array
    # PROMPT: Add `insert_at(index, value)` for any `index` from `0` to `length` (inserting at `length` means append).
    # EXAMPLE: `[1, 2, 4]` -> `insert_at(2, 3)` -> `[1, 2, 3, 4]` in 2 steps
    # BIGO: O(N - index): N + 1 steps at the start, 1 step at the end.
    def insert_at(self, index, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.10 | Delete at the end | Core | class=Array
    # PROMPT: Add `delete_at_end()` that removes and returns the last element. Raise `IndexError` when empty.
    # EXAMPLE: `[1, 2, 3]` -> returns `3`, leaves `[1, 2]`, 1 step
    # BIGO: O(1).
    def delete_at_end(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.11 | Delete at the start | Core | class=Array
    # PROMPT: Add `delete_at_start()` that removes and returns element 0, then shifts every remaining element one slot left to close the gap.
    # EXAMPLE: `[1, 2, 3, 4]` -> returns `1`, leaves `[2, 3, 4]` in 4 steps (1 delete + 3 shifts)
    # BIGO: O(N). Worst case for deletion: 1 delete + (N - 1) shifts = N steps.
    def delete_at_start(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.12 | Delete at an index | Core | class=Array
    # PROMPT: Add `delete_at(index)` that removes and returns the element at `index` and closes the gap.
    # EXAMPLE: `[1, 2, 9, 3]` -> `delete_at(2)` returns `9`, leaves `[1, 2, 3]`
    # BIGO: O(N - index).
    def delete_at(self, index):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.1.13 | Delete by value | Core | class=Array
    # PROMPT: Add `delete_value(value)` that removes the first occurrence and returns `True`, or returns `False` if absent.
    # EXAMPLE: `[4, 5, 4]` -> `delete_value(4)` -> `[5, 4]`, returns `True`
    # BIGO: O(N) in every case: the search and the shifts together touch every element once.
    # NOTE: If the match is near the front, search is short but shifting is long, and the reverse near the back.
    def delete_value(self, value):
        raise NotImplementedError
    # ==== END


# ==== EX 2.1.14 | Count and locate every match | Core
# PROMPT: Write `count_occurrences(arr, value)` and `find_all_indices(arr, value)` on a plain list, using one loop and no `list.count` or `list.index`.
# EXAMPLE: `find_all_indices([3, 1, 3, 3], 3)` -> `[0, 2, 3]`; count is `3`
# BIGO: O(N) time; O(1) space for the count, O(K) for the K indices returned.
def count_occurrences(arr, value):
    raise NotImplementedError


def find_all_indices(arr, value):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.15 | Minimum and maximum in one pass | Core
# PROMPT: Write `find_min_max(arr)` returning `(min, max)` in a single loop without `min()` or `max()`. Return `None` for an empty list.
# EXAMPLE: `[7, -2, 9, 4]` -> `(-2, 9)`
# BIGO: O(N) time, O(1) space.
def find_min_max(arr):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.16 | Reverse in place | Core
# PROMPT: Write `reverse_in_place(arr)` that reverses a list using two indices that walk toward each other. No slicing, no `reversed`.
# EXAMPLE: `[1, 2, 3, 4, 5]` -> `[5, 4, 3, 2, 1]`
# BIGO: O(N) time (N/2 swaps), O(1) extra space.
def reverse_in_place(arr):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.17 | Array-based set | Core | class=ArraySet
# PROMPT: Subclass `Array` as `ArraySet`. Override `insert_at_end` (and add `add`) so a duplicate is refused. Return `True` if added, `False` if already present.
# EXAMPLE: `s.add(3); s.add(3)` -> second call returns `False`, length stays 1
# BIGO: O(N): the duplicate check is a full search before every insert. Best-case insert is N + 1 steps, not 1.
# NOTE: One rule (no duplicates) turns the cheapest operation into a linear one. That is the chapter's central lesson.
class ArraySet(Array):
    def add(self, value):
        raise NotImplementedError

    def insert_at_end(self, value):
        raise NotImplementedError
# ==== END


# ==== EX 2.1.18 | Predict the steps | Practice
# PROMPT: Write `steps_table(n)` that builds an `Array` of N elements and returns a dict of the step counts for: read, search for a missing value, insert at end, insert at start, delete at end, delete at start. Predict the numbers on paper first.
# EXAMPLE: `steps_table(5)` -> `{'read': 1, 'search_missing': 5, 'insert_end': 1, 'insert_start': 6, 'delete_end': 1, 'delete_start': 5}`
# BIGO: Confirms read O(1), search O(N), insert/delete O(1) at the end and O(N) at the start.
def steps_table(n):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.19 | Grow when full (dynamic array) | Stretch | class=DynamicArray
# PROMPT: Subclass `Array` as `DynamicArray` whose `insert_at_end` doubles the capacity (copying every element to a new block) when full, instead of raising.
# EXAMPLE: Capacity 2, append 1, 2, 3 -> capacity becomes 4, contents `[1, 2, 3]`
# BIGO: A single append is O(N) when it triggers a copy, but O(1) amortized across many appends.
# NOTE: This is how Python's `list.append` stays fast: it over-allocates so copies are rare.
class DynamicArray(Array):
    def _grow(self):
        raise NotImplementedError

    def insert_at_end(self, value):
        raise NotImplementedError
# ==== END


# ==== EX 2.1.20 | Majority value by voting | Practice
# PROMPT: A value fills more than half of `nums`. Write `majority(nums)` in one pass with O(1) extra space: keep a candidate and a count; a matching value adds a vote, a different one removes a vote, and an empty count picks the next value as the candidate.
# EXAMPLE: `[3, 1, 3, 3, 2, 3]` -> `3`
# BIGO: O(N) time, O(1) space: each vote cancels against a different value, and the majority outlasts every cancellation.
def majority(nums):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.21 | Products of everything but self | Core
# PROMPT: Write `products_except_self(nums)` returning, for each index, the product of every other value, without using division (so zeros need no special case).
# EXAMPLE: `[2, 3, 4, 5]` -> `[60, 40, 30, 24]`
# BIGO: O(N) time: one pass left to right for the product before each index, one pass right to left for the product after it.
def products_except_self(nums):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.22 | Longest mountain run | Core
# PROMPT: A mountain is a run that strictly rises and then strictly falls, with at least one step each way. Write `longest_mountain(nums)` returning the length of the longest mountain, or 0 if there is none. Find each tip, then walk down both sides.
# EXAMPLE: `[1, 3, 5, 4, 2, 2, 6, 1]` -> `5`
# BIGO: O(N): each tip is found once, and the climbs and descents around different tips never overlap by more than one value.
def longest_mountain(nums):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.23 | Smallest amount the coins cannot make | Practice
# PROMPT: Each coin in `coins` (positive values, repeats allowed) can be used at most once. Write `smallest_unmakeable(coins)` returning the smallest positive amount that no selection of coins adds up to. Sort, then track the largest amount `reach` that every smaller amount can be made up to.
# EXAMPLE: `[2, 1, 6]` -> `4`; `[1, 1, 3]` -> `6`
# BIGO: O(N log N) for the sort, then one pass: if every amount up to `reach` can be paid and the next coin is at most reach + 1, every amount up to reach + coin can be paid.
def smallest_unmakeable(coins):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.24 | Lowest missing positive, in place | Stretch
# PROMPT: Write `lowest_missing_positive(nums)` returning the smallest positive integer not in `nums`, in O(N) time with no extra list. Rearrange in place so that value `v` (when 1 <= v <= N) sits at index `v - 1`; then the first index whose value is wrong gives the answer.
# EXAMPLE: `[4, -2, 1, 9, 2]` -> `3`; `[2, 3]` -> `1`
# BIGO: O(N) time and O(1) extra space: each swap puts one value in its home slot for good, so there are at most N swaps.
def lowest_missing_positive(nums):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.25 | Missing numbers in 1..n | Core
# PROMPT: `nums` holds distinct values from 1 to `n`. Write `missing_from_range(nums, n)` returning the values in 1..n that are absent, in increasing order, using a list of `n + 1` marks rather than sorting.
# EXAMPLE: `[4, 1, 6], 6` -> `[2, 3, 5]`
# BIGO: O(N) time and O(N) space: one pass marks what is present, one pass collects what is not.
def missing_from_range(nums, n):
    raise NotImplementedError
# ==== END


# ==== EX 2.1.26 | First repeat, using the array as its own table | Practice
# PROMPT: Every value in `nums` is between 1 and `len(nums)`. Write `first_repeat_in_place(nums)` returning the value whose second appearance comes first, or -1, using no extra structure: when you meet `v`, flip `nums[v - 1]` negative; finding it already negative means `v` is a repeat. Restore the signs before returning.
# EXAMPLE: `[3, 1, 4, 4, 1]` -> `4`; `[1, 2, 3]` -> `-1`
# BIGO: O(N) time, O(1) extra space: the sign of `nums[v - 1]` records whether `v` has been seen.
def first_repeat_in_place(nums):
    raise NotImplementedError
# ==== END
