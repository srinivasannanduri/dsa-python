"""Chapter 1.1: Counting steps: how cost grows with input."""


# ==== EX 1.1.1 | An O(1) algorithm | Core
# PROMPT: Write `is_leap_year(year)`. Explain why its step count does not depend on the input's size.
# EXAMPLE: `is_leap_year(2024)` -> `True`; `1900` -> `False`; `2000` -> `True`
# BIGO: O(1). At most three checks, whatever the year.
def is_leap_year(year):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.2 | An O(N) algorithm | Core
# PROMPT: Write `array_sum(arr)` with a loop (no `sum()`), and say how many steps it takes for N elements.
# EXAMPLE: `[1, 2, 3, 4]` -> `10`, 4 loop steps
# BIGO: O(N). One step per element.
def array_sum(arr):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.3 | An O(log N) algorithm | Core
# PROMPT: Write `halving_steps(n)` returning how many times you can halve `n` (integer division) before it reaches 1.
# EXAMPLE: `halving_steps(8)` -> `3`; `halving_steps(1024)` -> `10`; `halving_steps(1)` -> `0`
# BIGO: O(log N). This is the definition of log2 N for powers of two.
def halving_steps(n):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.4 | Doubling: rounds until everyone knows | Practice
# PROMPT: One person knows a rumour. Each round, everyone who knows tells one person who does not. Write `rounds_to_reach(people)` returning how many rounds pass before at least `people` know.
# EXAMPLE: `rounds_to_reach(1)` -> `0`; `rounds_to_reach(2)` -> `1`; `rounds_to_reach(1000)` -> `10`
# BIGO: O(log N). The number who know doubles each round, the mirror image of halving.
def rounds_to_reach(people):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.5 | Count nested-loop steps | Practice
# PROMPT: Write `all_pairs_steps(n)` (inner loop runs N times per outer step) and `unique_pairs_steps(n)` (inner loop starts at `i + 1`). Both return the number of inner-loop iterations. Classify both.
# EXAMPLE: `all_pairs_steps(4)` -> `16`; `unique_pairs_steps(4)` -> `6`
# BIGO: Both O(N^2). Unique pairs is N(N-1)/2, about half, and Big O ignores the 1/2.
def all_pairs_steps(n):
    raise NotImplementedError


def unique_pairs_steps(n):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.6 | Running balance with no overdraft | Core
# PROMPT: Write `final_balance(changes)`: start at 0 and apply each deposit (positive) or withdrawal (negative) in order, skipping any withdrawal that would take the balance below 0.
# EXAMPLE: `[50, -20, -40, 10]` -> `40`
# BIGO: O(N). One pass, and each step does a constant amount of work.
def final_balance(changes):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.7 | Every pairing from a list | Core
# PROMPT: Write `pairings(names)` returning `'a-b'` for every pair of positions `i < j`, in that order.
# EXAMPLE: `['ana', 'bo', 'cy']` -> `['ana-bo', 'ana-cy', 'bo-cy']`
# BIGO: O(N^2): N(N-1)/2 pairings, each built once.
def pairings(names):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.8 | Committees of three | Practice
# PROMPT: Extend the idea to `committees(names)`: every choice of three positions `i < j < k`, written `'a,b,c'`, in that order. How does the Big O change?
# EXAMPLE: `['a', 'b', 'c', 'd']` -> `['a,b,c', 'a,b,d', 'a,c,d', 'b,c,d']`
# BIGO: O(N^3): about N^3/6 committees. Each extra nested loop over the same input adds one to the exponent.
def committees(names):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.9 | The newest entries of a log | Core
# PROMPT: Write `newest(lines, k)` returning the last `k` lines in their original order (all of them if there are fewer), reading by index rather than walking the whole list.
# EXAMPLE: `['a', 'b', 'c', 'd'], 2` -> `['c', 'd']`
# BIGO: O(k), not O(N). Reading by index jumps straight to the end, so the length of the log does not matter.
def newest(lines, k):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.10 | Busiest hour of the day | Core
# PROMPT: Write `busiest_hour(times)` for a non-empty list of `'HH:MM'` strings, returning the hour (an int) with the most entries; on a tie, the earliest hour.
# EXAMPLE: `['09:15', '10:02', '09:40', '11:00']` -> `9`
# BIGO: O(N). One pass counts into 24 slots, then a fixed 24-step scan; a constant amount of extra work does not change the class.
def busiest_hour(times):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.11 | A week of slots per person | Core
# PROMPT: Write `weekly_slots(names)` returning `'<name> <day>'` for every name and each of `Mon` to `Sun`, name by name.
# EXAMPLE: `['ana']` -> `['ana Mon', 'ana Tue', 'ana Wed', 'ana Thu', 'ana Fri', 'ana Sat', 'ana Sun']`
# BIGO: O(N). The inner loop always runs 7 times, so it is 7N steps, not N^2.
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def weekly_slots(names):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.12 | Vowels across a document | Core
# PROMPT: Write `count_vowels(lines)` counting the vowels `aeiou`, in either case, across a list of strings.
# EXAMPLE: `['Hello', 'World']` -> `3`
# BIGO: O(C) where C is the total number of characters. The loops are nested, but together they visit each character once.
def count_vowels(lines):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.13 | Is the grid symmetric? | Core
# PROMPT: Write `is_symmetric(grid)` for a square list of lists: `True` when `grid[i][j] == grid[j][i]` everywhere. Compare each pair of cells once.
# EXAMPLE: `[[1, 2], [2, 1]]` -> `True`; `[[1, 2], [3, 1]]` -> `False`
# BIGO: O(N^2) for an N x N grid. Checking only above the diagonal halves the work, and Big O ignores the half.
def is_symmetric(grid):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.14 | Closest pair of readings | Core
# PROMPT: Write `closest_gap(nums)` for a list of at least two numbers, returning the smallest absolute difference between any two of them, by comparing every pair.
# EXAMPLE: `[10, 4, 15, 7]` -> `3`
# BIGO: O(N^2): every pair is compared once.
# NOTE: Sorting first brings this to O(N log N) (3.2.4).
def closest_gap(nums):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.15 | Free hours two people share | Practice
# PROMPT: Write `shared_hours(a, b)` returning the hours in `a` that also appear in `b`, in `a`'s order, using nested loops.
# EXAMPLE: `[9, 10, 13, 15]`, `[10, 11, 15]` -> `[10, 15]`
# BIGO: O(N * M) with nested loops. With two different inputs, name both sizes instead of writing O(N^2).
# NOTE: Putting one list in a hash set makes it O(N + M) (Chapter 4.1).
def shared_hours(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 1.1.16 | Every on/off switch setting | Practice
# PROMPT: Write `switch_settings(n)` returning every setting of `n` on/off switches as a string of `'0'` and `'1'`, in increasing binary order. Build the strings yourself rather than with a formatting helper.
# EXAMPLE: `switch_settings(2)` -> `['00', '01', '10', '11']`
# BIGO: O(2^N): each extra switch doubles the number of settings (and each setting takes N characters to write).
def switch_settings(n):
    raise NotImplementedError
# ==== END
