from collections import deque
from ch2_4_stacks_queues import (after_collisions, binary_numbers, CircularQueue, Editor, eval_rpn, largest_rectangle,
                                longest_balanced, MinMaxStack, next_greater, Queue, QueueStack, reverse_first_k,
                                round_robin, simplify_path, sort_stack, Stack, StackQueue, sunset_view,
                                tags_balanced, window_max)


def test_ex_2_4_1():
    s = Stack()
    assert s.is_empty()
    for v in (1, 2, 3):
        s.push(v)
    assert s.read() == 3 and s.pop() == 3 and s.read() == 2 and len(s) == 2 and not s.is_empty()
    assert Stack().pop() is None


def test_ex_2_4_2():
    q = Queue()
    assert q.is_empty()
    for v in (1, 2, 3):
        q.enqueue(v)
    assert q.dequeue() == 1 and q.read() == 2 and len(q) == 2 and not q.is_empty()


def test_ex_2_4_3():
    assert tags_balanced('<p><b>hi</b></p>') and not tags_balanced('<p><b></p></b>')
    assert not tags_balanced('<p>') and not tags_balanced('</p>') and tags_balanced('plain text')
    assert tags_balanced('<a><b></b><c>x</c></a>') and not tags_balanced('<a></a></a>')


def test_ex_2_4_4():
    assert simplify_path('/a/./b/../c/') == '/a/c' and simplify_path('/../') == '/'
    assert simplify_path('/home//user/') == '/home/user' and simplify_path('/a/b/../../..') == '/'
    assert simplify_path('/x/y/./z') == '/x/y/z'


def test_ex_2_4_5():
    assert round_robin(['a', 'b', 'c'], [3, 1, 2], 1) == ['b', 'c', 'a']
    assert round_robin(['a', 'b', 'c'], [3, 1, 2], 5) == ['a', 'b', 'c']
    assert round_robin(['x', 'y'], [4, 4], 2) == ['x', 'y'] and round_robin([], [], 3) == []


def test_ex_2_4_6():
    sq = StackQueue()
    sq.enqueue(1)
    sq.enqueue(2)
    assert sq.dequeue() == 1
    sq.enqueue(3)
    assert sq.dequeue() == 2 and sq.dequeue() == 3 and sq.dequeue() is None


def test_ex_2_4_7():
    assert eval_rpn(['3', '4', '+', '2', '*']) == 14
    assert eval_rpn(['10', '4', '-']) == 6 and eval_rpn(['9', '2', '/']) == 4.5


def test_ex_2_4_8():
    e = Editor()
    e.type('a')
    e.type('b')
    assert e.undo() == 'a' and e.redo() == 'ab'
    e.undo()
    e.type('c')
    assert e.text == 'ac' and e.redo() == 'ac' and e.undo() == 'a' and e.undo() == '' and e.undo() == ''


def test_ex_2_4_9():
    c = CircularQueue(3)
    assert all(c.enqueue(v) for v in (1, 2, 3)) and not c.enqueue(4)
    assert c.dequeue() == 1 and c.enqueue(4) and c.data[0] == 4
    assert [c.dequeue() for _ in range(4)] == [2, 3, 4, None]


def test_ex_2_4_10():
    s = MinMaxStack()
    for v in (5, 2, 8):
        s.push(v)
    assert (s.min(), s.max(), s.peek()) == (2, 8, 8)
    assert s.pop() == 8 and (s.min(), s.max()) == (2, 5)
    assert s.pop() == 2 and (s.min(), s.max()) == (5, 5)
    s.push(5)
    s.push(-1)
    assert (s.min(), s.max(), s.peek()) == (-1, 5, -1)


def test_ex_2_4_11():
    assert next_greater([2, 7, 3, 5, 4, 6, 8]) == [7, 8, 5, 6, 6, 8, -1] and next_greater([]) == []
    assert next_greater([5, 4, 3]) == [-1, -1, -1] and next_greater([1, 1, 2]) == [2, 2, -1]


def test_ex_2_4_12():
    assert sunset_view([3, 5, 4, 4, 3, 1, 3, 2]) == [1, 3, 6, 7] and sunset_view([]) == []
    assert sunset_view([1, 2, 3]) == [2] and sunset_view([3, 2, 1]) == [0, 1, 2] and sunset_view([2, 2]) == [1]


def test_ex_2_4_13():
    assert largest_rectangle([2, 4, 3, 5, 1, 3]) == 9 and largest_rectangle([2, 1, 2]) == 3 and largest_rectangle([]) == 0
    assert largest_rectangle([5]) == 5 and largest_rectangle([1, 1, 1, 1]) == 4 and largest_rectangle([2, 3, 4, 5]) == 9


def test_ex_2_4_14():
    stack = [3, 1, 4, 2]
    out = sort_stack(stack)
    assert stack == [] and [out.pop() for _ in range(4)] == [4, 3, 2, 1]
    assert sort_stack([]) == [] and sort_stack([2, 2, 1]) == [1, 2, 2] and sort_stack([1, 2, 3]) == [1, 2, 3]


def test_ex_2_4_15():
    assert after_collisions([-3, 4, 9, -6, 2, -2, 7]) == [-3, 4, 9, 7] and after_collisions([4, 9, -6, 2, -2, -10]) == [-10]
    assert after_collisions([5, -5]) == [] and after_collisions([-1, 1]) == [-1, 1] and after_collisions([]) == []


def test_ex_2_4_16():
    assert window_max([4, 2, 12, 3, 8, 1, 7], 3) == [12, 12, 12, 8, 8] and window_max([3, 1, 2], 1) == [3, 1, 2]
    assert window_max([3, 1, 2], 3) == [3] and window_max([5, 4, 3, 2, 1], 2) == [5, 4, 3, 2] and window_max([1, 3, 3, 1], 2) == [3, 3, 3]


def test_ex_2_4_17():
    assert longest_balanced("(()())())(") == 8 and longest_balanced("") == 0 and longest_balanced(")(") == 0
    assert longest_balanced("()(()") == 2 and longest_balanced("(()") == 2 and longest_balanced("()()") == 4 and longest_balanced("))()(())") == 6


def test_ex_2_4_18():
    s = QueueStack()
    assert s.is_empty()
    for v in (1, 2, 3):
        s.push(v)
    assert s.pop() == 3 and s.peek() == 2 and not s.is_empty()
    s.push(4)
    assert [s.pop(), s.pop(), s.pop()] == [4, 2, 1] and s.is_empty()


def test_ex_2_4_19():
    q = deque([1, 2, 3, 4, 5])
    assert reverse_first_k(q, 3) is q and list(q) == [3, 2, 1, 4, 5]
    assert list(reverse_first_k(deque([1, 2, 3]), 0)) == [1, 2, 3] and list(reverse_first_k(deque([1, 2, 3]), 3)) == [3, 2, 1]
    assert list(reverse_first_k(deque(), 0)) == []


def test_ex_2_4_20():
    assert binary_numbers(5) == ["1", "10", "11", "100", "101"] and binary_numbers(0) == [] and binary_numbers(1) == ["1"]
    assert binary_numbers(16)[-1] == "10000" and binary_numbers(16) == [format(i, "b") for i in range(1, 17)]
