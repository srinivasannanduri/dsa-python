"""Chapter 6.2: Shortest paths and ordering."""
import heapq
import math
from collections import deque


# ==== EX 6.2.1 | Shortest path, unweighted | Core
# PROMPT: Write `shortest_path(graph, start, end)` on a dict graph using BFS and a `previous` map, returning the list of vertices or `None`.
# EXAMPLE: `{'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}`, A to E -> `['A', 'B', 'D', 'E']`
# BIGO: O(V + E). The first time BFS reaches a vertex is along a fewest-edges path.
def shortest_path(graph, start, end):
    raise NotImplementedError
# ==== END


# ==== EX 6.2.2 | Fastest route by travel time | Core
# PROMPT: Write `dijkstra(routes, start, end)` for `routes = {town: {neighbour: minutes}}`. Return `(total_cost, path)` or `(None, [])`. Use `heapq` to always visit the nearest known unvisited town next.
# EXAMPLE: `routes = {'Ames': {'Bern': 4, 'Cork': 2}, 'Bern': {'Dover': 5}, 'Cork': {'Bern': 1, 'Dover': 8, 'Eden': 10}, 'Dover': {'Eden': 2}}` -> Ames to Eden is `(10, ['Ames', 'Cork', 'Bern', 'Dover', 'Eden'])`
# BIGO: O((V + E) log V) with a heap. Scanning an array for the cheapest unvisited city instead is O(V^2).
# NOTE: Dijkstra requires non-negative weights.
def dijkstra(routes, start, end):
    raise NotImplementedError
# ==== END


# ==== EX 6.2.3 | Topological order of tasks | Stretch
# PROMPT: Write `topological_order(deps)` for a directed graph `{task: [tasks that depend on it]}` using Kahn's algorithm (repeatedly take tasks with no remaining prerequisites). Return `None` if there is a cycle.
# EXAMPLE: `{'wake': ['shower', 'coffee'], 'shower': ['dress'], 'coffee': ['dress'], 'dress': []}` -> `['wake', 'shower', 'coffee', 'dress']`
# BIGO: O(V + E).
def topological_order(deps):
    raise NotImplementedError
# ==== END


# ==== EX 6.2.4 | Shortest paths with negative weights | Practice
# PROMPT: Vertices are `0` to `n - 1`, and `edges` holds directed `[u, v, w]` with any integer weight. Write `bellman_ford(n, edges, source)` that returns the list of shortest distances from `source` (`float("inf")` when unreachable), or `None` when a negative cycle can be reached. Relax every edge `n - 1` times, then check once more.
# EXAMPLE: `4, [[0, 1, 4], [0, 2, 1], [2, 1, -2], [1, 3, 1]], 0` -> `[0, -1, 1, 0]`
# BIGO: O(V * E) time, O(V) space: a shortest path uses at most V - 1 edges, so V - 1 rounds of relaxing every edge settle it, and any improvement after that means a negative cycle.
# NOTE: This is the Bellman-Ford method. Dijkstra (6.2.2) is faster but wrong once a weight is negative, because a settled vertex can still get cheaper.
def bellman_ford(n, edges, source):
    raise NotImplementedError
# ==== END


# ==== EX 6.2.5 | A profitable loop of exchanges | Stretch
# PROMPT: `rates[i][j]` is how many units of currency `j` one unit of `i` buys. Write `has_profitable_loop(rates)`: `True` when some cycle of exchanges ends with more than it started. Give edge `i -> j` the weight `-math.log(rates[i][j])` and look for a negative cycle: start every distance at `0`, relax all edges `n - 1` times, then check once more (allow `1e-12` for rounding).
# EXAMPLE: `[[1, 0.9, 0.8], [1.2, 1, 0.7], [1.3, 1.4, 1]]` -> `True` (0 -> 1 -> 0 turns 1 into 1.08)
# BIGO: O(N^3) time for N currencies, O(N) space: logarithms turn a product above 1 into a sum below 0, so a profitable loop is a negative cycle.
def has_profitable_loop(rates):
    raise NotImplementedError
# ==== END


# ==== EX 6.2.6 | A* search on a grid | Stretch
# PROMPT: `grid` is a list of strings, `.` open and `#` wall; a step moves to one of the 4 neighbouring open cells. Write `grid_path_length(grid, start, goal)` (cells as `(row, col)` tuples) that returns the fewest steps, or `-1`, using A*: a `heapq` ordered by steps so far plus the Manhattan distance to `goal`, and a table of the best known steps per cell.
# EXAMPLE: `["....#", ".##.#", "....."], (0, 0), (2, 4)` -> `6`
# BIGO: O(R*C log(R*C)) worst case, usually much less: the Manhattan distance never overestimates, so the first time the goal leaves the queue its cost is optimal, and the estimate steers the search toward it.
def grid_path_length(grid, start, goal):
    raise NotImplementedError
# ==== END
