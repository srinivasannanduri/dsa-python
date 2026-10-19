from ch2_5_strings import (anagram_starts, first_unique_index, letters_needed, longest_after_changes,
                          longest_palindrome, one_edit_apart, reverse_words, reversed_pairs, smallest_window,
                          underscore_matches)


def test_ex_2_5_1():
    chars = list('sun is up')
    assert reverse_words(chars) is chars and ''.join(chars) == 'up is sun'
    assert ''.join(reverse_words(list('solo'))) == 'solo' and reverse_words([]) == [] and ''.join(reverse_words(list('a b'))) == 'b a'


def test_ex_2_5_2():
    assert one_edit_apart('cart', 'card') and one_edit_apart('cart', 'art') and not one_edit_apart('cart', 'cards')
    assert not one_edit_apart('cart', 'cart') and one_edit_apart('', 'x') and not one_edit_apart('ab', 'ba') and one_edit_apart('art', 'cart')


def test_ex_2_5_3():
    assert first_unique_index('abacabad') == 3 and first_unique_index('aabb') == -1
    assert first_unique_index('') == -1 and first_unique_index('z') == 0 and first_unique_index('xxyz') == 2


def test_ex_2_5_4():
    assert letters_needed(['tool', 'loot', 'lot']) == 'loot'
    assert letters_needed(['a', 'b']) == 'ab' and letters_needed(['aa', 'a']) == 'aa' and letters_needed([]) == ''
    assert letters_needed(['abc', 'cab', 'cc']) == 'abcc'


def test_ex_2_5_5():
    assert reversed_pairs(['stop', 'tops', 'pots', 'spot', 'level']) == [['stop', 'pots'], ['tops', 'spot']]
    assert reversed_pairs([]) == [] and reversed_pairs(['noon', 'abc']) == [] and reversed_pairs(['ab', 'ba']) == [['ab', 'ba']]


def test_ex_2_5_6():
    assert longest_palindrome('noonabcbad') == 'abcba'
    assert longest_palindrome('') == '' and longest_palindrome('x') == 'x' and longest_palindrome('ab') == 'a' and longest_palindrome('cbbd') == 'bb'
    assert longest_palindrome('aaaa') == 'aaaa'


def test_ex_2_5_7():
    assert anagram_starts('tapatpta', 'pat') == [0, 2, 3, 5]
    assert anagram_starts('aaa', 'aa') == [0, 1] and anagram_starts('ab', 'abc') == [] and anagram_starts('xyz', 'q') == []


def test_ex_2_5_8():
    assert longest_after_changes('aabcabb', 2) == 5 and longest_after_changes('aabcabb', 0) == 2
    assert longest_after_changes('', 3) == 0 and longest_after_changes('abcd', 9) == 4 and longest_after_changes('abab', 1) == 3


def test_ex_2_5_9():
    assert underscore_matches('lalala la', 'la') == '_lalala_ _la_'
    assert underscore_matches('aaa', 'aa') == '_aaa_' and underscore_matches('abc', 'x') == 'abc' and underscore_matches('xx', 'x') == '_xx_'


def test_ex_2_5_10():
    assert smallest_window('bxaxcaxb', 'abc') == 'caxb' and smallest_window('abxab', 'aab') == 'abxa'
    assert smallest_window('abc', 'd') == '' and smallest_window('a', 'a') == 'a' and smallest_window('aa', 'aaa') == '' and smallest_window('xyz', '') == ''
