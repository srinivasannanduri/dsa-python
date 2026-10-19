"""Chapter 6.1: Graphs: representation and traversal."""
from collections import deque


# ==== EX 6.1.1 | Adjacency-list graph with a hash map | Core
# PROMPT: Write `add_edge(graph, a, b, directed=False)` for a graph stored as `{vertex: [neighbours]}`. Add missing vertices automatically and avoid duplicate edges.
# EXAMPLE: `g = {}; add_edge(g, 'Ames', 'Bern')` -> `{'Ames': ['Bern'], 'Bern': ['Ames']}`
# BIGO: O(D) for the duplicate check, where D is the vertex's degree. A set of neighbours would make it O(1).
def add_edge(graph, a, b, directed=False):
    raise NotImplementedError
# ==== END


# ==== EX 6.1.2 | Vertex objects with adjacency lists | Core | class=Vertex
# PROMPT: Create `Vertex(value)` with an `adjacent` list and `add_adjacent(vertex)` that links both ways (friendship is mutual) without recursing forever.
# EXAMPLE: `ames.add_adjacent(bern)` -> bern is in ames.adjacent and ames is in bern.adjacent
# BIGO: O(D) per link because of the membership check.
class Vertex:
    def __init__(self, value):
        raise NotImplementedError

    def add_adjacent(self, vertex):
        raise NotImplementedError
# ==== END


# ==== EX 6.1.3 | Depth-first traversal | Core
# PROMPT: Write `dfs_traverse(vertex, visited=None)` returning vertex values in visit order. Mark each vertex visited before recursing into its neighbours.
# EXAMPLE: Ames-Bern, Ames-Cork, Bern-Dover -> `['Ames', 'Bern', 'Dover', 'Cork']`
# BIGO: O(V + E). Without the visited set, a cycle would loop forever.
def dfs_traverse(vertex, visited=None):
    raise NotImplementedError
# ==== END


# ==== EX 6.1.4 | Depth-first search | Core
# PROMPT: Write `dfs_search(vertex, target_value, visited=None)` returning the matching `Vertex` or `None`.
# EXAMPLE: From Ames, search 'Dover' -> the Dover vertex
# BIGO: O(V + E) worst case.
def dfs_search(vertex, target_value, visited=None):
    raise NotImplementedError
# ==== END


# ==== EX 6.1.5 | Breadth-first traversal | Core
# PROMPT: Write `bfs_traverse(start)` using a queue: mark the start visited, then repeatedly dequeue a vertex and enqueue its unvisited neighbours.
# EXAMPLE: Same graph as 6.1.3 -> `['Ames', 'Bern', 'Cork', 'Dover']`
# BIGO: O(V + E).
# NOTE: BFS spreads out in rings, so it finds close vertices first; DFS dives deep first.
def bfs_traverse(start):
    raise NotImplementedError
# ==== END


# ==== EX 6.1.6 | Count connected groups | Practice
# PROMPT: Write `count_components(graph)` returning how many separate groups an undirected dict graph has.
# EXAMPLE: `{'a': ['b'], 'b': ['a'], 'c': [], 'd': ['e'], 'e': ['d']}` -> `3`
# BIGO: O(V + E): each vertex is explored once across all searches.
def count_components(graph):
    raise NotImplementedError
# ==== END


