"""Chapter 3.2: Divide and conquer: mergesort, quicksort and quickselect."""


# ==== EX 3.2.1 | Partition | Core
# PROMPT: Write `partition(arr, left, right)` using the rightmost element as pivot: a left pointer moves right past values smaller than the pivot, a right pointer moves left past values larger, swap, repeat; finally swap the pivot into the left pointer's spot. Return the pivot's final index.
# EXAMPLE: `[0, 5, 2, 1, 6, 3]` -> pivot 3 ends at index 3, values left of it are all < 3, right of it all > 3
# BIGO: O(N) for one partition.
def partition(arr, left, right):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.2 | Quicksort | Core
# PROMPT: Write `quicksort(arr, left=0, right=None)`: partition, then recurse on the sub-arrays left and right of the pivot. Base case: fewer than two elements.
# EXAMPLE: `[0, 5, 2, 1, 6, 3]` -> `[0, 1, 2, 3, 5, 6]`
# BIGO: O(N log N) average, O(N^2) worst case (pivot is always the smallest or largest, e.g. sorted input with a rightmost pivot).
def quicksort(arr, left=0, right=None):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.3 | Quickselect | Core
# PROMPT: Write `quickselect(arr, k)` returning the k-th smallest value (k = 0 is the minimum) without fully sorting: partition, then recurse into only the side that holds index k.
# EXAMPLE: `[0, 50, 20, 10, 60, 30]`, k = 1 -> `10`
# BIGO: O(N) average (N + N/2 + N/4 ... = 2N), O(N^2) worst case.
def quickselect(arr, k, left=0, right=None):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.4 | Closest pair after sorting | Core
# PROMPT: Write `closest_gap_sorted(nums)` for at least two numbers: sort a copy with your quicksort, then compare only neighbours.
# EXAMPLE: `[10, 4, 15, 7]` -> `3`
# BIGO: O(N log N). Once sorted, the closest pair is always adjacent, so N - 1 comparisons replace 1.1.14's every pair.
def closest_gap_sorted(nums):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.5 | Do any meetings overlap? | Practice
# PROMPT: Write `any_overlap(meetings)` for a list of `[start, end]` pairs (a meeting may start exactly when another ends). Sort by start (the built-in sort is fine), then check each meeting against the one before it.
# EXAMPLE: `[[9, 11], [13, 15], [10, 12]]` -> `True`; `[[9, 10], [10, 11]]` -> `False`
# BIGO: O(N log N) for the sort, then one O(N) pass.
def any_overlap(meetings):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.6 | Count distinct values by sorting | Core
# PROMPT: Write `count_distinct_sorted(nums)`: sort a copy with your quicksort, then count the positions whose value differs from the one before.
# EXAMPLE: `[5, 9, 3, 5, 9, 9]` -> `3`
# BIGO: O(N log N) time, with no hash table: after sorting, equal values sit side by side.
def count_distinct_sorted(nums):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.7 | Median with quickselect | Practice
# PROMPT: Write `median(nums)` using `quickselect`. For an even count, average the two middle values.
# EXAMPLE: `[7, 1, 3]` -> `3`; `[4, 1, 3, 2]` -> `2.5`
# BIGO: O(N) average.
def median(nums):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.8 | Three-way partition for repeated values | Stretch
# PROMPT: Write `quicksort3(arr)` that sorts in place and returns `arr`, partitioning each range into values less than, equal to and greater than the pivot (the first value of the range), then recursing only on the outer two parts.
# EXAMPLE: `[3, 1, 3, 2, 3, 1]` -> `[1, 1, 2, 3, 3, 3]`
# BIGO: O(N log N) expected. With only D distinct values it drops to about O(N * D), because the block equal to the pivot is never touched again.
def quicksort3(arr, lo=0, hi=None):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.9 | Merge two sorted arrays | Core
# PROMPT: Write `merge(a, b)` returning one sorted list from two sorted lists, using two indices that advance through them. No `sorted()`.
# EXAMPLE: `merge([1, 4, 9], [2, 3, 10, 11])` -> `[1, 2, 3, 4, 9, 10, 11]`
# BIGO: O(N + M) time, O(N + M) space.
# NOTE: Use `<=` when comparing so equal items from `a` come first. That one character is what makes mergesort stable (3.2.15).
def merge(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.10 | Count the comparisons in a merge | Core
# PROMPT: Write `merge_comparisons(a, b)` returning `(merged, comparisons)`. Find inputs that need the fewest and the most comparisons.
# EXAMPLE: `merge_comparisons([1, 2, 3], [4, 5, 6])[1]` -> `3`; `merge_comparisons([1, 3, 5], [2, 4, 6])[1]` -> `5`
# BIGO: Between min(N, M) and N + M - 1 comparisons.
def merge_comparisons(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.11 | Mergesort, top-down | Core
# PROMPT: Write `mergesort(arr)` returning a new sorted list: split in half, sort each half recursively, then `merge` them. Base case: length 0 or 1.
# EXAMPLE: `mergesort([38, 27, 43, 3, 9, 82, 10])` -> `[3, 9, 10, 27, 38, 43, 82]`
# BIGO: O(N log N) in every case: log2 N levels of splitting, O(N) merging per level. O(N) extra space.
def mergesort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.12 | Mergesort with one shared buffer | Practice
# PROMPT: Write `mergesort_in_place(arr)` that sorts `arr` itself, recursing on index ranges and merging into one auxiliary list allocated once, instead of slicing at every level.
# EXAMPLE: `a = [5, 2, 4, 6, 1, 3]; mergesort_in_place(a)` -> `a` is `[1, 2, 3, 4, 5, 6]`
# BIGO: O(N log N) time, O(N) extra space total instead of fresh slices per call.
def mergesort_in_place(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.13 | Mergesort, bottom-up | Core
# PROMPT: Write `mergesort_bottom_up(arr)` with no recursion: merge runs of width 1 into width 2, then 4, 8, and so on, until one run covers the list.
# EXAMPLE: `mergesort_bottom_up([5, 1, 4, 2, 8, 0, 2])` -> `[0, 1, 2, 2, 4, 5, 8]`
# BIGO: O(N log N) time, O(N) space, and no call stack at all.
def mergesort_bottom_up(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.14 | Count inversions while merging | Practice
# PROMPT: An inversion is a pair i < j with arr[i] > arr[j]. Write `count_inversions(arr)` by adding, every time an item from the right half is taken first, the number of items still waiting in the left half.
# EXAMPLE: `count_inversions([2, 4, 1, 3, 5])` -> `3`; a reversed list of 5 -> `10`
# BIGO: O(N log N), versus O(N^2) for checking every pair.
def count_inversions(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.15 | Stability, with records | Core
# PROMPT: Write `mergesort_by(records, key)` that sorts records by `key(record)` and keeps records with equal keys in their original order. Show that quicksort from Chapter 3.2 does not promise this.
# EXAMPLE: `mergesort_by([("ann", 3), ("bo", 1), ("cy", 3), ("di", 1)], key=lambda r: r[1])` -> `[('bo', 1), ('di', 1), ('ann', 3), ('cy', 3)]`
# BIGO: O(N log N).
def mergesort_by(records, key):
    raise NotImplementedError
# ==== END


# ==== EX 3.2.16 | Hybrid: insertion sort for small pieces | Stretch
# PROMPT: Write `hybrid_sort(arr, cutoff=16)`: mergesort that switches to insertion sort when a piece has `cutoff` items or fewer. Benchmark it against plain mergesort in Chapter 1.3.
# EXAMPLE: `hybrid_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], cutoff=4)` -> `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
# BIGO: Still O(N log N); insertion sort wins on tiny inputs because its constant factor is small. Python's own Timsort does the same trick.
def hybrid_sort(arr, cutoff=16):
    raise NotImplementedError
# ==== END
