"""Chapter 8.1: Caching and eviction."""
from collections import OrderedDict, deque


# ==== EX 8.1.1 | LRU cache from the standard library | Core
# PROMPT: Write `LRUCache(capacity)` with `get(key)` (returns `None` on a miss) and `put(key, value)`, evicting the least recently used key. Use `move_to_end` and `popitem(last=False)`.
# EXAMPLE: capacity 2: put a, put b, get a, put c -> b is evicted; get b is `None`
# BIGO: O(1) per operation.
class LRUCache:
    def __init__(self, capacity):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError
# ==== END


# ==== EX 8.1.2 | LRU from a hash table and a doubly linked list | Core
# PROMPT: Build `LinkedLRU(capacity)` without OrderedDict: a dict from key to node, plus a doubly linked list with head and tail sentinels. Most recent sits next to head; evict from next to tail.
# EXAMPLE: Same behaviour as 2.4.1
# BIGO: O(1) per get and put: the dict finds the node, the links let it move without shifting.
# NOTE: Sentinel nodes remove every "is the list empty?" special case from insert and unlink.
class _Node:
    __slots__ = ("key", "value", "prev", "next")

    def __init__(self, key=None, value=None):
        raise NotImplementedError


class LinkedLRU:
    def __init__(self, capacity):
        raise NotImplementedError

    def _unlink(self, node):
        raise NotImplementedError

    def _push_front(self, node):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError
# ==== END


# ==== EX 8.1.3 | Measure a hit rate | Core
# PROMPT: Write `hit_rate(cache, requests)` that, for each requested key, counts a hit when `get` finds it and otherwise `put`s it. Return hits / requests.
# EXAMPLE: `hit_rate(LRUCache(2), ["a", "b", "a", "a", "c", "b"])` -> `0.333...` (2 hits in 6)
# BIGO: O(R) for R requests.
def hit_rate(cache, requests):
    raise NotImplementedError
# ==== END


# ==== EX 8.1.4 | FIFO eviction for comparison | Core
# PROMPT: Write `FIFOCache(capacity)` that evicts the oldest inserted key regardless of use, with the same `get`/`put` interface. Compare its hit rate with LRU on a stream that reuses a few hot keys.
# EXAMPLE: hot keys reused constantly -> LRU's hit rate is higher than FIFO's
# BIGO: O(1) per operation with a deque of insertion order.
class FIFOCache:
    def __init__(self, capacity):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError
# ==== END


# ==== EX 8.1.5 | Random eviction in O(1) | Core
# PROMPT: Write `RandomCache(capacity, rng)` that evicts a uniformly random key. Keep keys in a list plus a dict of key to index; remove by swapping the victim with the last slot.
# EXAMPLE: capacity 3 never holds more than 3 keys; which key goes depends on the seed
# BIGO: O(1) per operation.
class RandomCache:
    def __init__(self, capacity, rng):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError
# ==== END


# ==== EX 8.1.6 | LRU's worst case, fixed by randomness | Practice
# PROMPT: Write `cyclic_requests(capacity, rounds)` that cycles through capacity + 1 keys. Show LRU's hit rate on it is 0, while `RandomCache` keeps a healthy share of hits.
# EXAMPLE: capacity 10, 100 rounds -> LRU `0.0`; random eviction (seed 1) well above `0.5`
# BIGO: O(R). Every request evicts the very key that will be needed next, the textbook LRU pathology.
def cyclic_requests(capacity, rounds):
    raise NotImplementedError
# ==== END


# ==== EX 8.1.7 | A bounded memoizing wrapper | Practice
# PROMPT: Write `lru_memo(maxsize)` returning a decorator that caches results in your `LRUCache`, keyed by the argument tuple, and exposes `wrapper.hits` and `wrapper.misses`.
# EXAMPLE: decorate a slow `square(x)`, call it with 1, 2, 1 -> hits `1`, misses `2`
# BIGO: O(1) bookkeeping per call; memory is capped at maxsize entries, unlike an unbounded dict.
def lru_memo(maxsize):
    raise NotImplementedError
# ==== END


# ==== EX 8.1.8 | Cache-friendly traversal order | Core
# PROMPT: Write `sum_rows_first(grid)` and `sum_columns_first(grid)`, then a `blocked_transpose(m, block)` that copies the matrix tile by tile. All must give correct results; time them on a 2000 by 2000 grid.
# EXAMPLE: both sums of `[[1, 2], [3, 4]]` -> `10`; `blocked_transpose([[1, 2, 3], [4, 5, 6]], 2)` -> `[[1, 4], [2, 5], [3, 6]]`
# BIGO: All O(R * C) steps. Row-first touches memory in order (spatial locality); in pure Python the gap is smaller than in C, because each list element is a pointer to an object.
def sum_rows_first(grid):
    raise NotImplementedError


def sum_columns_first(grid):
    raise NotImplementedError


def blocked_transpose(m, block):
    raise NotImplementedError
# ==== END
