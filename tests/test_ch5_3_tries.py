from ch5_3_tries import (board_words, keypad_words, prefix_counts, RankedTrie, shortest_unique_prefixes,
                        substring_checks, Trie, trie_sort, wildcard_matches)


def trie(*words):
    t = Trie()
    for w in words:
        t.insert(w)
    return t


def test_ex_5_3_1():
    t = trie('pin', 'pit')
    assert list(t.root.children) == ['p'] and set(t.root.children['p'].children['i'].children) == {'n', 't'}
    assert '*' in t.root.children['p'].children['i'].children['n'].children


def test_ex_5_3_2():
    t = trie('pin', 'pit')
    assert t.search('pi') is not None and t.search('po') is None


def test_ex_5_3_3():
    t = trie('pin', 'pit')
    assert t.contains_word('pin') and not t.contains_word('pi')


def test_ex_5_3_4():
    assert trie('pin', 'pit', 'sun').collect_all_words() == ['pin', 'pit', 'sun']
    assert Trie().collect_all_words() == []


def test_ex_5_3_5():
    t = trie('pin', 'pinch', 'pit', 'sun')
    assert t.autocomplete('pin') == ['pin', 'pinch'] and t.autocomplete('x') == []


def test_ex_5_3_6():
    assert trie('pie', 'pin').all_keys() == ['p', 'i', 'e', 'n']


def test_ex_5_3_7():
    assert trie('pine', 'pint', 'pinto').longest_common_prefix() == 'pin'
    assert trie('pin', 'pinch').longest_common_prefix() == 'pin' and trie('sun').longest_common_prefix() == 'sun'
    assert trie('pin', 'sun').longest_common_prefix() == '' and Trie().longest_common_prefix() == ''


def test_ex_5_3_8():
    r = RankedTrie()
    r.insert('pinch', 9)
    r.insert('pin', 5)
    r.insert('pinball', 7)
    assert r.autocomplete('pin', 2) == ['pinch', 'pinball'] and r.autocomplete('z') == []


def test_ex_5_3_9():
    t = trie('pin', 'pinto', 'pinch')
    assert t.delete('pinch') and t.contains_word('pin') and not t.contains_word('pinch')
    assert 'c' not in t.search('pin').children and t.contains_word('pinto')
    assert not t.delete('sun') and not t.delete('pi')


def test_ex_5_3_10():
    assert prefix_counts(["car", "card", "care", "dog"], ["car", "ca", "d", "x"]) == [3, 3, 1, 0]
    assert prefix_counts(["a", "a", "ab"], ["a", "ab", "abc", ""]) == [3, 1, 0, 3] and prefix_counts([], ["a"]) == [0]


def test_ex_5_3_11():
    assert trie_sort(["pear", "apple", "pea", "app"]) == ["app", "apple", "pea", "pear"] and trie_sort([]) == []
    assert trie_sort(["b", "a", "b"]) == ["a", "b", "b"] and trie_sort(["ba", "b", "abc", "ab"]) == ["ab", "abc", "b", "ba"]


def test_ex_5_3_12():
    words = ["bad", "bed", "bid", "bud", "bead", "bad"]
    assert wildcard_matches(words, "b.d") == ["bad", "bed", "bid", "bud"] and wildcard_matches(words, "..") == []
    assert wildcard_matches(words, "b..d") == ["bead"] and wildcard_matches(words, "bad") == ["bad"] and wildcard_matches(words, ".e.") == ["bed"]


def test_ex_5_3_13():
    assert substring_checks("banana", ["nan", "ana", "nab", ""]) == [True, True, False, True]
    assert substring_checks("banana", ["banana", "bananas", "a"]) == [True, False, True]
    assert substring_checks("", [""]) == [True] and substring_checks("", ["a"]) == [False]


def test_ex_5_3_14():
    assert shortest_unique_prefixes(["zebra", "dog", "duck", "dove"]) == ["z", "dog", "du", "dov"]
    assert shortest_unique_prefixes(["a", "b"]) == ["a", "b"] and shortest_unique_prefixes(["abc"]) == ["a"]
    assert shortest_unique_prefixes(["ab", "ac", "bd"]) == ["ab", "ac", "b"] and shortest_unique_prefixes([]) == []


def test_ex_5_3_15():
    words = ["good", "home", "gone", "hood", "hoof", "in"]
    assert keypad_words("4663", words) == ["gone", "good", "home", "hood", "hoof"] and keypad_words("46", words) == ["in"]
    assert keypad_words("2", ["a", "b", "ab"]) == ["a", "b"] and keypad_words("", ["x"]) == [] and keypad_words("9", words) == []


def test_ex_5_3_16():
    words = ["car", "cat", "core", "tea", "rat", "bin", "rob", "cab", "tin", "ore", "rare"]
    assert board_words(["cat", "ore", "bin"], words) == ["bin", "car", "cat", "core", "ore", "rat", "rob", "tea"]
    assert board_words(["aa"], ["aaa", "aa", "a"]) == ["a", "aa"] and board_words([], ["a"]) == []
    assert board_words(["ab", "cd"], ["abdc", "acdb", "adcb", "bad", "abca"]) == ["abdc", "acdb", "adcb", "bad"]
