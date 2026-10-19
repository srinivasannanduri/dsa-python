"""Chapter 5.3: Tries."""


# ==== EX 5.3.1 | Trie node and insertion | Core | class=Trie
# PROMPT: Create `TrieNode` with a `children` dict and `Trie` with a `root`. Write `insert(word)` that walks or creates one child per character, then adds a `'*'` child to mark the end of the word.
# EXAMPLE: insert 'pin', 'pit' -> root has one child `'p'`, whose `'i'` child has children `'n'` and `'t'`
# BIGO: O(K) for a K-character word, regardless of how many words are stored.
class TrieNode:
    def __init__(self):
        raise NotImplementedError


class Trie:
    def __init__(self):
        raise NotImplementedError

    def insert(self, word):
        raise NotImplementedError
# ==== END

    # ==== EX 5.3.2 | Search a prefix | Core | class=Trie
    # PROMPT: Add `search(prefix)` returning the node where the prefix ends, or `None` if it is not in the trie.
    # EXAMPLE: After 'pin' -> `search('pi')` is a node; `search('po')` is `None`
    # BIGO: O(K).
    def search(self, prefix):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.3.3 | Is it a whole word? | Core | class=Trie
    # PROMPT: Add `contains_word(word)`: the prefix must exist and its node must have a `'*'` child.
    # EXAMPLE: After 'pin' -> `contains_word('pin')` is `True`, `contains_word('pi')` is `False`
    # BIGO: O(K).
    def contains_word(self, word):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.3.4 | Collect every word | Core | class=Trie
    # PROMPT: Add `collect_all_words(node=None, word='', words=None)` that recursively gathers every word below `node` (the root by default).
    # EXAMPLE: After 'pin', 'pit', 'sun' -> `['pin', 'pit', 'sun']` (insertion order)
    # BIGO: O(M) for M nodes beneath the starting node.
    def collect_all_words(self, node=None, word="", words=None):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.3.5 | Autocomplete | Core | class=Trie
    # PROMPT: Add `autocomplete(prefix)`: search to the prefix's node, collect the words below it and prepend the prefix.
    # EXAMPLE: Words 'pin', 'pinch', 'pit', 'sun' -> `autocomplete('pin')` -> `['pin', 'pinch']`
    # BIGO: O(K + M): reach the prefix, then visit only the matching subtree.
    def autocomplete(self, prefix):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.3.6 | Print every key | Practice | class=Trie
    # PROMPT: Add `all_keys()` returning every character stored in the trie (excluding `'*'`), depth first.
    # EXAMPLE: After 'pie', 'pin' -> `['p', 'i', 'e', 'n']`
    # BIGO: O(M) nodes.
    def all_keys(self, node=None, keys=None):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.3.7 | Longest prefix every word shares | Practice | class=Trie
    # PROMPT: Add `longest_common_prefix()`: walk down from the root while the current node has exactly one child and no word ends there, collecting the characters. Return `''` for an empty trie.
    # EXAMPLE: Words 'pine', 'pint', 'pinto' -> `'pin'`; words 'pin', 'pinch' -> `'pin'`
    # BIGO: O(P) where P is the length of the shared prefix: only one path is ever walked.
    def longest_common_prefix(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 5.3.9 | Delete a word | Stretch | class=Trie
    # PROMPT: Add `delete(word)` that removes the end marker and prunes nodes that no longer lead to any word. Return `True` if the word was present.
    # EXAMPLE: Words 'pin', 'pinch' -> delete 'pinch' -> 'pin' still found, the 'c-h' nodes are gone
    # BIGO: O(K).
    def delete(self, word):
        raise NotImplementedError
    # ==== END


# ==== EX 5.3.8 | Tries with values: ranked autocomplete | Practice | class=RankedTrie
# PROMPT: Build `RankedTrie(Trie)` whose `insert(word, popularity)` stores the popularity under `'*'`. Add `autocomplete(prefix, limit=3)` returning the most popular completions first.
# EXAMPLE: ('pinch', 9), ('pin', 5), ('pinball', 7) -> `autocomplete('pin', 2)` -> `['pinch', 'pinball']`
# BIGO: O(K + M + R log R) to collect and sort R matches.
class RankedTrie(Trie):
    def insert(self, word, popularity=0):
        raise NotImplementedError

    def _collect(self, node, word, out):
        raise NotImplementedError

    def autocomplete(self, prefix, limit=3):
        raise NotImplementedError
# ==== END


class WordNode:
    """Trie node for 5.3.10-5.3.16: `next` maps a letter to a child, `passes` counts the words through it, `ends` the words ending at it."""

    def __init__(self):
        self.next = {}
        self.passes = 0
        self.ends = 0


def word_trie(words):
    """Build a `WordNode` trie holding `words`, repeats counted."""
    root = WordNode()
    for word in words:
        node = root
        node.passes += 1
        for ch in word:
            node = node.next.setdefault(ch, WordNode())
            node.passes += 1
        node.ends += 1
    return root


# ==== EX 5.3.10 | Count the words under each prefix | Core
# PROMPT: Write `prefix_counts(words, prefixes)` that returns, for each prefix, how many of `words` (repeats included) start with it. Use the `word_trie(words)` helper: each `WordNode` has `next` (letter -> child), `passes` and `ends`. Walk each prefix down from the root and read `passes`.
# EXAMPLE: `["car", "card", "care", "dog"], ["car", "ca", "d", "x"]` -> `[3, 3, 1, 0]`
# BIGO: O(total letters) to build, then O(K) per prefix of length K: the node at the end of the prefix already counts every word passing through it.
def prefix_counts(words, prefixes):
    raise NotImplementedError
# ==== END


# ==== EX 5.3.11 | Sort words with a trie | Core
# PROMPT: Write `trie_sort(words)` that returns `words` in dictionary order, repeats kept, by walking a trie: emit a node's word `ends` times, then visit its children in letter order. Use the `word_trie(words)` helper: each `WordNode` has `next` (letter -> child), `passes` and `ends`.
# EXAMPLE: `["pear", "apple", "pea", "app"]` -> `["app", "apple", "pea", "pear"]`
# BIGO: O(total letters) plus the sort of each node's children: a pre-order walk that takes children in letter order meets the words in dictionary order.
def trie_sort(words):
    raise NotImplementedError
# ==== END


# ==== EX 5.3.12 | Wildcard search | Practice
# PROMPT: Write `wildcard_matches(words, pattern)` that returns, in dictionary order and without repeats, the words matching `pattern`, where `.` matches any one letter. Walk the trie: a letter follows one child, a dot tries every child in letter order. Use the `word_trie(words)` helper: each `WordNode` has `next` (letter -> child), `passes` and `ends`.
# EXAMPLE: `["bad", "bed", "bid", "bud", "bead"], "b.d"` -> `["bad", "bed", "bid", "bud"]`
# BIGO: O(26^D * K) worst case for D dots in a pattern of length K, far less in practice: each dot branches only into children that exist.
def wildcard_matches(words, pattern):
    raise NotImplementedError
# ==== END


# ==== EX 5.3.13 | Substring check with a suffix trie | Practice
# PROMPT: Write `substring_checks(text, queries)` that returns, for each query, whether it occurs in `text` (the empty string always does). Put every suffix of `text` in a trie, then walk each query from the root. Use the `word_trie(words)` helper: each `WordNode` has `next` (letter -> child), `passes` and `ends`.
# EXAMPLE: `"banana", ["nan", "ana", "nab", ""]` -> `[True, True, False, True]`
# BIGO: O(N^2) time and space to build for a text of length N, then O(M) per query of length M: every substring is a prefix of some suffix.
# NOTE: Suffix trees and suffix arrays get the build down to O(N) or O(N log N); the query idea is the same.
def substring_checks(text, queries):
    raise NotImplementedError
# ==== END


# ==== EX 5.3.14 | Shortest unique prefixes | Practice
# PROMPT: `words` are distinct and none is a prefix of another. Write `shortest_unique_prefixes(words)` that returns, for each word in order, its shortest non-empty prefix that no other word starts with. Walk each word down until a node is passed by one word only. Use the `word_trie(words)` helper: each `WordNode` has `next` (letter -> child), `passes` and `ends`.
# EXAMPLE: `["zebra", "dog", "duck", "dove"]` -> `["z", "dog", "du", "dov"]`
# BIGO: O(total letters) time and space: the `passes` count on each node says at once whether any other word shares the prefix so far.
def shortest_unique_prefixes(words):
    raise NotImplementedError
# ==== END


# ==== EX 5.3.15 | Keypad words | Practice
# PROMPT: On a phone keypad, `2` is `abc`, `3` `def`, `4` `ghi`, `5` `jkl`, `6` `mno`, `7` `pqrs`, `8` `tuv` and `9` `wxyz`. Write `keypad_words(digits, words)` that returns, in dictionary order, the words from `words` whose letters type exactly `digits`. Walk the trie, trying each letter of the current digit. Use the `word_trie(words)` helper: each `WordNode` has `next` (letter -> child), `passes` and `ends`.
# EXAMPLE: `"4663", ["good", "home", "gone", "hood", "hoof", "in"]` -> `["gone", "good", "home", "hood", "hoof"]`
# BIGO: O(4^K) worst case for K digits, usually far less: the trie cuts off every letter sequence that starts no word.
def keypad_words(digits, words):
    raise NotImplementedError
# ==== END


# ==== EX 5.3.16 | Words on a letter board | Stretch
# PROMPT: `board` is a list of equal-length strings. A word can be traced by starting on any cell and stepping to any of the 8 neighbouring cells, using each cell at most once. Write `board_words(board, words)` that returns, sorted and without repeats, the words from `words` that can be traced. Start a depth-first walk from every cell, following the trie in step with the path. Use the `word_trie(words)` helper: each `WordNode` has `next` (letter -> child), `passes` and `ends`.
# EXAMPLE: `["cat", "ore", "bin"]`, `["car", "cat", "core", "tea", "rat", "bin", "rob", "cab", "tin", "ore", "rare"]` -> `["bin", "car", "cat", "core", "ore", "rat", "rob", "tea"]`
# BIGO: O(R * C * 8^L) worst case for words up to length L, in practice far less: the walk stops as soon as the path so far starts no word.
def board_words(board, words):
    raise NotImplementedError
# ==== END
