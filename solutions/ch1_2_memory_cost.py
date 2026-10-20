"""Chapter 1.2: Memory as a cost."""
import sys


# ==== EX 1.2.1 | Scale scores: a copy or in place | Core
# PROMPT: Write `scaled_copy(scores, factor)` returning a new list with every score multiplied by `factor`, and `scale_in_place(scores, factor)` that changes the original list and returns it. State the extra space each one needs.
# EXAMPLE: `[10, 20], 3` -> `[30, 60]` either way
# BIGO: Both O(N) time. The copy needs O(N) extra space; in place needs O(1).
def scaled_copy(scores, factor):
    return [score * factor for score in scores]

def scale_in_place(scores, factor):
    for idx in range(len(scores)):
        scores[idx] *= factor

    return scores
# ==== END


# ==== EX 1.2.2 | Most frequent value: three trade-offs | Core
# PROMPT: Find the most frequent value of a non-empty list three ways, breaking ties toward the smaller value: `mode_nested(nums)` (count each value with an inner loop), `mode_counts(nums)` (a dict of counts) and `mode_sorted(nums)` (sort the list in place, then find the longest run).
# EXAMPLE: All three: `[4, 1, 4, 2, 1, 4]` -> `4`
# BIGO: Nested loops: O(N^2) time, O(1) space. Counts table: O(N) time, O(N) space. Sort in place: O(N log N) time and no table of your own, though Python's sort may borrow up to N/2 temporary slots. Choose by which resource is scarcer.
def mode_nested(nums):
    best, best_count = None, 0

    for x in nums:
        count = 0
        for y in nums:
            if x == y: 
                count += 1

        if count > best_count or (count == best_count and x < best): 
            best, best_count = x, count 

    return best

def mode_counts(nums):
    counts = {}

    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    best = None
    for key, value in counts.items():
        if best is None or value > counts[best] or (value == counts[best] and key < best):
            best = key
    
    return best


def mode_sorted(nums):
    nums.sort()

    best, best_len, run = nums[0], 0, 0

    for i in range(len(nums)):
        run = run + 1 if i > 0 and nums[i] == nums[i - 1] else 1

        if run > best_len:
            best, best_len = nums[i], run
    
    return best
# ==== END


# ==== EX 1.2.3 | The call stack is memory too | Core
# PROMPT: Write `sum_list_recursive(nums, i=0)` (the sum of `nums[i:]`, without slicing) and `sum_list_iterative(nums)`. Call both on a 50,000-item list and catch the `RecursionError` from the recursive one; check `sys.getrecursionlimit()`.
# EXAMPLE: `sum_list_iterative(list(range(50_000)))` -> `1249975000`; the recursive one raises `RecursionError` (default limit is 1,000)
# BIGO: Both O(N) time. The recursive version holds one stack frame per element, O(N) space; the loop uses O(1).
def sum_list_recursive(nums, i=0):
    return 0 if i == len(nums) else nums[i] + sum_list_recursive(nums, i + 1)
    
def sum_list_iterative(nums):
    sum = 0 
    for num in nums:
        sum += num
    return sum

def recursion_limit():
    return sys.getrecursionlimit()
# ==== END


# ==== EX 1.2.4 | Rotate an array without extra space | Core
# PROMPT: Rotate right by `k`: the last `k` items move to the front. Write `rotate_copy(arr, k)` returning a new list, and `rotate_in_place(arr, k)` that reverses the whole list, then the first `k` items, then the rest, and returns `arr`. Which would you use for a 1 GB list?
# EXAMPLE: `[1, 2, 3, 4, 5], 2` -> `[4, 5, 1, 2, 3]`
# BIGO: Copy: O(N) time, O(N) space. Three reversals: O(N) time, O(1) space.
def rotate_copy(arr, k):
    return arr[-k:] + arr[:-k]


def rotate_in_place(arr, k):    
    def reverse(lo, hi):
        while lo < hi:
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo, hi = lo + 1, hi - 1

    n = len(arr)
    if n:
        k %= n
        reverse(0, n -1)
        reverse(0, k - 1)
        reverse(k, n - 1)

    return arr
# ==== END


# ==== EX 1.2.5 | Palindrome in O(1) space | Practice
# PROMPT: `s == s[::-1]` builds a full reversed copy. Write `is_palindrome_clean(s)` that ignores case and anything that is not a letter or digit, using two pointers and no new string.
# EXAMPLE: `'A man, a plan, a canal: Panama'` -> `True`
# BIGO: O(N) time, O(1) extra space.
def is_palindrome_clean(s):
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1

    return True
# ==== END
