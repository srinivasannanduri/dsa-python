import random
import string
from ch4_3_text_search import (brute_force_search, find_any, longest_repeat, prefix_search, prefix_table, PRIME,
                              rabin_karp, rabin_karp_monte_carlo, rolling_hashes, spurious_hits, window_sums)


def all_matches(text, needle):
    return [i for i in range(len(text) - len(needle) + 1) if text[i:i + len(needle)] == needle]


def random_text():
    return "".join(random.Random(7).choice(string.ascii_lowercase) for _ in range(10000))


def ab_cases():
    rng = random.Random(5)
    for _ in range(100):
        text = "".join(rng.choice("ab") for _ in range(rng.randint(0, 60)))
        needle = "".join(rng.choice("ab") for _ in range(rng.randint(1, 5)))
        yield text, needle


def test_ex_4_3_1():
    assert brute_force_search("abracadabra", "abra") == [0, 7]
    for text, needle in ab_cases():
        assert brute_force_search(text, needle) == all_matches(text, needle)


def test_ex_4_3_2():
    assert window_sums([1, 2, 3, 4, 5], 3) == [6, 9, 12]


def test_ex_4_3_3():
    assert rolling_hashes("abcd", 2) == [1, 28, 55]


def test_ex_4_3_4():
    assert rabin_karp("abracadabra", "abra") == [0, 7]
    for text, needle in ab_cases():
        assert rabin_karp(text, needle) == all_matches(text, needle)
        assert rabin_karp(text, needle, prime=7) == all_matches(text, needle)


def test_ex_4_3_5():
    text = random_text()
    assert spurious_hits(text, "abcde", 7) > 1000 and spurious_hits(text, "abcde", PRIME) == 0


def test_ex_4_3_6():
    assert rabin_karp_monte_carlo("abracadabra", "abra", random.Random(1)) == [0, 7]
    text = random_text()
    assert rabin_karp_monte_carlo(text, text[500:510], random.Random(2)) == all_matches(text, text[500:510])


def test_ex_4_3_7():
    assert find_any("thecatsatonthemat", ["cat", "mat", "dog"]) == [(3, 'cat'), (14, 'mat')]


def test_ex_4_3_8():
    assert longest_repeat("banana") == "ana" and longest_repeat("abcd") == "" and longest_repeat("aaaa") == "aaa"


def test_ex_4_3_9():
    assert prefix_table("abacabab") == [0, 0, 1, 0, 1, 2, 3, 2] and prefix_table("aaaa") == [0, 1, 2, 3] and prefix_table("") == []
    assert prefix_table("abcd") == [0, 0, 0, 0] and prefix_table("aabaaab") == [0, 1, 0, 1, 2, 2, 3]


def test_ex_4_3_10():
    assert prefix_search("abababca", "abab") == [0, 2] and prefix_search("aaaa", "aa") == [0, 1, 2] and prefix_search("abc", "d") == []
    assert prefix_search("ab", "abc") == [] and prefix_search("xabcabcx", "abcx") == [4] and prefix_search("", "a") == []
