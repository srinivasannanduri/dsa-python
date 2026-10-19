"""Chapter 4.3: Rolling hashes and text search."""


BASE = 26
PRIME = 1_000_000_007


def code(ch):
    """Map 'a'..'z' to 0..25 so base 26 is exact for lowercase text."""
    return ord(ch) - 97


# ==== EX 4.3.1 | Brute-force substring search | Core
# PROMPT: Write `brute_force_search(text, needle)` returning every index where `needle` starts, comparing character by character at each position.
# EXAMPLE: `brute_force_search("abracadabra", "abra")` -> `[0, 7]`
# BIGO: O(N * M) worst case, e.g. text `"aaaa...a"` and needle `"aa...ab"`.
def brute_force_search(text, needle):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.2 | Sliding a window in O(1) per step | Core
# PROMPT: Write `window_sums(arr, k)` returning the sum of every window of k consecutive values, adding the entering value and subtracting the leaving one.
# EXAMPLE: `window_sums([1, 2, 3, 4, 5], 3)` -> `[6, 9, 12]`
# BIGO: O(N) instead of O(N * k). Rabin-Karp applies exactly this idea to a hash.
def window_sums(arr, k):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.3 | Rolling base-26 hashes | Core
# PROMPT: Write `rolling_hashes(text, m)` returning the hash of every length-m window, treating each window as a base-26 number mod PRIME. Roll with: remove the leading digit times 26^(m-1), multiply by 26, add the new digit.
# EXAMPLE: `rolling_hashes("abcd", 2)` -> `[1, 28, 55]` (ab = 0*26 + 1, bc = 1*26 + 2, cd = 2*26 + 3)
# BIGO: O(N) for all windows.
def rolling_hashes(text, m):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.4 | Rabin-Karp, verified (Las Vegas) | Core
# PROMPT: Write `rabin_karp(text, needle, prime=PRIME)` that compares rolling hashes and confirms each hash match with a real comparison, so the answer is always correct.
# EXAMPLE: `rabin_karp("abracadabra", "abra")` -> `[0, 7]`
# BIGO: O(N + M) expected; O(N * M) only if hash matches are spuriously frequent.
def rabin_karp(text, needle, prime=PRIME):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.5 | Spurious hits with a tiny modulus | Core
# PROMPT: Write `spurious_hits(text, needle, prime)` counting windows whose hash equals the needle's but whose text does not. Compare prime = 7 with prime = 10^9 + 7 on a long text.
# EXAMPLE: 10,000 random letters, needle "abcde" -> prime 7 gives over a thousand spurious hits; 10^9 + 7 gives `0`
# BIGO: O(N). Expected spurious hits are about N / prime, which is why the modulus is large.
def spurious_hits(text, needle, prime):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.6 | Rabin-Karp without verification (Monte Carlo) | Practice
# PROMPT: Write `rabin_karp_monte_carlo(text, needle, rng)` that picks a random prime-sized modulus between 10^9 and 2 x 10^9 for this run and reports every hash match without checking the text.
# EXAMPLE: on ordinary text it returns the same indices as 3.1.4, in strictly O(N + M) time
# BIGO: O(N + M) worst case, with a small chance of a false match. 3.1.4 trades that chance for a verification step.
def _is_prime(n):
    raise NotImplementedError


def rabin_karp_monte_carlo(text, needle, rng):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.7 | Many needles of one length | Practice
# PROMPT: Write `find_any(text, needles)` for needles that all share one length: put their hashes in a set and slide one rolling hash over the text, returning `(index, needle)` pairs.
# EXAMPLE: `find_any("thecatsatonthemat", ["cat", "mat", "dog"])` -> `[(3, 'cat'), (14, 'mat')]`
# BIGO: O(N + K * M) for K needles, instead of K separate searches.
def find_any(text, needles):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.8 | Longest repeated substring | Stretch
# PROMPT: Write `longest_repeat(text)` returning the longest substring that occurs at least twice. Binary-search the length L; for each L, check for a repeated rolling hash (verifying matches).
# EXAMPLE: `longest_repeat("banana")` -> `"ana"`; `longest_repeat("abcd")` -> `""`
# BIGO: O(N log N) expected.
def longest_repeat(text):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.9 | The prefix table | Practice
# PROMPT: Write `prefix_table(pattern)` that returns a list where entry `i` is the length of the longest proper prefix of `pattern[:i + 1]` that is also its suffix. Keep the current match length `k`; on a mismatch fall back to `table[k - 1]` instead of starting over.
# EXAMPLE: `"abacabab"` -> `[0, 0, 1, 0, 1, 2, 3, 2]`
# BIGO: O(M) time and space: `k` rises by at most one per character and every fall-back lowers it, so the total work is linear.
def prefix_table(pattern):
    raise NotImplementedError
# ==== END


# ==== EX 4.3.10 | Search with the prefix table | Practice
# PROMPT: Write `prefix_search(text, pattern)` that returns every start index of `pattern` (non-empty) in `text`, overlaps included, in O(N + M): build the prefix table of `pattern` (4.3.9), then walk `text` once, keeping the matched length `k` and falling back through the table on a mismatch or after a full match.
# EXAMPLE: `"abababca", "abab"` -> `[0, 2]`
# BIGO: O(N + M) worst case, O(M) space: the text pointer never moves back, and the table says how much of the match survives a mismatch.
# NOTE: Unlike Rabin-Karp (4.3.4), this is linear even in the worst case and needs no hashing or verification.
def prefix_search(text, pattern):
    raise NotImplementedError
# ==== END
