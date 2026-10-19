from ch6_2_paths_order import (bellman_ford, dijkstra, grid_path_length, has_profitable_loop, shortest_path,
                              topological_order)


def test_ex_6_2_1():
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}
    assert shortest_path(graph, 'A', 'E') == ['A', 'B', 'D', 'E'] and shortest_path(graph, 'A', 'Z') is None


def test_ex_6_2_2():
    routes = {'Ames': {'Bern': 4, 'Cork': 2}, 'Bern': {'Dover': 5}, 'Cork': {'Bern': 1, 'Dover': 8, 'Eden': 10},
              'Dover': {'Eden': 2}, 'Eden': {}}
    assert dijkstra(routes, 'Ames', 'Eden') == (10, ['Ames', 'Cork', 'Bern', 'Dover', 'Eden'])
    assert dijkstra(routes, 'Ames', 'Ames') == (0, ['Ames'])
    assert dijkstra(routes, 'Ames', 'Dover') == (8, ['Ames', 'Cork', 'Bern', 'Dover'])
    assert dijkstra(routes, 'Eden', 'Ames') == (None, [])


def test_ex_6_2_3():
    deps = {'wake': ['shower', 'coffee'], 'shower': ['dress'], 'coffee': ['dress'], 'dress': []}
    assert topological_order(deps) == ['wake', 'shower', 'coffee', 'dress']
    assert topological_order({'a': ['b'], 'b': ['a']}) is None


def test_ex_6_2_4():
    assert bellman_ford(4, [[0, 1, 4], [0, 2, 1], [2, 1, -2], [1, 3, 1]], 0) == [0, -1, 1, 0]
    assert bellman_ford(3, [[0, 1, 5]], 0) == [0, 5, float("inf")] and bellman_ford(1, [], 0) == [0]
    assert bellman_ford(3, [[0, 1, 1], [1, 2, -1], [2, 1, -1]], 0) is None
    assert bellman_ford(3, [[1, 2, -1], [2, 1, -1]], 0) == [0, float("inf"), float("inf")]


def test_ex_6_2_5():
    assert has_profitable_loop([[1, 0.9, 0.8], [1.2, 1, 0.7], [1.3, 1.4, 1]]) and not has_profitable_loop([[1, 0.5], [1.9, 1]])
    assert not has_profitable_loop([[1, 2], [0.5, 1]]) and not has_profitable_loop([[1]])
    assert has_profitable_loop([[1, 2, 0.1], [0.4, 1, 3], [0.2, 0.1, 1]])


def test_ex_6_2_6():
    grid = ["....#", ".##.#", "....."]
    assert grid_path_length(grid, (0, 0), (2, 4)) == 6 and grid_path_length(grid, (0, 0), (0, 0)) == 0 and grid_path_length(grid, (0, 3), (2, 4)) == 3
    assert grid_path_length([".#.", ".#.", "..."], (0, 0), (0, 2)) == 6 and grid_path_length([".#", "#."], (0, 0), (1, 1)) == -1
