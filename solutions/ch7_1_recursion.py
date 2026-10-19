"""Chapter 7.1: Recursion."""


# ==== EX 7.1.1 | Count the digits | Core
# PROMPT: Write `digit_count(n)` for `n >= 0` recursively: a number below 10 has one digit; otherwise it has one more digit than `n // 10`.
# EXAMPLE: `digit_count(12345)` -> `5`; `digit_count(0)` -> `1`
# BIGO: O(log N) calls: one per digit.
def digit_count(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.2 | Factorial | Core
# PROMPT: Write `factorial(n)` recursively.
# EXAMPLE: `factorial(5)` -> `120`; `factorial(0)` -> `1`
# BIGO: O(N).
def factorial(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.3 | Sum an array recursively | Core
# PROMPT: Write `sum_recursive(arr, index=0)` without slicing (slicing copies, adding hidden O(N) work per call).
# EXAMPLE: `[1, 2, 3, 4]` -> `10`
# BIGO: O(N) time and stack depth.
def sum_recursive(arr, index=0):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.4 | Depth of nesting | Core
# PROMPT: Write `max_depth(nested)` for a list whose items are numbers or further lists: a list with no lists inside has depth 1, and each level of nesting adds one.
# EXAMPLE: `[1, [2, [3]], 4]` -> `3`; `[]` -> `1`
# BIGO: O(N) in the total number of items and lists. Recursion fits because the depth is unknown in advance.
def max_depth(nested):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.5 | Fast power | Practice
# PROMPT: Write `power(x, n)` for integer `n >= 0` by squaring: x^n = (x^(n//2))^2, times x if n is odd.
# EXAMPLE: `power(2, 10)` -> `1024`; `power(3, 0)` -> `1`
# BIGO: O(log N): each call halves n.
def power(x, n):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.6 | Headcount of an org chart | Core
# PROMPT: A person is a tuple `(name, reports)` where `reports` is a list of people. Write `headcount(person)` counting that person and everyone below them.
# EXAMPLE: `('ana', [('bo', []), ('cy', [('di', [])])])` -> `4`
# BIGO: O(N) in the number of people: each person is visited once.
def headcount(person):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.7 | Binary digits, recursively | Core
# PROMPT: Write `to_binary(n)` for `n >= 0` returning its base-2 digits as a string: below 2 it is the digit itself; otherwise it is `to_binary(n // 2)` followed by the last bit.
# EXAMPLE: `to_binary(5)` -> `'101'`; `to_binary(0)` -> `'0'`
# BIGO: O(log N) calls: each one halves n.
def to_binary(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.8 | Running totals in place | Core
# PROMPT: Write `running_totals(arr, i=1)` that replaces each element with the sum of itself and everything before it, recursively and in place, and returns `arr`.
# EXAMPLE: `[1, 2, 3, 4]` -> `[1, 3, 6, 10]`
# BIGO: O(N) time and call-stack depth.
def running_totals(arr, i=1):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.9 | Palindrome check by indexes | Core
# PROMPT: Write `is_palindrome_rec(s, lo=0, hi=None)`: compare the two ends, then recurse on the part between them by moving the indexes inward (no slicing).
# EXAMPLE: `'level'` -> `True`; `'levels'` -> `False`
# BIGO: O(N): N/2 calls, and no copies because the indexes move instead of the string being sliced.
def is_palindrome_rec(s, lo=0, hi=None):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.10 | Sum of the digits | Core
# PROMPT: Write `digit_sum(n)` for `n >= 0` recursively: the last digit plus the digit sum of `n // 10`.
# EXAMPLE: `digit_sum(9045)` -> `18`; `digit_sum(0)` -> `0`
# BIGO: O(log N) calls: one per digit.
def digit_sum(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.11 | Longest word, recursively | Core
# PROMPT: Write `longest_word(words, i=0)` returning the longest word from position `i` on (the earliest one on a tie, `''` for none): compare `words[i]` with the longest word of the rest.
# EXAMPLE: `['go', 'java', 'py', 'rust']` -> `'java'`
# BIGO: O(N) calls, one per word.
def longest_word(words, i=0):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.12 | Collapse repeated neighbours | Core
# PROMPT: Write `collapse_runs(nums, i=0)` returning `nums` with each run of equal neighbours reduced to one value, recursively: keep `nums[i]` unless the next value equals it.
# EXAMPLE: `[1, 1, 2, 2, 2, 3, 1]` -> `[1, 2, 3, 1]`
# BIGO: O(N) calls. Building each result by joining one value onto a new list copies, so O(N^2) values are copied in total.
def collapse_runs(nums, i=0):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.13 | Collatz steps | Core
# PROMPT: Write `collatz_steps(n)` for `n >= 1`: 0 steps from 1; otherwise one step to `n // 2` (n even) or `3n + 1` (n odd), plus the steps from there.
# EXAMPLE: `collatz_steps(6)` -> `8`; `collatz_steps(1)` -> `0`
# BIGO: No known bound in terms of N: each call does O(1) work, so the cost is the number of steps itself.
def collatz_steps(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.14 | Greatest common divisor | Core
# PROMPT: Write `gcd(a, b)` for `a, b >= 0` (not both 0) recursively: `gcd(a, 0)` is `a`; otherwise it equals `gcd(b, a % b)`.
# EXAMPLE: `gcd(48, 18)` -> `6`; `gcd(7, 0)` -> `7`
# BIGO: O(log(min(a, b))) calls: the remainders shrink at least as fast as the Fibonacci numbers grow.
def gcd(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.15 | Tiling a path with short and long tiles | Practice
# PROMPT: A path of length `n` is covered with tiles of length 1 and 3, in order. Write `tilings(n)` counting the ways: the first tile is either short (leaving `n - 1`) or long (leaving `n - 3`).
# EXAMPLE: `tilings(4)` -> `3`; `tilings(10)` -> `28`
# BIGO: About O(1.47^N) as written: the two calls overlap. Chapter 7.2 (7.2.3) brings it to O(N).
def tilings(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.16 | Every balanced bracket string | Practice
# PROMPT: Write `paren_strings(n)` returning every string of `n` `'('` and `n` `')'` that is balanced. Build them one character at a time: add `'('` while fewer than `n` are open, and `')'` while it closes something.
# EXAMPLE: `paren_strings(2)` -> `['(())', '()()']`
# BIGO: Exponential: the number of results follows the Catalan numbers (1, 2, 5, 14, 42, ...), roughly 4^N.
def paren_strings(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.17 | Ways to roll a total with dice | Practice
# PROMPT: Write `dice_ways(dice, total)` counting the ordered ways `dice` six-sided dice can add up to `total`: zero dice make 0 one way; otherwise try each face 1 to 6 for the first die and count the ways for the rest.
# EXAMPLE: `dice_ways(2, 7)` -> `6`; `dice_ways(1, 7)` -> `0`
# BIGO: O(6^D) as written for D dice. Memoized in 72.4.
def dice_ways(dice, total):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.18 | All subsets | Stretch
# PROMPT: Write `subsets(items)` returning every subset (the power set). Each subset of the rest appears once without and once with the first item.
# EXAMPLE: `[1, 2]` -> `[[], [2], [1], [1, 2]]` (any order)
# BIGO: O(2^N) subsets.
def subsets(items):
    raise NotImplementedError
# ==== END


# ==== EX 7.1.19 | Last one standing in a circle | Practice
# PROMPT: `n` people sit in a circle in seats `1` to `n`. Counting from seat 1, every `k`-th person still seated leaves, and counting restarts from the next one. Write `last_standing(n, k)` that returns the seat of the last person left. Recurse on `n - 1`: after one person leaves, the survivor's position in the smaller circle shifts by `k`.
# EXAMPLE: `5, 2` -> `3` (seats 2, 4, 1, 5 leave in that order)
# BIGO: O(N) time and O(N) stack: each call removes one person and renumbers the circle so the next count starts at 0.
def last_standing(n, k):
    raise NotImplementedError
# ==== END
