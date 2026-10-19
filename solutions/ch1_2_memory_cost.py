"""Chapter 1.2: Memory as a cost."""
import sys


# ==== EX 1.2.1 | Scale scores: a copy or in place | Core
# PROMPT: Write `scaled_copy(scores, factor)` returning a new list with every score multiplied by `factor`, and `scale_in_place(scores, factor)` that changes the original list and returns it. State the extra space each one needs.
# EXAMPLE: `[10, 20], 3` -> `[30, 60]` either way
# BIGO: Both O(N) time. The copy needs O(N) extra space; in place needs O(1).
def scaled_copy(scores, factor):
    raise NotImplementedError


def scale_in_place(scores, factor):
    raise NotImplementedError
# ==== END


# ==== EX 1.2.2 | Most frequent value: three trade-offs | Core
# PROMPT: Find the most frequent value of a non-empty list three ways, breaking ties toward the smaller value: `mode_nested(nums)` (count each value with an inner loop), `mode_counts(nums)` (a dict of counts) and `mode_sorted(nums)` (sort the list in place, then find the longest run).
# EXAMPLE: All three: `[4, 1, 4, 2, 1, 4]` -> `4`
# BIGO: Nested loops: O(N^2) time, O(1) space. Counts table: O(N) time, O(N) space. Sort in place: O(N log N) time and no table of your own, though Python's sort may borrow up to N/2 temporary slots. Choose by which resource is scarcer.
def mode_nested(nums):
    raise NotImplementedError


def mode_counts(nums):
    raise NotImplementedError


def mode_sorted(nums):
    raise NotImplementedError
# ==== END


# ==== EX 1.2.3 | The call stack is memory too | Core
# PROMPT: Write `sum_list_recursive(nums, i=0)` (the sum of `nums[i:]`, without slicing) and `sum_list_iterative(nums)`. Call both on a 50,000-item list and catch the `RecursionError` from the recursive one; check `sys.getrecursionlimit()`.
# EXAMPLE: `sum_list_iterative(list(range(50_000)))` -> `1249975000`; the recursive one raises `RecursionError` (default limit is 1,000)
# BIGO: Both O(N) time. The recursive version holds one stack frame per element, O(N) space; the loop uses O(1).
def sum_list_recursive(nums, i=0):
    raise NotImplementedError


def sum_list_iterative(nums):
    raise NotImplementedError


def recursion_limit():
    raise NotImplementedError
# ==== END


# ==== EX 1.2.4 | Rotate an array without extra space | Core
# PROMPT: Rotate right by `k`: the last `k` items move to the front. Write `rotate_copy(arr, k)` returning a new list, and `rotate_in_place(arr, k)` that reverses the whole list, then the first `k` items, then the rest, and returns `arr`. Which would you use for a 1 GB list?
# EXAMPLE: `[1, 2, 3, 4, 5], 2` -> `[4, 5, 1, 2, 3]`
# BIGO: Copy: O(N) time, O(N) space. Three reversals: O(N) time, O(1) space.
def rotate_copy(arr, k):
    raise NotImplementedError


def rotate_in_place(arr, k):
    raise NotImplementedError
# ==== END


# ==== EX 1.2.5 | Palindrome in O(1) space | Practice
# PROMPT: `s == s[::-1]` builds a full reversed copy. Write `is_palindrome_clean(s)` that ignores case and anything that is not a letter or digit, using two pointers and no new string.
# EXAMPLE: `'A man, a plan, a canal: Panama'` -> `True`
# BIGO: O(N) time, O(1) extra space.
def is_palindrome_clean(s):
    raise NotImplementedError
# ==== END
