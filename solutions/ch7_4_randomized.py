"""Chapter 7.4: Randomized algorithms."""
import bisect
import itertools
import math
import random
from collections import Counter


# ==== EX 7.4.1 | Randomized quicksort | Core
# PROMPT: Write `random_quicksort(arr, rng)` returning a new sorted list, choosing each pivot uniformly at random. Count comparisons on sorted input and compare with 22.6.
# EXAMPLE: `random_quicksort(list(range(10)), random.Random(1))` -> `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
# BIGO: O(N log N) expected on every input, including sorted ones. The worst case still exists but needs extraordinarily bad luck.
def random_quicksort(arr, rng):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.2 | Reproducible randomness with seeds | Core
# PROMPT: Write `sample_with_seed(seed, population, k)` that returns the same k-item sample every time for the same seed, using its own `random.Random(seed)` rather than the global generator.
# EXAMPLE: `sample_with_seed(42, range(100), 3) == sample_with_seed(42, range(100), 3)` -> `True`
# BIGO: O(k).
# NOTE: A private `Random` instance keeps your results reproducible even when other code also draws random numbers.
def sample_with_seed(seed, population, k):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.3 | A linear congruential generator | Core
# PROMPT: Write a generator `lcg(seed, a=1103515245, c=12345, m=2**31)` yielding `x = (a * x + c) % m` forever. Then find the period of the tiny generator `a=5, c=3, m=16`.
# EXAMPLE: first three values from `lcg(1, 5, 3, 16)` -> `[8, 11, 10]`; its period is `16`
# BIGO: O(1) per number. This is a PRNG: fully determined by the seed, which is why it is reproducible and why it is not secure.
def lcg(seed, a=1103515245, c=12345, m=2**31):
    raise NotImplementedError


def lcg_period(seed, a, c, m):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.4 | Fisher-Yates shuffle | Core
# PROMPT: Write `fisher_yates(arr, rng)` that shuffles in place: for i from the last index down to 1, swap arr[i] with arr[j] for a random j in 0..i.
# EXAMPLE: `fisher_yates([1, 2, 3, 4, 5], random.Random(7))` returns some ordering of 1..5, the same one every time for seed 7
# BIGO: O(N) time, O(1) extra space, and every permutation is equally likely.
def fisher_yates(arr, rng):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.5 | Prove the naive shuffle is biased | Practice
# PROMPT: The naive shuffle swaps each position with any position 0..n-1. Write `naive_distribution(n)` and `fisher_yates_distribution(n)` that enumerate every possible sequence of random choices and count the resulting permutations.
# EXAMPLE: For n = 3: Fisher-Yates gives each of the 6 permutations exactly once; naive spreads 27 outcomes as `{4, 5, 5, 5, 4, 4}`
# BIGO: O(n^n) and O(n!) sequences: exact enumeration, no randomness needed.
# NOTE: 27 equally likely outcomes cannot split evenly over 6 permutations, so the naive shuffle must be biased.
def naive_distribution(n):
    raise NotImplementedError


def fisher_yates_distribution(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.6 | Randomize before building a BST | Core
# PROMPT: Write `bst_height(keys)` that inserts keys in order into a plain BST and returns its height. Compare sorted keys with the same keys shuffled.
# EXAMPLE: `bst_height(list(range(200)))` -> `200`; shuffled with `random.Random(3)` -> about 15 to 20
# BIGO: Height O(N) for sorted input, O(log N) expected after shuffling.
def bst_height(keys):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.7 | Reservoir sampling | Practice
# PROMPT: Write `reservoir(stream, k, rng)` that picks k items uniformly from a stream of unknown length in one pass: keep the first k, then replace a random slot with item i (0-based) with probability k / (i + 1).
# EXAMPLE: `reservoir(range(1_000_000), 3, random.Random(0))` -> 3 values, each equally likely to be any of the million
# BIGO: O(N) time, O(k) memory.
def reservoir(stream, k, rng):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.8 | Load balancing with random choices | Core
# PROMPT: Write `max_load_random(jobs, servers, rng)` assigning each job to a random server, and `max_load_two_choices(jobs, servers, rng)` picking two random servers and using the less loaded one. Return the busiest server's load.
# EXAMPLE: With 10,000 jobs on 1,000 servers and seed 5, two choices gives a clearly lower maximum than one choice
# BIGO: O(J) for J jobs. The "power of two choices" drops the expected maximum excess from about log N / log log N to log log N.
def max_load_random(jobs, servers, rng):
    raise NotImplementedError


def max_load_two_choices(jobs, servers, rng):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.9 | Weighted random choice | Practice
# PROMPT: Write `make_weighted_picker(weights, rng)` that precomputes prefix sums and returns a function picking index i with probability weights[i] / total, using `bisect`.
# EXAMPLE: weights `[1, 3, 6]` -> over 10,000 picks index 2 comes up about 60% of the time
# BIGO: O(N) setup, O(log N) per pick.
def make_weighted_picker(weights, rng):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.10 | Estimate pi by throwing darts | Core
# PROMPT: Write `estimate_pi(samples, rng)`: pick random points in the unit square and return 4 times the fraction that land inside the quarter circle.
# EXAMPLE: `estimate_pi(100_000, random.Random(0))` -> about `3.14` (within 0.02)
# BIGO: O(S) samples; the error shrinks like 1 / sqrt(S), so 100 times more samples buy one more correct digit.
def estimate_pi(samples, rng):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.11 | Averages from a random sample | Core
# PROMPT: Write `sampled_mean(data, k, rng)` estimating the mean of a huge list from k random positions (with replacement), and `exact_mean(data)` for comparison.
# EXAMPLE: one million values, k = 2,000 -> the estimate lands within about 2% of the true mean
# BIGO: O(k) instead of O(N); accuracy depends on k and the data's spread, not on N.
def sampled_mean(data, k, rng):
    raise NotImplementedError


def exact_mean(data):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.12 | Monte Carlo versus Las Vegas | Core
# PROMPT: In a list where half the entries are 1, write `las_vegas_find_one(arr, rng)` (probe random positions until a 1 appears; always right, time varies) and `monte_carlo_find_one(arr, rng, tries)` (give up after `tries` probes and return -1; time fixed, may fail).
# EXAMPLE: both return an index holding 1; Monte Carlo with 20 tries fails with probability (1/2)^20, about one in a million
# BIGO: Las Vegas: 2 probes expected. Monte Carlo: exactly `tries` probes at most.
def las_vegas_find_one(arr, rng):
    raise NotImplementedError


def monte_carlo_find_one(arr, rng, tries):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.13 | The trial-division baseline | Core
# PROMPT: Write `is_prime_trial(n)` checking divisors up to sqrt(n). Time it on a 12-digit prime and note why it is too slow for 100-digit numbers.
# EXAMPLE: `is_prime_trial(999_999_000_001)` -> `True` after about 500,000 divisions
# BIGO: O(sqrt N): exponential in the number of digits.
def is_prime_trial(n):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.14 | Fermat's little theorem, one base | Core
# PROMPT: If n is prime, `pow(a, n - 1, n) == 1` for every a not divisible by n. Write `fermat_witness(a, n)` returning True when a proves n composite.
# EXAMPLE: `fermat_witness(2, 15)` -> `True` (15 is composite); `fermat_witness(2, 13)` -> `False`
# BIGO: O(log n) multiplications with three-argument pow.
def fermat_witness(a, n):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.15 | Fermat's primality test | Core
# PROMPT: Write `fermat_test(n, k, rng)` trying k random bases in [2, n - 2] and answering "probably prime" (True) if none is a witness. Then show 561, a Carmichael number, fools every base coprime to it.
# EXAMPLE: `fermat_test(10**9 + 7, 20, rng)` -> `True`; `fermat_test(1_000_000_007 * 998_244_353, 20, rng)` -> `False`; `fermat_witness(2, 561)` -> `False` although 561 = 3 x 11 x 17
# BIGO: O(k log n). A Monte Carlo algorithm: "composite" is always right, "prime" can be wrong.
def fermat_test(n, k, rng):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.16 | Miller-Rabin, which Carmichael numbers cannot fool | Stretch
# PROMPT: Write `miller_rabin(n, bases=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37))`: write n - 1 = d x 2^s, and for each base check whether `a^d` is 1 or reaches n - 1 by repeated squaring. With these 12 bases it is exact for every n below 3.3 x 10^24.
# EXAMPLE: `miller_rabin(561)` -> `False`; `miller_rabin(2**61 - 1)` -> `True`
# BIGO: O(k log^3 n) bit operations; effectively instant for 64-bit numbers.
def miller_rabin(n, bases=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)):
    raise NotImplementedError
# ==== END


# ==== EX 7.4.17 | Simulate, then check against the formula | Practice
# PROMPT: Write `birthday_simulation(people, trials, rng)` estimating the chance that two of `people` share a birthday (365 days), and `birthday_exact(people)` from the product formula.
# EXAMPLE: 23 people -> exact `0.507...`; 20,000 simulated trials land within 0.02 of it
# BIGO: O(trials x people). When no formula exists, simulation is how you get the number.
def birthday_simulation(people, trials, rng):
    raise NotImplementedError


def birthday_exact(people):
    raise NotImplementedError
# ==== END
