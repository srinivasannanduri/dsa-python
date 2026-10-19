"""Chapter 4.2: Hash functions."""
from collections import Counter


# ==== EX 4.2.1 | A naive string hash and its collisions | Core
# PROMPT: Write `sum_hash(s, m)` that adds the character codes and takes `% m`. Show that every anagram collides.
# EXAMPLE: `sum_hash("stop", 101) == sum_hash("pots", 101) == sum_hash("tops", 101)` -> `True`
# BIGO: O(len(s)). Ignoring position throws away most of the information in the key.
def sum_hash(s, m):
    raise NotImplementedError
# ==== END


# ==== EX 4.2.2 | Polynomial string hashing | Core
# PROMPT: Write `poly_hash(s, m, base=31)` computing `(c0 * base^(L-1) + c1 * base^(L-2) + ... ) % m` with Horner's rule, so character order matters.
# EXAMPLE: `poly_hash("stop", 10**9 + 7) != poly_hash("pots", 10**9 + 7)` -> `True`
# BIGO: O(len(s)).
def poly_hash(s, m, base=31):
    raise NotImplementedError
# ==== END


# ==== EX 4.2.3 | The division method and a bad table size | Core
# PROMPT: Write `division_hash(k, m)` = `k % m`. Hash the keys 0, 8, 16, ..., 7992 into m = 64 and into m = 61 and count how many buckets each uses.
# EXAMPLE: m = 64 -> only `8` buckets used; m = 61 (a prime) -> all `61` used
# BIGO: O(1) per key. Keys that share a factor with m crowd into few buckets; a prime m not near a power of two avoids the most common patterns.
def division_hash(k, m):
    raise NotImplementedError


def buckets_used(keys, m, hash_fn):
    raise NotImplementedError
# ==== END


# ==== EX 4.2.4 | Measure a hash function's spread | Core
# PROMPT: Write `max_bucket(keys, m, hash_fn)` returning the size of the fullest bucket. A good function keeps it close to len(keys) / m.
# EXAMPLE: 10,000 words into 1,000 buckets with `poly_hash` -> a fullest bucket around 20 to 25; with `sum_hash`, many times more
# BIGO: O(N). The fullest bucket bounds the worst lookup time with chaining.
def max_bucket(keys, m, hash_fn):
    raise NotImplementedError
# ==== END


# ==== EX 4.2.5 | Universal hashing | Core
# PROMPT: Write `UniversalHash(m, rng, p=2**61 - 1)` that picks random a in [1, p - 1] and b in [0, p - 1] once, and hashes an integer k as `((a * k + b) % p) % m`.
# EXAMPLE: two instances with different seeds send the same key to different buckets; any fixed pair of keys collides with probability about 1 / m
# BIGO: O(1) per key. Because the function is chosen at random after the keys are fixed, no input can be bad for most choices.
class UniversalHash:
    def __init__(self, m, rng, p=2**61 - 1):
        raise NotImplementedError

    def __call__(self, k):
        raise NotImplementedError
# ==== END


# ==== EX 4.2.6 | Adversarial keys break a fixed function | Practice
# PROMPT: Write `adversarial_keys(m, count)` returning keys that all collide under `k % m` (multiples of m). Compare the fullest bucket under the division method and under `UniversalHash`.
# EXAMPLE: m = 1,000, 5,000 keys -> division method `5000` in one bucket; universal hash about `15`
# BIGO: Fixed function: O(N) per lookup on these keys. Universal: O(1 + N/m) expected on any keys.
def adversarial_keys(m, count):
    raise NotImplementedError


def fullest(keys, fn):
    raise NotImplementedError
# ==== END


# ==== EX 4.2.7 | A hash table that re-randomizes when it grows | Practice
# PROMPT: Write `RandomizedHashTable(rng)` with chaining over integer keys: `put`, `get` and `__len__`. When the load factor passes 1, double the bucket count and draw a fresh `UniversalHash` before rehashing.
# EXAMPLE: insert 10,000 adversarial keys -> every value is found and the fullest bucket stays small
# BIGO: O(1) expected per operation, O(1) amortized for resizing.
class RandomizedHashTable:
    def __init__(self, rng, capacity=8):
        raise NotImplementedError

    def _new_table(self, capacity):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError

    def get(self, key, default=None):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def longest_chain(self):
        raise NotImplementedError
# ==== END


# ==== EX 4.2.8 | The multiplication method | Stretch
# PROMPT: Write `mult_hash(k, m, A=0.6180339887)` = `floor(m * frac(k * A))` (Knuth's golden-ratio choice). Unlike the division method it works well even when m is a power of two.
# EXAMPLE: the keys 0, 8, ..., 7992 into m = 64 -> all `64` buckets used, where `k % 64` used only 8
# BIGO: O(1).
def mult_hash(k, m, A=0.6180339887498949):
    raise NotImplementedError
# ==== END
