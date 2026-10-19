"""Chapter 2.2: Searching sorted data."""


# ==== EX 2.2.1 | Ordered array insert | Core | class=OrderedArray
# PROMPT: Create `OrderedArray` holding a Python list `items` that is always sorted. Write `insert(value)`: scan from the left to find the first element larger than `value`, then shift everything from there one slot right and write the value. Do not use `list.insert` or `sort`.
# EXAMPLE: `[3, 17, 80, 202]` -> `insert(75)` -> `[3, 17, 75, 80, 202]`
# BIGO: O(N). Comparisons up to the spot plus shifts after it always total about N + 2 steps.
# NOTE: Insertion is slower than in a plain array (which appends in O(1)), the price paid for O(log N) search.
class OrderedArray:
    def __init__(self, values=()):
        raise NotImplementedError

    def insert(self, value):
        raise NotImplementedError
# ==== END

    # ==== EX 2.2.6 | Insert using binary search for the position | Practice | class=OrderedArray
    # PROMPT: Add `OrderedArray.insert_fast(value)` that finds the position with your `lower_bound` from 2.2.5 instead of a linear scan, then shifts.
    # EXAMPLE: Same result as `insert`, with only about log2(N) comparisons
    # BIGO: Still O(N) overall because the shifts dominate; the comparisons drop to O(log N).
    def insert_fast(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 2.2.8 | Delete from an ordered array | Core | class=OrderedArray
    # PROMPT: Add `OrderedArray.delete(value)`: find it with binary search, shift the rest left, return `True`; return `False` if absent.
    # EXAMPLE: `[2, 4, 6, 8]` -> `delete(4)` -> `[2, 6, 8]`
    # BIGO: O(log N) to find + O(N) to shift = O(N).
    def delete(self, value):
        raise NotImplementedError
    # ==== END


# ==== EX 2.2.2 | Linear search with early exit | Core
# PROMPT: Write `linear_search_ordered(arr, target)` for a sorted list. Return the index, or `-1` as soon as you pass a value larger than the target.
# EXAMPLE: `[3, 17, 75, 80, 202]`, target `22` -> `-1` after inspecting only 3 elements
# BIGO: O(N) worst case, but it often stops early.
def linear_search_ordered(arr, target):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.3 | Binary search, iterative | Core
# PROMPT: Write `binary_search(arr, target)` on a sorted list using `lower` and `upper` bounds and a midpoint. Return the index or `-1`.
# EXAMPLE: `[3, 17, 75, 80, 202]`, target `80` -> `3`
# BIGO: O(log N). Each step halves the range: 100 elements need at most 7 steps, 1,000,000 need 20.
def binary_search(arr, target):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.4 | Binary search, recursive | Practice
# PROMPT: Write `binary_search_recursive(arr, target, lower=0, upper=None)` with the same contract, using recursion instead of a loop.
# EXAMPLE: `[1, 3, 5, 7, 9]`, target `1` -> `0`
# BIGO: O(log N) time, O(log N) call-stack space.
def binary_search_recursive(arr, target, lower=0, upper=None):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.5 | Insertion point (lower bound) | Core
# PROMPT: Write `lower_bound(arr, target)`: the first index whose value is `>= target` (or `len(arr)` if none). You will reuse it in 2.6.
# EXAMPLE: `[10, 20, 20, 30]`, target `20` -> `1`; target `25` -> `3`; target `99` -> `4`
# BIGO: O(log N).
# NOTE: The range is half-open `[lo, hi)`, so `hi` starts at `len(arr)`, not `len(arr) - 1`.
def lower_bound(arr, target):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.7 | First and last occurrence | Practice
# PROMPT: Write `first_and_last(arr, target)` returning `(first_index, last_index)` in a sorted list with duplicates, or `(-1, -1)`. Use two binary searches.
# EXAMPLE: `[1, 2, 2, 2, 5]`, target `2` -> `(1, 3)`
# BIGO: O(log N). A linear scan outward from one match would degrade to O(N) when everything matches.
def first_and_last(arr, target):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.9 | Count the steps: linear vs binary | Practice
# PROMPT: Write `search_steps(n)` that searches `list(range(n))` for a missing value (`n`) both ways and returns `(linear_steps, binary_steps)`.
# EXAMPLE: `search_steps(100)` -> `(100, 7)`; `search_steps(10_000)` -> `(10000, 14)`
# BIGO: Linear grows 1:1 with N; binary grows by one step each time N doubles.
def search_steps(n):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.10 | Integer square root by binary search | Stretch
# PROMPT: Write `int_sqrt(n)` returning the largest integer `r` with `r * r <= n`, without `math.sqrt`. Binary-search the answer between 0 and n.
# EXAMPLE: `int_sqrt(27)` -> `5`; `int_sqrt(36)` -> `6`
# BIGO: O(log N). Binary search works on any sorted range of candidate answers, not only on arrays.
def int_sqrt(n):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.11 | Search a rotated sorted array | Practice
# PROMPT: `nums` held distinct values in ascending order and was then rotated (`[15, 18, 22, 3, 7, 9]`). Write `search_rotated(nums, target)` that returns the index of `target` or `-1`, in O(log N): at each step decide which half is sorted, then whether `target` lies inside it.
# EXAMPLE: `[15, 18, 22, 3, 7, 9], 7` -> `4`; `[15, 18, 22, 3, 7, 9], 10` -> `-1`
# BIGO: O(log N) time, O(1) space: at every midpoint one half is in order, and a range check on that half decides which way to go.
def search_rotated(nums, target):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.12 | Find a peak | Core
# PROMPT: `nums` is non-empty and no two neighbours are equal. Write `find_peak(nums)` that returns the index of a value larger than both neighbours (past the ends counts as smaller), in O(log N): compare `nums[mid]` with `nums[mid + 1]` and keep the rising side. Any peak is accepted.
# EXAMPLE: `[1, 3, 2, 5, 4]` -> `3` (`1` would also be accepted)
# BIGO: O(log N) time, O(1) space: if the next value is larger, a peak must lie to the right, because the values cannot rise forever.
def find_peak(nums):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.13 | Binary search on the answer | Practice
# PROMPT: Write `smallest_max_load(loads, k)` that splits the positive `loads`, in order, into at most `k` contiguous groups so the largest group sum is as small as possible, and returns that sum. Binary search the answer between `max(loads)` and `sum(loads)`; to test a limit, fill groups greedily and count them.
# EXAMPLE: `[4, 9, 3, 6, 2, 8], 3` -> `13` (`[4, 9] [3, 6, 2] [8]`)
# BIGO: O(N log S) time for loads summing to S, O(1) space: whether a limit works is monotonic, so binary search finds the smallest one, and each check is a greedy pass.
def smallest_max_load(loads, k):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.14 | Index equal to value | Core
# PROMPT: `nums` holds distinct integers in ascending order. Write `fixed_point(nums)` that returns the smallest index `i` with `nums[i] == i`, or `-1`, in O(log N).
# EXAMPLE: `[-4, -1, 2, 5, 9]` -> `2`; `[1, 2, 3]` -> `-1`
# BIGO: O(log N) time, O(1) space: with distinct sorted integers, `nums[i] - i` never decreases, so the matches form one block that binary search can find.
def fixed_point(nums):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.15 | Median of two sorted arrays | Stretch
# PROMPT: `a` and `b` are sorted and not both empty. Write `median_of_two(a, b)` that returns the median of all their values as a float, in O(log min(M, N)) without merging: binary search how many values of the shorter array go in the lower half, and check the four values around the two cuts.
# EXAMPLE: `[1, 4, 9], [2, 3]` -> `3.0`; `[1, 4], [2, 3]` -> `2.5`
# BIGO: O(log min(M, N)) time, O(1) space: binary search the cut in the shorter array; the cut in the other follows, and four border values say which way to move.
def median_of_two(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 2.2.16 | Weighted random pick | Practice | class=WeightedPicker
# PROMPT: Build `WeightedPicker(weights)` for positive integer weights with `total()` and `pick(r)`: for an integer `r` in `[0, total())`, `pick` returns the index whose range of prefix sums holds `r`, found by binary search. Then `pick(random.randrange(picker.total()))` returns index `i` with probability `weights[i] / total`.
# EXAMPLE: `WeightedPicker([3, 1, 2])`: `pick(0)` -> `0`; `pick(3)` -> `1`; `pick(5)` -> `2`
# BIGO: O(N) to build, O(log N) per pick, O(N) space: the prefix sums split `[0, total)` into one range per index, and binary search finds the range holding `r`.
class WeightedPicker:
    def __init__(self, weights):
        raise NotImplementedError

    def total(self):
        raise NotImplementedError

    def pick(self, r):
        raise NotImplementedError
# ==== END
