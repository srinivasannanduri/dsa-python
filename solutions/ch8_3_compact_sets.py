"""Chapter 8.3: Compact sets: bit vectors and Bloom filters."""
import hashlib
import math
import sys


# ==== EX 8.3.1 | A set as a boolean array | Core
# PROMPT: Write `BoolArraySet(universe)` for integers 0..universe-1 backed by a list of booleans, with `add`, `remove`, `__contains__` and `__len__`.
# EXAMPLE: universe 10: add 3, add 7, remove 3 -> `7 in s` is `True`, `3 in s` is `False`, `len(s)` is `1`
# BIGO: O(1) per operation, but one Python object slot (8 bytes) per possible value.
class BoolArraySet:
    def __init__(self, universe):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError

    def remove(self, x):
        raise NotImplementedError

    def __contains__(self, x):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
# ==== END


# ==== EX 8.3.2 | A bit vector with masks | Core | class=BitVector
# PROMPT: Write `BitVector(size)` on a `bytearray` of ceil(size / 8) bytes. Value x lives in byte `x >> 3`, bit `x & 7`. Implement `add` (OR with the mask), `remove` (AND with the inverted mask) and `__contains__` (AND, then test).
# EXAMPLE: `bv = BitVector(100); bv.add(42)` -> `42 in bv` is `True`; `bv.data[5]` is `4` (bit 2 of byte 5)
# BIGO: O(1) per operation, and 1 bit per possible value: 64 times less than a list of booleans.
class BitVector:
    def __init__(self, size):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError

    def remove(self, x):
        raise NotImplementedError

    def __contains__(self, x):
        raise NotImplementedError
# ==== END

    # ==== EX 8.3.3 | Count the members | Core | class=BitVector
    # PROMPT: Add `__len__` that counts set bits across all bytes, using `int.bit_count` on each byte (or a 256-entry lookup table).
    # EXAMPLE: add 1, 5, 99 -> `len(bv)` is `3`
    # BIGO: O(size / 8). Keep a running counter instead if you need O(1).
    def __len__(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 8.3.4 | Union, intersection and difference | Core | class=BitVector
    # PROMPT: Add `union`, `intersection` and `difference`, each returning a new `BitVector` of the same size by combining the bytes with `|`, `&` and `& ~`.
    # EXAMPLE: {1, 2, 3} and {2, 3, 4} -> union `{1, 2, 3, 4}`, intersection `{2, 3}`, difference `{1}`
    # BIGO: O(size / 8): eight set members combined per byte operation.
    def _combine(self, other, op):
        raise NotImplementedError

    def union(self, other):
        raise NotImplementedError

    def intersection(self, other):
        raise NotImplementedError

    def difference(self, other):
        raise NotImplementedError
    # ==== END

    # ==== EX 8.3.5 | Iterate over members | Core | class=BitVector
    # PROMPT: Add `__iter__` yielding members in increasing order, skipping zero bytes entirely.
    # EXAMPLE: add 9, 2, 63 -> `list(bv)` is `[2, 9, 63]`
    # BIGO: O(size / 8 + members).
    def __iter__(self):
        raise NotImplementedError
    # ==== END


# ==== EX 8.3.6 | Estimate the space | Core
# PROMPT: Write `space_report(n)` returning the bytes used by a Python `set` of 0..n-1 (the set plus its int objects), a list of n booleans, and a `BitVector(n)`.
# EXAMPLE: n = 1,000,000 -> set about 60 MB, list about 8 MB, bit vector `125000` bytes
# BIGO: O(N) each, but the constants differ by a factor of about 500.
def space_report(n):
    raise NotImplementedError
# ==== END


# ==== EX 8.3.7 | Find duplicates in a bounded range | Core
# PROMPT: Write `first_duplicate(nums, universe)` returning the first value seen twice, using a `BitVector` as the "seen" set.
# EXAMPLE: `first_duplicate([4, 9, 1, 9, 4], 10)` -> `9`; no repeats -> `None`
# BIGO: O(N) time, universe / 8 bytes of space, no matter how many numbers there are.
def first_duplicate(nums, universe):
    raise NotImplementedError
# ==== END


# ==== EX 8.3.8 | A built-in type as a growable bit set | Practice
# PROMPT: Write `IntBitSet` holding one Python int: `add` with `|=`, `__contains__` with `>>` and `&`, `__or__` and `__and__` for set operations, and `__len__` with `bit_count`.
# EXAMPLE: `a = IntBitSet([1, 5]); b = IntBitSet([5, 7])` -> `list(a | b)` is `[1, 5, 7]`; `len(a & b)` is `1`
# BIGO: Big-int operations run in O(size / 64) machine words, and the set grows as needed.
class IntBitSet:
    def __init__(self, items=()):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError

    def __contains__(self, x):
        raise NotImplementedError

    def __or__(self, other):
        raise NotImplementedError

    def __and__(self, other):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
# ==== END


# ==== EX 8.3.9 | Missing numbers from a range | Practice
# PROMPT: Write `missing(nums, n)` returning every value in 0..n-1 that does not appear in `nums`, marking a `BitVector` and then scanning it.
# EXAMPLE: `missing([0, 3, 1, 6], 7)` -> `[2, 4, 5]`
# BIGO: O(N + n) time, n / 8 bytes of space.
def missing(nums, n):
    raise NotImplementedError
# ==== END


def _two_hashes(item):
    d = hashlib.sha256(str(item).encode()).digest()
    return int.from_bytes(d[:8], "big"), int.from_bytes(d[8:16], "big") | 1


# ==== EX 8.3.10 | k hash functions from two | Core
# PROMPT: Write `bit_positions(item, k, m)` returning k bit positions in [0, m) using double hashing: `(h1 + i * h2) % m` for i in 0..k-1, where h1 and h2 come from one SHA-256 digest.
# EXAMPLE: `bit_positions("cat", 3, 32)` -> three positions in 0..31, the same on every run
# BIGO: O(k) after one hash computation. Kirsch and Mitzenmacher showed this behaves as well as k independent hashes.
def bit_positions(item, k, m):
    raise NotImplementedError
# ==== END


# ==== EX 8.3.11 | A Bloom filter | Core | class=BloomFilter
# PROMPT: Write `BloomFilter(m, k)` with an m-bit `bytearray`, `add(item)` setting the item's k bits, and `might_contain(item)` returning True only if all k bits are set.
# EXAMPLE: add "apple" and "pear" -> `might_contain("apple")` is `True`; `might_contain("grape")` is almost certainly `False`
# BIGO: O(k) per operation; m bits of memory regardless of how large the items are.
# NOTE: "No" is always right. "Yes" means "probably": other items may have set those same bits.
class BloomFilter:
    def __init__(self, m, k):
        raise NotImplementedError

    def _set(self, i):
        raise NotImplementedError

    def _get(self, i):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError

    def might_contain(self, item):
        raise NotImplementedError
# ==== END

    # ==== EX 8.3.16 | Union of two filters | Practice | class=BloomFilter
    # PROMPT: Add `union(other)` returning a new filter whose bits are the OR of both, for filters built with the same m and k.
    # EXAMPLE: filter A holds "x", filter B holds "y" -> the union might contain both
    # BIGO: O(m / 8). Handy for merging filters built on separate machines.
    def union(self, other):
        raise NotImplementedError
    # ==== END


# ==== EX 8.3.12 | Predict the false-positive rate | Core
# PROMPT: Write `false_positive_rate(n, m, k)` = `(1 - e^(-k n / m))^k`, the chance a never-added item looks present after n insertions.
# EXAMPLE: `false_positive_rate(1000, 10_000, 7)` -> about `0.0082` (under 1%)
# BIGO: O(1).
def false_positive_rate(n, m, k):
    raise NotImplementedError
# ==== END


# ==== EX 8.3.13 | Size a filter for a target error | Core
# PROMPT: Write `optimal_params(n, p)` returning `(m, k)`: bits `m = ceil(-n ln p / (ln 2)^2)` and hash count `k = round((m / n) ln 2)`.
# EXAMPLE: `optimal_params(1_000_000, 0.01)` -> `(9585059, 7)`: about 1.2 MB for a million items at 1% error
# BIGO: O(1). Each tenfold cut in p costs only about 4.8 more bits per item.
def optimal_params(n, p):
    raise NotImplementedError
# ==== END


# ==== EX 8.3.14 | Measure the real error | Core
# PROMPT: Write `measured_fp_rate(n, m, k, probes)`: add the strings "in-0" .. "in-{n-1}", then probe "out-0" .. "out-{probes-1}" (never added) and return the fraction reported present.
# EXAMPLE: `measured_fp_rate(1000, 10_000, 7, 20_000)` lands close to the 1.3.3 prediction (within about 0.005)
# BIGO: O((n + probes) * k).
def measured_fp_rate(n, m, k, probes):
    raise NotImplementedError
# ==== END


# ==== EX 8.3.15 | Duplicate detection in a stream | Core
# PROMPT: Write `stream_duplicates(items, m, k)` that reports items the filter says it has seen before. Then write `confirmed_duplicates(items, m, k)` that double-checks each report against an exact set, and count how many reports were false.
# EXAMPLE: a stream of 5,000 unique items plus 100 repeats with m = 64,000, k = 6 -> all 100 repeats reported, and only a handful of false alarms
# BIGO: O(N * k) time, m bits of space. Real systems (web crawlers, databases) use the filter to skip most exact lookups.
def stream_duplicates(items, m, k):
    raise NotImplementedError


def confirmed_duplicates(items, m, k):
    raise NotImplementedError
# ==== END


# ==== EX 8.3.17 | A counting Bloom filter that can delete | Stretch
# PROMPT: Write `CountingBloomFilter(m, k)` with a list of small counters instead of bits: `add` increments, `remove` decrements (only for items you added), and `might_contain` checks all counters are above zero.
# EXAMPLE: add "a", add "b", remove "a" -> `might_contain("a")` is `False` (barring collisions), `might_contain("b")` is `True`
# BIGO: O(k) per operation, at the cost of 4 to 8 bits per counter instead of 1.
class CountingBloomFilter:
    def __init__(self, m, k):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError

    def remove(self, item):
        raise NotImplementedError

    def might_contain(self, item):
        raise NotImplementedError
# ==== END
