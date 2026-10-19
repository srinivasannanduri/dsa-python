"""Chapter 2.4: Stacks and queues."""
from collections import deque


# ==== EX 2.4.1 | Stack | Core | class=Stack
# PROMPT: Build `Stack` on a Python list, exposing only `push`, `pop`, `read` (peek), `is_empty` and `__len__`. `pop` and `read` return `None` when empty.
# EXAMPLE: push 1, 2, 3 -> `read()` is `3`, `pop()` is `3`, `read()` is `2`
# BIGO: O(1) for every operation. The end of a list is the cheap end.
# NOTE: A stack is an abstract data type: the constraint (last in, first out) matters, not the list underneath.
class Stack:
    def __init__(self):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.4.2 | Queue | Core | class=Queue
# PROMPT: Build `Queue` with `enqueue`, `dequeue`, `read` (front), `is_empty`, `__len__`. Use `collections.deque`, then explain why `list.pop(0)` would be a poor choice.
# EXAMPLE: enqueue 1, 2, 3 -> `dequeue()` is `1`, `read()` is `2`
# BIGO: O(1) each with a deque. `list.pop(0)` is O(N) because every element shifts left (see 2.1.11).
class Queue:
    def __init__(self):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.4.3 | Do the tags nest? | Core
# PROMPT: Write `tags_balanced(markup)` using your `Stack`. Tags are `<name>` and `</name>` with letters only and no attributes; text between tags is ignored. Return `True` when every tag closes, in the reverse order it opened.
# EXAMPLE: `'<p><b>hi</b></p>'` -> `True`; `'<p><b></p></b>'` -> `False`
# BIGO: O(N) time, O(N) space for the stack.
def tags_balanced(markup):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.4 | Simplify a file path | Core
# PROMPT: Write `simplify_path(path)` for an absolute path: drop empty parts and `.`, let `..` remove the folder before it (if any), and return the canonical path. Use your `Stack` for the folders.
# EXAMPLE: `'/a/./b/../c/'` -> `'/a/c'`; `'/../'` -> `'/'`
# BIGO: O(N) time and space.
def simplify_path(path):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.5 | Round-robin turns | Core
# PROMPT: Write `round_robin(names, times, slice_)` using your `Queue`: job `names[i]` needs `times[i]` units of work. The front job runs for up to `slice_` units; if it still has work left it goes to the back. Return the names in the order the jobs finish.
# EXAMPLE: `['a', 'b', 'c'], [3, 1, 2], 1` -> `['b', 'c', 'a']`
# BIGO: O(T / s + N) queue operations for total work T, slice s and N jobs; each one is O(1).
def round_robin(names, times, slice_):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.6 | Queue built from two stacks | Practice | class=StackQueue
# PROMPT: Build `StackQueue` with `enqueue` and `dequeue` using only two `Stack` objects.
# EXAMPLE: enqueue 1, 2; dequeue -> `1`; enqueue 3; dequeue -> `2`, dequeue -> `3`
# BIGO: O(1) amortized: each element is moved from the inbox to the outbox at most once.
class StackQueue:
    def __init__(self):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.4.7 | Evaluate postfix (RPN) | Practice
# PROMPT: Write `eval_rpn(tokens)` for `+ - * /` (true division) using a stack.
# EXAMPLE: `['3', '4', '+', '2', '*']` -> `14`
# BIGO: O(N).
def eval_rpn(tokens):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.8 | Undo and redo | Practice | class=Editor
# PROMPT: Build `Editor` with `type(text)`, `undo()`, `redo()` and a `text` attribute. Use one stack of past states and one of undone states; new typing clears redo.
# EXAMPLE: type 'a', type 'b', undo -> `'a'`; redo -> `'ab'`
# BIGO: O(1) per operation (plus the cost of building the new string).
class Editor:
    def __init__(self):
        raise NotImplementedError

    def type(self, chars):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError

    def redo(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.4.9 | Fixed-size circular queue | Stretch | class=CircularQueue
# PROMPT: Build `CircularQueue(capacity)` on a fixed list with `head` and `size`, so neither `enqueue` nor `dequeue` shifts anything. `enqueue` returns `False` when full.
# EXAMPLE: capacity 3: enqueue 1, 2, 3 -> 4th returns `False`; dequeue -> `1`; enqueue 4 succeeds and wraps to slot 0
# BIGO: O(1) for both, with no shifting, because the index wraps with `% capacity`.
class CircularQueue:
    def __init__(self, capacity):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.4.10 | Min-max stack | Core | class=MinMaxStack
# PROMPT: Build `MinMaxStack` with `push(value)`, `pop()`, `peek()`, `min()` and `max()`, every one O(1). Store each value together with the minimum and maximum of the stack at the moment it was pushed. Callers never pop or read an empty stack.
# EXAMPLE: push 5, 2, 8 -> `min()` is `2`, `max()` is `8`; `pop()` -> `8`; `max()` is `5`
# BIGO: O(1) per operation, O(N) space: each entry stores the minimum and maximum of itself and everything below it, so popping restores the old ones for free.
class MinMaxStack:
    def __init__(self):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def min(self):
        raise NotImplementedError

    def max(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.4.11 | Next greater value | Core
# PROMPT: Write `next_greater(nums)` that returns, for each index, the first value to its right that is larger, or `-1`. Keep a stack of indices still waiting; each new value settles every waiting index with a smaller value.
# EXAMPLE: `[2, 7, 3, 5, 4, 6, 8]` -> `[7, 8, 5, 6, 6, 8, -1]`
# BIGO: O(N) time and space: each index is pushed and popped at most once, and the stack always holds indices still waiting for a larger value.
def next_greater(nums):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.12 | Sunset view | Core
# PROMPT: `heights` lists buildings from west to east, and the sun sets in the east. Write `sunset_view(heights)` that returns, in ascending order, the indices of the buildings strictly taller than every building east of them. Scan west to east with a stack, popping every building that is not taller than the new one.
# EXAMPLE: `[3, 5, 4, 4, 3, 1, 3, 2]` -> `[1, 3, 6, 7]`
# BIGO: O(N) time and space: a building that is not taller than a later one can never see past it, so it leaves the stack for good.
def sunset_view(heights):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.13 | Largest rectangle under a bar chart | Stretch
# PROMPT: `heights` are the bars of a chart, each 1 wide. Write `largest_rectangle(heights)` that returns the largest rectangle area that fits under the bars. Keep a stack of `(start, height)` with rising heights; a lower bar pops every taller entry, scoring `height * (i - start)`, and inherits the start of the last one popped. A final zero-height bar empties the stack.
# EXAMPLE: `[2, 4, 3, 5, 1, 3]` -> `9` (height 3 across the bars `4, 3, 5`)
# BIGO: O(N) time and space: a bar is popped exactly when the first lower bar to its right appears, and the entry below it says how far left it reaches.
def largest_rectangle(heights):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.14 | Sort a stack with one more stack | Practice
# PROMPT: A stack is a list with its top at the end. Write `sort_stack(stack)` that empties `stack` into a new stack whose values rise from bottom to top (largest on top) and returns it, using only push, pop and a look at the top of the two stacks: pop a value, move every larger value from the new stack back onto the old one, then push it.
# EXAMPLE: push 3, 1, 4, 2 -> popping the result gives `4, 3, 2, 1`
# BIGO: O(N^2) time, O(N) space for the second stack: each value may have to move every larger value aside before it settles.
def sort_stack(stack):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.15 | Collisions on a track | Practice
# PROMPT: `carts` lists carts on a track from left to right: the size is the absolute value, and the sign is the direction (positive moves right). When two meet, the smaller one is destroyed; equal sizes destroy each other. Write `after_collisions(carts)` that returns the carts left, in order. A stack of survivors works: only a left-mover arriving at a right-mover on top collides.
# EXAMPLE: `[-3, 4, 9, -6, 2, -2, 7]` -> `[-3, 4, 9, 7]`
# BIGO: O(N) time and space: every cart is pushed once and destroyed at most once.
def after_collisions(carts):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.16 | Window maximum with a deque | Practice
# PROMPT: Write `window_max(nums, k)` that returns the maximum of every window of `k` consecutive values (`1 <= k <= len(nums)`), in O(N). Keep a `deque` of indices whose values fall from front to back: drop smaller values from the back before adding, and drop the front once it leaves the window.
# EXAMPLE: `[4, 2, 12, 3, 8, 1, 7], 3` -> `[12, 12, 12, 8, 8]`
# BIGO: O(N) time, O(K) space: the deque keeps indices of falling values, so its front is the window's maximum, and each index enters and leaves once.
def window_max(nums, k):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.17 | Longest balanced bracket run | Practice
# PROMPT: `s` holds only `(` and `)`. Write `longest_balanced(s)` that returns the length of the longest substring of correctly matched brackets. Keep a stack of indices starting with `-1`: push each `(`; on `)` pop, then either measure from the new top or, if the stack is empty, push this index as the new boundary.
# EXAMPLE: `"(()())())("` -> `8`
# BIGO: O(N) time and space: the stack holds open-bracket indices above the index of the last unmatched close, which marks where a balanced run can start.
def longest_balanced(s):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.18 | Stack from a queue | Core | class=QueueStack
# PROMPT: Build `QueueStack` with `push(value)`, `pop()`, `peek()` and `is_empty()` on one `deque` used only as a queue (`append`, `popleft`, `[0]`, `len`). After appending, rotate the older values from the front to the back so the newest is in front. Callers never pop or peek an empty stack.
# EXAMPLE: push 1, 2, 3; `pop()` -> `3`; `peek()` -> `2`
# BIGO: O(N) push, O(1) pop and peek: after each push the queue is rotated so the newest value is at the front.
class QueueStack:
    def __init__(self):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError
# ==== END


# ==== EX 2.4.19 | Reverse the first k of a queue | Core
# PROMPT: Write `reverse_first_k(queue, k)` that reverses the first `k` values of a `deque` in place (`0 <= k <= len(queue)`) and returns it, using only queue operations (`append`, `popleft`) and a list as a stack: move `k` values onto the stack, append them back, then rotate the remaining `len - k` values from the front to the back.
# EXAMPLE: `[1, 2, 3, 4, 5], 3` -> `[3, 2, 1, 4, 5]`
# BIGO: O(N) time, O(K) space for the stack: k values go through the stack, then the other N - k rotate to the back once.
def reverse_first_k(queue, k):
    raise NotImplementedError
# ==== END


# ==== EX 2.4.20 | Binary numbers 1 to n with a queue | Core
# PROMPT: Write `binary_numbers(n)` that returns the binary forms of `1` to `n` as strings, in order, without converting numbers: start a `deque` with `"1"`, and each time you take a string from the front, record it and add it with `"0"` and `"1"` appended to the back.
# EXAMPLE: `5` -> `["1", "10", "11", "100", "101"]`
# BIGO: O(N log N) time and space: N strings of about log N digits each, every one produced by appending a digit to an earlier one.
def binary_numbers(n):
    raise NotImplementedError
# ==== END
