"""Chapter 3.1: Simple sorts: bubble, selection and insertion."""


# ==== EX 3.1.1 | Bubble sort | Core
# PROMPT: Write `bubble_sort(arr)` that sorts in place by repeatedly comparing neighbours and swapping them when out of order. Return the list.
# EXAMPLE: `[4, 2, 7, 1, 3]` -> `[1, 2, 3, 4, 7]`
# BIGO: O(N^2) time, O(1) space. About N^2/2 comparisons plus up to N^2/2 swaps.
def bubble_sort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.2 | Bubble sort with early exit | Practice
# PROMPT: Write `bubble_sort_optimized(arr)` that shrinks the unsorted range each pass and stops as soon as a pass makes no swaps. Return `(arr, passes)`.
# EXAMPLE: `[1, 2, 3, 4]` -> `([1, 2, 3, 4], 1)`; `[4, 3, 2, 1]` -> 3 passes
# BIGO: Worst case still O(N^2); best case (already sorted) O(N).
# NOTE: The largest unsorted value "bubbles" to its final spot each pass, which is why the range can shrink.
def bubble_sort_optimized(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.3 | Count equal pairs, quadratic | Core
# PROMPT: Write `equal_pairs_quadratic(nums)` counting the pairs of positions `i < j` with `nums[i] == nums[j]`, using two nested loops.
# EXAMPLE: `[1, 2, 1, 1, 2]` -> `4`
# BIGO: O(N^2) time, O(1) space.
def equal_pairs_quadratic(nums):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.4 | Count equal pairs, linear | Core
# PROMPT: Write `equal_pairs_linear(nums)` with one loop and a dict counting how many times each value has appeared so far: each new value pairs with every earlier copy.
# EXAMPLE: Same results as 3.1.3: `[1, 2, 1, 1, 2]` -> `4`
# BIGO: O(N) time, O(N) space. Trading memory for speed.
def equal_pairs_linear(nums):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.5 | Largest pair sum, two ways | Practice
# PROMPT: For a list of at least two numbers, write `largest_pair_sum_quadratic(nums)` (try every pair of positions) and `largest_pair_sum_linear(nums)` (one pass keeping the two largest values seen).
# EXAMPLE: `[3, 9, 1, 7]` -> `16`
# BIGO: O(N^2) versus O(N), for the same answer.
def largest_pair_sum_quadratic(nums):
    raise NotImplementedError


def largest_pair_sum_linear(nums):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.6 | Is it sorted? | Core
# PROMPT: Write `is_sorted(arr)` that checks ascending order in one pass.
# EXAMPLE: `[1, 2, 2, 5]` -> `True`; `[1, 3, 2]` -> `False`
# BIGO: O(N) worst case, can stop at the first out-of-order pair.
def is_sorted(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.7 | Selection sort | Core
# PROMPT: Write `selection_sort(arr)`: on each pass find the index of the smallest unsorted value and swap it into place (one swap per pass at most).
# EXAMPLE: `[4, 2, 7, 1, 3]` -> `[1, 2, 3, 4, 7]`
# BIGO: O(N^2) time, O(1) space. About N^2/2 comparisons but at most N - 1 swaps.
def selection_sort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.8 | Bubble vs selection: count the work | Practice
# PROMPT: Write `bubble_counts(arr)` and `selection_counts(arr)`, each sorting a copy and returning `(comparisons, swaps)`. Compare them on a reversed list of 10.
# EXAMPLE: Reversed 10 elements -> bubble `(45, 45)`, selection `(45, 5)`
# BIGO: Both O(N^2). Selection does roughly half the total steps; Big O ignores that constant, which is why both share a category.
def bubble_counts(arr):
    raise NotImplementedError


def selection_counts(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.9 | Differences between neighbours | Core
# PROMPT: Write `neighbour_gaps(nums)` returning `nums[i + 1] - nums[i]` for each pair of neighbours, in order.
# EXAMPLE: `[3, 7, 4, 10]` -> `[4, -3, 6]`
# BIGO: N - 1 steps, which is still O(N): Big O drops constants and the minus one.
def neighbour_gaps(nums):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.10 | Second largest in one pass | Practice
# PROMPT: Write `second_largest(arr)` returning the second-largest distinct value, or `None`, in a single pass and without sorting.
# EXAMPLE: `[5, 1, 9, 7, 9]` -> `7`; `[3, 3]` -> `None`
# BIGO: O(N) time, O(1) space. Sorting first would be O(N log N).
def second_largest(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.11 | K smallest by partial selection sort | Stretch
# PROMPT: Write `k_smallest(arr, k)` that runs only the first `k` passes of selection sort on a copy and returns the first `k` values.
# EXAMPLE: `[8, 3, 5, 1, 9]`, k = 2 -> `[1, 3]`
# BIGO: O(kN). Better than a full O(N^2) sort when k is small.
def k_smallest(arr, k):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.12 | Insertion sort | Core
# PROMPT: Write `insertion_sort(arr)`: for each index from 1, lift the value out ("temp"), shift larger values on its left one slot right, and drop the value into the gap.
# EXAMPLE: `[4, 2, 7, 1, 3]` -> `[1, 2, 3, 4, 7]`
# BIGO: Worst O(N^2), average about N^2/2, best (already sorted) O(N). O(1) space.
def insertion_sort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.13 | Best, average, worst case in numbers | Practice
# PROMPT: Write `insertion_sort_steps(arr)` that sorts a copy and returns the count of comparisons plus shifts. Run it on a sorted, a random, and a reversed list of 100.
# EXAMPLE: Sorted 100 -> `99`; reversed 100 -> `9900`; random lands in between
# BIGO: Shows O(N) best case and O(N^2) worst case for the same algorithm.
# NOTE: When data is usually nearly sorted, insertion sort can beat selection sort, despite sharing O(N^2).
def insertion_sort_steps(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.14 | Does the list hold every wanted value? | Core
# PROMPT: Write `contains_all(values, wanted)` with a linear search for each wanted value that `break`s on a match, returning `False` as soon as one is missing.
# EXAMPLE: `[4, 8, 15, 16]`, `[8, 16]` -> `True`; `[4, 8]`, `[8, 5]` -> `False`
# BIGO: O(N * M) worst case. Stopping early only helps the best and average case: a missing first value ends the work after one scan.
def contains_all(values, wanted):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.15 | Insert one value into a sorted array | Core
# PROMPT: Write `insert_sorted(arr, value)` that performs a single insertion-sort step: append, then shift left until the value is in place.
# EXAMPLE: `[1, 4, 9]`, value `5` -> `[1, 4, 5, 9]`
# BIGO: O(N) worst case, O(1) if the value belongs at the end.
def insert_sorted(arr, value):
    raise NotImplementedError
# ==== END


# ==== EX 3.1.16 | Sort a nearly sorted list | Practice
# PROMPT: Every value in `nums` is at most `k` positions away from where it belongs. Write `sort_nearly_sorted(nums, k)` that sorts in place with insertion sort and returns `nums`, and explain why it beats O(N^2) here.
# EXAMPLE: `[2, 1, 3, 5, 4], 1` -> `[1, 2, 3, 4, 5]`
# BIGO: O(N * k): each value shifts at most k places, so for small k insertion sort is close to linear.
def sort_nearly_sorted(nums, k):
    raise NotImplementedError
# ==== END
