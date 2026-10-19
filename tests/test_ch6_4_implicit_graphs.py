from ch6_4_implicit_graphs import (clone_graph, count_islands, GraphNode, has_cycle_directed, knight_distance,
                                  ladder_length, largest_island, longest_rising_path, rounds_to_spread,
                                  two_colourable)


def test_ex_6_4_1():
    assert count_islands(["##..#", "#...#", "..#..", "....#"]) == 4 and count_islands([]) == 0 and count_islands(["..."]) == 0
    assert count_islands(["###", "#.#", "###"]) == 1 and count_islands(["#.#", ".#.", "#.#"]) == 5


def test_ex_6_4_2():
    assert two_colourable(4, [[0, 1], [1, 2], [2, 3], [3, 0]]) and not two_colourable(3, [[0, 1], [1, 2], [2, 0]])
    assert two_colourable(5, []) and not two_colourable(6, [[0, 1], [3, 4], [4, 5], [5, 3]]) and two_colourable(4, [[0, 1], [2, 3]])


def test_ex_6_4_3():
    ring = [GraphNode(v) for v in (1, 2, 3, 4)]
    for i, node in enumerate(ring):
        node.neighbours = [ring[(i + 1) % 4], ring[(i - 1) % 4]]
    copy = clone_graph(ring[0])
    seen, stack = {copy}, [copy]
    while stack:
        node = stack.pop()
        assert node not in ring
        for other in node.neighbours:
            if other not in seen:
                seen.add(other)
                stack.append(other)
    assert sorted(n.value for n in seen) == [1, 2, 3, 4] and [n.value for n in copy.neighbours] == [2, 4]
    assert copy.neighbours[0].neighbours[0].neighbours[0].value == 4 and copy.neighbours[0].neighbours[1] is copy
    assert clone_graph(None) is None
    alone = GraphNode(7)
    alone.neighbours = [alone]
    twin = clone_graph(alone)
    assert twin is not alone and twin.neighbours == [twin]


def test_ex_6_4_4():
    assert largest_island(["##..#", "#...#", "..#..", "....#"]) == 3 and largest_island([]) == 0 and largest_island(["..."]) == 0
    assert largest_island(["###", "#.#", "###"]) == 8 and largest_island(["#.#", ".#.", "#.#"]) == 1 and largest_island(["##.", "...", "###"]) == 3


def test_ex_6_4_5():
    assert rounds_to_spread(["S..#", ".#..", "...S"]) == 2 and rounds_to_spread(["S#."]) == -1 and rounds_to_spread(["S#"]) == 0
    assert rounds_to_spread(["..."]) == -1 and rounds_to_spread(["S...."]) == 4 and rounds_to_spread(["S..", "#..", "..S"]) == 2


def test_ex_6_4_6():
    assert has_cycle_directed(4, [[0, 1], [1, 2], [2, 0], [2, 3]]) and not has_cycle_directed(3, [[0, 1], [0, 2], [1, 2]])
    assert not has_cycle_directed(3, []) and has_cycle_directed(2, [[1, 1]]) and has_cycle_directed(5, [[0, 1], [3, 4], [4, 2], [2, 3]])
    assert not has_cycle_directed(4, [[0, 1], [2, 1], [3, 2], [3, 0]])


def test_ex_6_4_7():
    words = ["cord", "card", "ward", "warm", "word", "worm"]
    assert ladder_length("cold", "warm", words) == 5 and ladder_length("cold", "cord", words) == 2 and ladder_length("cold", "warn", words) == 0
    assert ladder_length("ab", "cd", ["ad", "cd"]) == 3 and ladder_length("ab", "cd", ["xy", "cd"]) == 0


def test_ex_6_4_8():
    assert knight_distance(8, (0, 0), (7, 7)) == 6 and knight_distance(8, (0, 0), (1, 2)) == 1 and knight_distance(8, (3, 3), (3, 3)) == 0
    assert knight_distance(3, (0, 0), (1, 1)) == -1 and knight_distance(8, (0, 0), (1, 1)) == 4 and knight_distance(1, (0, 0), (0, 0)) == 0


def test_ex_6_4_9():
    assert longest_rising_path([[1, 2, 9], [5, 3, 8], [4, 6, 7]]) == 7 and longest_rising_path([[7]]) == 1 and longest_rising_path([[1, 1], [1, 1]]) == 1
    assert longest_rising_path([[1, 2, 3, 4]]) == 4 and longest_rising_path([[5, 4], [2, 3]]) == 4
