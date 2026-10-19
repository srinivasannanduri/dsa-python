import pytest
from ch2_3_linked_lists import (add_digit_lists, cycle_start_and_length, DoublyLinkedList, drop_sorted_duplicates,
                               flatten, interleave_ends, is_palindrome_list, LinkedList, LinkedQueue, meeting_node,
                               merge_sorted_lists, MultiNode, Node, partition_list, remove_kth_from_end,
                               rotate_right, sort_list, swap_pairs)


L = LinkedList.from_list


def test_ex_2_3_1():
    assert L([1, 2, 3]).to_list() == [1, 2, 3] and len(L([1, 2, 3])) == 3 and len(L([])) == 0
    lst = L([7])
    assert lst.head.data == 7 and lst.head.next is None


def test_ex_2_3_2():
    lst = L([10, 20, 30])
    assert lst.read(2) == 30 and lst.read(5) is None and lst.read(0) == 10


def test_ex_2_3_3():
    lst = L([10, 20, 30])
    assert lst.index_of(20) == 1 and lst.index_of(99) is None


def test_ex_2_3_4():
    lst = L([2, 3])
    lst.insert_at_start(1)
    assert lst.to_list() == [1, 2, 3]
    lst = L([])
    lst.insert_at_start(1)
    assert lst.to_list() == [1]


def test_ex_2_3_5():
    lst = L([1, 2])
    lst.insert_at_end(3)
    assert lst.to_list() == [1, 2, 3]
    lst = L([])
    lst.insert_at_end(1)
    assert lst.to_list() == [1]


def test_ex_2_3_6():
    lst = L([1, 2, 4])
    lst.insert_at(2, 3)
    assert lst.to_list() == [1, 2, 3, 4]
    lst.insert_at(4, 5)
    lst.insert_at(0, 0)
    assert lst.to_list() == [0, 1, 2, 3, 4, 5]
    with pytest.raises(IndexError):
        L([1]).insert_at(3, 9)


def test_ex_2_3_7():
    lst = L([1, 2, 3])
    assert lst.delete_at_start() == 1 and lst.to_list() == [2, 3]
    assert L([]).delete_at_start() is None


def test_ex_2_3_8():
    lst = L([1, 2, 3])
    assert lst.delete_at_end() == 3 and lst.to_list() == [1, 2]
    lst = L([1])
    assert lst.delete_at_end() == 1 and lst.to_list() == []


def test_ex_2_3_9():
    lst = L([1, 2, 9, 3])
    assert lst.delete_at(2) == 9 and lst.to_list() == [1, 2, 3]
    assert lst.delete_at(2) == 3 and lst.to_list() == [1, 2]
    with pytest.raises(IndexError):
        lst.delete_at(2)
    with pytest.raises(IndexError):
        L([]).delete_at(0)


def test_ex_2_3_10():
    lst = L([4, 5, 4])
    assert lst.delete_value(4) and lst.to_list() == [5, 4]
    assert lst.delete_value(4) and lst.to_list() == [5] and not lst.delete_value(7)


def test_ex_2_3_11():
    lst = L([1, 2, 3, 4, 5])
    second = lst.split_half()
    assert lst.to_list() == [1, 2, 3] and second.to_list() == [4, 5]
    even = L([1, 2, 3, 4])
    assert even.split_half().to_list() == [3, 4] and even.to_list() == [1, 2]
    one, empty = L([7]), L([])
    assert one.split_half().to_list() == [] and one.to_list() == [7] and empty.split_half().to_list() == []


def test_ex_2_3_12():
    lst = L([1, 2, 3])
    lst.reverse()
    assert lst.to_list() == [3, 2, 1]
    empty = L([])
    empty.reverse()
    assert empty.to_list() == []


def test_ex_2_3_13():
    a, b = L([1, 4, 7]), L([2, 3, 9])
    first_b = b.head
    merged = merge_sorted_lists(a, b)
    assert merged.to_list() == [1, 2, 3, 4, 7, 9] and merged.head.next is first_b
    assert merge_sorted_lists(L([]), L([5])).to_list() == [5] and merge_sorted_lists(L([2, 2]), L([2])).to_list() == [2, 2, 2]
    assert merge_sorted_lists(L([]), L([])).to_list() == []


def test_ex_2_3_14():
    cyc = L([1, 2, 3, 4])
    assert not cyc.has_cycle()
    cyc.head.next.next.next.next = cyc.head.next
    assert cyc.has_cycle()
    assert not L([]).has_cycle()


def test_ex_2_3_15():
    d = DoublyLinkedList()
    d.insert_at_end(2)
    d.insert_at_start(1)
    d.insert_at_end(3)
    assert d.to_list() == [1, 2, 3] and d.to_list_reversed() == [3, 2, 1]
    assert d.delete_at_end() == 3 and d.delete_at_start() == 1 and d.to_list() == [2]
    assert d.delete_at_end() == 2 and d.head is None and d.tail is None and d.delete_at_start() is None


def test_ex_2_3_16():
    q = LinkedQueue()
    for v in (1, 2, 3):
        q.enqueue(v)
    assert q.dequeue() == 1 and q.read() == 2


def test_ex_2_3_17():
    lst = L([1, 2, 3, 4, 5])
    assert remove_kth_from_end(lst, 2) == 4 and lst.to_list() == [1, 2, 3, 5]
    assert remove_kth_from_end(lst, 4) == 1 and lst.to_list() == [2, 3, 5]
    one = L([7])
    assert remove_kth_from_end(one, 1) == 7 and one.to_list() == []


def test_ex_2_3_18():
    assert add_digit_lists(L([9, 4, 1]), L([3, 8])).to_list() == [2, 3, 2]
    assert add_digit_lists(L([9, 9]), L([1])).to_list() == [0, 0, 1] and add_digit_lists(L([]), L([])).to_list() == []
    assert add_digit_lists(L([0]), L([0])).to_list() == [0] and add_digit_lists(L([5]), L([])).to_list() == [5]


def test_ex_2_3_19():
    shared = L([8, 9]).head
    a, b = LinkedList(Node(1, Node(2, shared))), LinkedList(Node(5, shared))
    assert meeting_node(a, b) is shared and meeting_node(b, a) is shared
    assert meeting_node(L([1, 2]), L([3])) is None and meeting_node(a, a) is a.head and meeting_node(L([]), b) is None


def test_ex_2_3_20():
    lst = L([1, 2, 3, 2, 1])
    assert is_palindrome_list(lst) and lst.to_list() == [1, 2, 3, 2, 1]
    lst = L([1, 2, 3, 1])
    assert not is_palindrome_list(lst) and lst.to_list() == [1, 2, 3, 1]
    assert is_palindrome_list(L([1, 2, 2, 1])) and not is_palindrome_list(L([1, 2])) and is_palindrome_list(L([])) and is_palindrome_list(L([4]))


def test_ex_2_3_21():
    for k, want in [(2, [4, 5, 1, 2, 3]), (7, [4, 5, 1, 2, 3]), (0, [1, 2, 3, 4, 5]), (5, [1, 2, 3, 4, 5]), (1, [5, 1, 2, 3, 4])]:
        lst = L([1, 2, 3, 4, 5])
        rotate_right(lst, k)
        assert lst.to_list() == want
    empty = L([])
    rotate_right(empty, 3)
    assert empty.to_list() == []


def test_ex_2_3_22():
    for values, want in [([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]), ([1, 2, 3, 4], [1, 4, 2, 3]), ([1, 2], [1, 2]), ([1], [1]), ([], [])]:
        lst = L(values)
        interleave_ends(lst)
        assert lst.to_list() == want


def test_ex_2_3_23():
    lst = L([1, 2, 3, 4, 5])
    first = lst.head
    swap_pairs(lst)
    assert lst.to_list() == [2, 1, 4, 3, 5] and lst.head.next is first
    for values, want in [([], []), ([1], [1]), ([1, 2], [2, 1]), ([1, 2, 3, 4], [2, 1, 4, 3])]:
        lst = L(values)
        swap_pairs(lst)
        assert lst.to_list() == want


def test_ex_2_3_24():
    lst = L([3, 1, 2])
    three = lst.head
    sort_list(lst)
    assert lst.to_list() == [1, 2, 3] and lst.head.next.next is three
    for values in ([5, 1, 4, 2, 3, 1], [], [2, 1], [7], [4, 4, 1, 9, 0, 3, 8]):
        lst = L(values)
        sort_list(lst)
        assert lst.to_list() == sorted(values)


def test_ex_2_3_25():
    for values, want in [([1, 1, 2, 3, 3, 3], [1, 2, 3]), ([], []), ([4, 4], [4]), ([1, 2], [1, 2]), ([0, 0, 0, 5], [0, 5])]:
        lst = L(values)
        drop_sorted_duplicates(lst)
        assert lst.to_list() == want


def test_ex_2_3_26():
    for values, x, want in [([4, 1, 6, 2, 5, 2], 4, [1, 2, 2, 4, 6, 5]), ([3, 1], 0, [3, 1]), ([], 5, []), ([5, 6, 1], 9, [5, 6, 1]), ([9, 2, 8, 1], 5, [2, 1, 9, 8])]:
        lst = L(values)
        partition_list(lst, x)
        assert lst.to_list() == want


def test_ex_2_3_27():
    n = {v: MultiNode(v) for v in range(1, 9)}
    n[1].next, n[2].next, n[3].next, n[5].next = n[2], n[3], n[4], n[6]
    n[2].child, n[5].child, n[4].child = n[5], n[7], n[8]
    values, node = [], flatten(n[1])
    while node:
        assert node.child is None
        values.append(node.data)
        node = node.next
    assert values == [1, 2, 5, 7, 6, 3, 4, 8] and flatten(None) is None


def test_ex_2_3_28():
    assert cycle_start_and_length(lambda x: (x * x + 1) % 11, 0) == [4, 2]
    assert cycle_start_and_length(lambda x: (x + 1) % 5, 0) == [0, 5] and cycle_start_and_length(lambda x: x // 2, 20) == [5, 1]
    digit_squares = lambda x: sum(int(d) ** 2 for d in str(x))
    assert cycle_start_and_length(digit_squares, 7) == [5, 1] and cycle_start_and_length(digit_squares, 4) == [0, 8]
