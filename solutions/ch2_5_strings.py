"""Chapter 2.5: Strings."""


# ==== EX 2.5.1 | Reverse the word order in place | Core
# PROMPT: `chars` is a list of characters holding words separated by single spaces. Write `reverse_words(chars)` that reverses the order of the words in place and returns `chars`: reverse the whole list, then reverse each word.
# EXAMPLE: `list('sun is up')` -> `list('up is sun')`
# BIGO: O(N) time, O(1) extra space: reversing everything puts the words in the right order but backwards; reversing each word fixes the letters.
def reverse_words(chars):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.2 | One edit apart | Core
# PROMPT: Write `one_edit_apart(a, b)`: `True` when exactly one insertion, deletion or replacement of a character turns `a` into `b` (equal strings are zero edits apart).
# EXAMPLE: `'cart', 'card'` -> `True`; `'cart', 'art'` -> `True`; `'cart', 'cards'` -> `False`
# BIGO: O(N): one walk with two pointers; the first mismatch decides which pointer skips.
def one_edit_apart(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.3 | First unique character | Core
# PROMPT: Write `first_unique_index(s)` returning the index of the first character that appears exactly once in `s`, or -1.
# EXAMPLE: `'abacabad'` -> `3`; `'aabb'` -> `-1`
# BIGO: O(N): one pass counts, a second pass finds the first character with a count of one.
def first_unique_index(s):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.4 | Letters needed to write any word | Core
# PROMPT: Write `letters_needed(words)` returning, as one sorted string, the smallest bag of letters from which any single word in `words` can be spelled (each letter as many times as the word that needs it most).
# EXAMPLE: `['tool', 'loot', 'lot']` -> `'loot'`
# BIGO: O(C + A log A) for C characters in all and A distinct letters: one count table per word, keeping the largest count of each letter.
def letters_needed(words):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.5 | Reversed-word pairs | Core
# PROMPT: Write `reversed_pairs(words)` for a list of distinct words: whenever a word's reverse appeared earlier in the list (and the word is not a palindrome), add `[earlier_word, word]`, in the order the second words appear.
# EXAMPLE: `['stop', 'tops', 'pots', 'spot', 'level']` -> `[['stop', 'pots'], ['tops', 'spot']]`
# BIGO: O(N * L) for N words of length L: one reversal and one set lookup per word.
def reversed_pairs(words):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.6 | Longest palindromic substring | Practice
# PROMPT: Write `longest_palindrome(s)` returning the longest substring that reads the same both ways (the earliest one on a tie, `''` for an empty string). Expand outwards from every centre: each character, and each gap between two characters.
# EXAMPLE: `'noonabcbad'` -> `'abcba'`
# BIGO: O(N^2) time, O(1) space: 2N - 1 centres, each expanded at most N/2 steps.
def longest_palindrome(s):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.7 | Anagram windows | Practice
# PROMPT: Write `anagram_starts(text, word)` returning every index where `text` has a window of `len(word)` characters that is an anagram of `word`. Slide the window one character at a time, updating a count table instead of recounting.
# EXAMPLE: `'tapatpta', 'pat'` -> `[0, 2, 3, 5]`
# BIGO: O(N * A) for a text of length N and A distinct letters: slide a fixed-size window, adding one character and removing one per step, then compare the two count tables.
def anagram_starts(text, word):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.8 | Longest run after k changes | Practice
# PROMPT: Write `longest_after_changes(s, k)`: the length of the longest substring that can be made all one letter by changing at most `k` of its characters. Slide a window; it is valid while its length minus the count of its most common letter is at most `k`.
# EXAMPLE: `'aabcabb', 2` -> `5`
# BIGO: O(N): the window only grows or slides; the most common letter's count never needs to shrink for the answer to stay right.
def longest_after_changes(s, k):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.9 | Underscore every match | Practice
# PROMPT: Write `underscore_matches(text, word)` that wraps every occurrence of `word` in `text` with `_` on each side, merging occurrences that overlap or touch into one wrapped stretch.
# EXAMPLE: `'lalala la', 'la'` -> `'_lalala_ _la_'`
# BIGO: O(N * M) to find the matches of a word of length M, then O(N) to merge the spans and write the result.
def underscore_matches(text, word):
    raise NotImplementedError
# ==== END


# ==== EX 2.5.10 | Smallest window holding every wanted letter | Stretch
# PROMPT: Write `smallest_window(text, wanted)` returning the shortest substring of `text` that contains every character of `wanted`, counting repeats (the earliest on a tie, `''` if there is none). Grow the window until it covers `wanted`, then shrink it from the left while it still does.
# EXAMPLE: `'bxaxcaxb', 'abc'` -> `'caxb'`
# BIGO: O(N + M): each index of the text enters and leaves the window at most once, and a counter of missing letters makes the validity check O(1).
def smallest_window(text, wanted):
    raise NotImplementedError
# ==== END
