"""Chapter 6.3: Union-find and spanning trees."""
import heapq


# ==== EX 6.3.1 | Union-find | Core | class=DisjointSet
# PROMPT: Build `DisjointSet(n)` over elements `0` to `n - 1` with `find(x)` (the root of x's group, pointing every node on the way straight at the root), `union(a, b)` (merge two groups, hanging the smaller under the larger; `False` if already together), `size(x)` and a `groups` count.
# EXAMPLE: `DisjointSet(5)`: `union(0, 1)` -> `True`; `union(1, 0)` -> `False`; `size(1)` -> `2`; `groups` is `4`
# BIGO: O(alpha(N)) amortized per operation, effectively constant: union by size keeps the trees shallow, and path compression flattens every path that `find` walks.
class DisjointSet:
    def __init__(self, n):
        raise NotImplementedError

    def find(self, x):
        raise NotImplementedError

    def union(self, a, b):
        raise NotImplementedError

    def size(self, x):
        raise NotImplementedError
# ==== END


# ==== EX 6.3.2 | How many groups after the merges? | Core
# PROMPT: People `0` to `n - 1` start alone; each pair in `pairs` joins two people's groups. Write `group_count(n, pairs)` that returns how many groups remain, using your `DisjointSet` (6.3.1).
# EXAMPLE: `5, [[0, 1], [1, 2], [3, 4]]` -> `2`
# BIGO: O(N + M alpha(N)) for M pairs: one union per pair, and the set keeps the count.
def group_count(n, pairs):
    raise NotImplementedError
# ==== END


# ==== EX 6.3.3 | Cycle in an undirected graph | Core
# PROMPT: Write `has_cycle_undirected(n, edges)` for vertices `0` to `n - 1` and undirected `[u, v]` edges (no repeats, no self-loops): `True` when the graph has a cycle. Add edges to a `DisjointSet` one at a time; an edge inside one group closes a cycle.
# EXAMPLE: `4, [[0, 1], [1, 2], [2, 0], [2, 3]]` -> `True`; `4, [[0, 1], [1, 2], [2, 3]]` -> `False`
# BIGO: O(N + E alpha(N)): an edge whose ends are already in one group closes a cycle.
def has_cycle_undirected(n, edges):
    raise NotImplementedError
# ==== END


# ==== EX 6.3.4 | Is the graph a tree? | Core
# PROMPT: Write `is_tree(n, edges)` for `n >= 1` vertices and undirected `[u, v]` edges: `True` when the graph is connected and has no cycle. Check that there are exactly `n - 1` edges and that none of them closes a cycle in a `DisjointSet`.
# EXAMPLE: `4, [[0, 1], [0, 2], [2, 3]]` -> `True`; `4, [[0, 1], [2, 3]]` -> `False`
# BIGO: O(N + E alpha(N)): a tree on N vertices has exactly N - 1 edges and no cycle, and those two facts together also force it to be connected.
def is_tree(n, edges):
    raise NotImplementedError
# ==== END


# ==== EX 6.3.5 | Minimum spanning tree, edge by edge | Practice
# PROMPT: Write `kruskal_cost(n, edges)` for an undirected graph on `0` to `n - 1` with `[u, v, w]` edges: the total weight of a minimum spanning tree, or `-1` when the graph is not connected. Take edges cheapest first, keeping each one that joins two different groups of a `DisjointSet`.
# EXAMPLE: `4, [[0, 1, 4], [1, 2, 2], [0, 2, 5], [2, 3, 1], [1, 3, 7]]` -> `7`
# BIGO: O(E log E) for the sort, then O(E alpha(V)): the cheapest edge between two groups is always safe to take (the cut property).
# NOTE: This is Kruskal's method; 6.3.6 grows the tree from one vertex instead.
def kruskal_cost(n, edges):
    raise NotImplementedError
# ==== END


# ==== EX 6.3.6 | Minimum spanning tree, grown from one vertex | Practice
# PROMPT: Write `prim_cost(n, edges)` with the same input and answer as 6.3.5, but grow one tree from vertex `0`: keep a `heapq` of `(weight, vertex)` for edges leaving the tree, and add the cheapest one whose far end is not yet in the tree.
# EXAMPLE: `4, [[0, 1, 4], [1, 2, 2], [0, 2, 5], [2, 3, 1], [1, 3, 7]]` -> `7`
# BIGO: O(E log E) time, O(V + E) space: the heap always offers the cheapest edge leaving the tree built so far, and stale entries are skipped.
# NOTE: This is Prim's method. It needs no union-find, and on dense graphs an array instead of a heap makes it O(V^2).
def prim_cost(n, edges):
    raise NotImplementedError
# ==== END


# ==== EX 6.3.7 | The one extra edge | Practice
# PROMPT: `edges` connect vertices `0` to `n - 1`, where `n = len(edges)`: a tree plus one extra edge, so there is exactly one cycle. Write `redundant_edge(edges)` that returns the edge you can remove, in order of the list, to leave a tree: the first one that joins two vertices already in one group.
# EXAMPLE: `[[0, 1], [1, 2], [2, 3], [1, 3], [3, 4]]` -> `[1, 3]`
# BIGO: O(N alpha(N)): add edges in order; the first one whose ends are already joined is the extra one.
def redundant_edge(edges):
    raise NotImplementedError
# ==== END


# ==== EX 6.3.8 | When is everyone connected? | Practice
# PROMPT: `logs` holds `[time, a, b]` entries, in any order, each saying people `a` and `b` became friends at `time`; friendship joins groups. Write `earliest_connected(n, logs)` for `n >= 2` people that returns the earliest time everyone is in one group, or `-1`. Sort by time and merge until `groups` reaches one.
# EXAMPLE: `4, [[7, 2, 3], [2, 0, 1], [5, 1, 2], [9, 0, 3]]` -> `7`
# BIGO: O(M log M) for sorting M log entries, then O(M alpha(N)): the group count falls to one at exactly the answer.
def earliest_connected(n, logs):
    raise NotImplementedError
# ==== END
