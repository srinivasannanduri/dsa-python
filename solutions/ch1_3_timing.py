"""Chapter 1.3: Timing real code."""
import math
import time
import timeit


# ==== EX 1.3.1 | Time one call with a monotonic clock | Core
# PROMPT: Write `time_once(fn, *args)` returning `(result, seconds)` using `time.perf_counter()` before and after the call.
# EXAMPLE: `time_once(sum, range(10**6))` -> `(499999500000, 0.01...)`
# BIGO: O(1) overhead. `perf_counter` is the highest-resolution clock; `time.time` can jump when the system clock changes.
def time_once(fn, *args):
    raise NotImplementedError
# ==== END


# ==== EX 1.3.2 | Repeat and keep the minimum | Core
# PROMPT: Write `bench(stmt, number=100, repeat=5)` that runs a zero-argument callable with `timeit.repeat` and returns the best time per call. Explain why the minimum, not the average, is the usual summary.
# EXAMPLE: `bench(lambda: sorted(range(1000)))` -> about `1e-05` seconds
# BIGO: O(number * repeat) calls.
# NOTE: Background noise only ever makes a run slower, so the fastest run is closest to the code's true cost.
def bench(stmt, number=100, repeat=5):
    raise NotImplementedError
# ==== END


# ==== EX 1.3.3 | The sort-the-same-array gotcha | Core
# PROMPT: Write `bench_sort(sort_fn, data, repeat=5)` that sorts a fresh copy of `data` on every run and times only the sort, not the copy. Then show what goes wrong if every run sorts the same list.
# EXAMPLE: `bench_sort(list.sort, list(range(10**4, 0, -1)))` returns a small positive float
# BIGO: O(repeat * cost of sort_fn).
# NOTE: An in-place sort leaves the list sorted, so runs 2..n time an already sorted input and look far faster than they are.
def bench_sort(sort_fn, data, repeat=5):
    raise NotImplementedError
# ==== END


# ==== EX 1.3.4 | Read the Big O off a benchmark | Core
# PROMPT: Write `growth_exponent(timings)` that takes `{n: seconds}` for several sizes and returns the slope of log(time) against log(n). A slope near 1 means O(N), near 2 means O(N^2).
# EXAMPLE: `growth_exponent({1000: 0.01, 2000: 0.04, 4000: 0.16})` -> `2.0`
# BIGO: O(K) for K sizes (least-squares fit).
def growth_exponent(timings):
    raise NotImplementedError
# ==== END


# ==== EX 1.3.5 | A sorting race | Practice
# PROMPT: Write `race(sorts, data)` taking `{name: function}` (each returns a new sorted list) and returning names ordered fastest first, checking every result is correct.
# EXAMPLE: `race({"builtin": sorted, "mergesort": mergesort}, data)` -> `['builtin', 'mergesort']` on most machines
# BIGO: Sum of each sort's cost.
def race(sorts, data):
    raise NotImplementedError
# ==== END


# ==== EX 1.3.6 | Quicksort on a sorted array | Core
# PROMPT: Write `quicksort_comparisons(arr)` counting pivot comparisons for the quicksort from Chapter 3.2 with the last element as pivot. Compare sorted input with shuffled input of the same size.
# EXAMPLE: `quicksort_comparisons(list(range(100)))` -> `4950`; a shuffled list of 100 needs far fewer
# BIGO: O(N^2) on sorted input with a last-element pivot, O(N log N) on average.
def quicksort_comparisons(arr):
    raise NotImplementedError
# ==== END


# ==== EX 1.3.7 | Why adaptive sorts love runs | Practice
# PROMPT: Write `count_runs(arr)` returning the number of maximal ascending runs. Python's Timsort merges existing runs, so data with few runs sorts in close to O(N).
# EXAMPLE: `count_runs([1, 2, 3, 2, 5, 6, 1])` -> `3`; a sorted list -> `1`
# BIGO: O(N).
def count_runs(arr):
    raise NotImplementedError
# ==== END
