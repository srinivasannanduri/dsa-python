"""Chapter 8.2: External memory: sorting data bigger than RAM."""
import heapq
import math
import os
import tempfile


# ==== EX 8.2.1 | Make sorted runs that fit in memory | Core
# PROMPT: Write `make_runs(data, M)` that cuts the input into pieces of at most M items and sorts each piece in memory.
# EXAMPLE: `make_runs([5, 1, 9, 3, 7, 2, 8], 3)` -> `[[1, 5, 9], [2, 3, 7], [8]]`
# BIGO: O(N log M) CPU, one read and one write pass over the data.
def make_runs(data, M):
    raise NotImplementedError
# ==== END


# ==== EX 8.2.2 | Two-way external mergesort | Core
# PROMPT: Write `two_way_sort(data, M)` that makes runs, then merges runs in pairs, pass after pass, until one run is left. Return `(sorted_list, passes)` counting the run-making pass too.
# EXAMPLE: `two_way_sort(list(range(16, 0, -1)), 2)` -> `(list(range(1, 17)), 4)`: 8 runs, then 4, 2, 1
# BIGO: 1 + ceil(log2(N / M)) passes over the data, each costing O(N / B) I/Os.
def two_way_sort(data, M):
    raise NotImplementedError
# ==== END


# ==== EX 8.2.3 | Merge K sorted arrays with a heap | Core
# PROMPT: Write `k_way_merge(lists)` with a heap of `(value, list_index, position)` entries, without `heapq.merge`.
# EXAMPLE: `k_way_merge([[1, 4, 9], [2, 3], [0, 10]])` -> `[0, 1, 2, 3, 4, 9, 10]`
# BIGO: O(N log K) for N total items in K lists.
def k_way_merge(lists):
    raise NotImplementedError
# ==== END


# ==== EX 8.2.4 | M/B-way mergesort | Core
# PROMPT: Write `multiway_sort(data, M, B)` that makes runs of M items and then merges up to `M // B - 1` runs at a time (one input block per run plus one output block). Return `(sorted_list, passes)`.
# EXAMPLE: N = 10,000, M = 100, B = 10 -> 100 runs merged 9 at a time: passes `4` (versus 8 for two-way)
# BIGO: 1 + ceil(log_{M/B}(N / M)) passes. The wider the fan-in, the fewer passes over the disk.
def multiway_sort(data, M, B):
    raise NotImplementedError
# ==== END


# ==== EX 8.2.5 | Predict the passes | Core
# PROMPT: Write `passes_two_way(N, M)` and `passes_multiway(N, M, B)` from the formulas, and check them against 8.2.2 and 8.2.4.
# EXAMPLE: `passes_two_way(10**4, 100)` -> `8`; `passes_multiway(10**4, 100, 10)` -> `4`
# BIGO: O(1).
def passes_two_way(N, M):
    raise NotImplementedError


def passes_multiway(N, M, B):
    raise NotImplementedError
# ==== END


# ==== EX 8.2.6 | Count the I/Os of an external sort | Practice
# PROMPT: Write `external_sort_ios(N, M, B)`: every pass reads and writes the whole data set, which is N / B blocks each way.
# EXAMPLE: `external_sort_ios(10**4, 100, 10)` -> `8000` (4 passes x 2 x 1000 blocks)
# BIGO: O((N / B) log_{M/B}(N / M)) I/Os, the known optimum for sorting in external memory.
def external_sort_ios(N, M, B):
    raise NotImplementedError
# ==== END


# ==== EX 8.2.7 | Sort a real file that "does not fit" | Practice
# PROMPT: Write `sort_file(src, dst, max_items)` that sorts a file of one integer per line using at most `max_items` numbers in memory: write sorted runs to temporary files, then stream them through `heapq.merge` into dst.
# EXAMPLE: a file of 1,000 shuffled numbers with `max_items=100` -> dst holds them sorted, via 10 temporary run files
# BIGO: O(N log N) CPU, two passes over the disk. The same code sorts files far larger than RAM.
def sort_file(src, dst, max_items):
    raise NotImplementedError
# ==== END
