from ch6_1_graphs import add_edge, bfs_traverse, count_components, dfs_search, dfs_traverse, Vertex


def make_towns():
    ames, bern, cork, dover = (Vertex(n) for n in ('Ames', 'Bern', 'Cork', 'Dover'))
    ames.add_adjacent(bern)
    ames.add_adjacent(cork)
    bern.add_adjacent(dover)
    return ames, bern, cork, dover


def test_ex_6_1_1():
    g = {}
    add_edge(g, 'Ames', 'Bern')
    assert g == {'Ames': ['Bern'], 'Bern': ['Ames']}
    add_edge(g, 'Ames', 'Bern')
    add_edge(g, 'Bern', 'Cork', directed=True)
    assert g == {'Ames': ['Bern'], 'Bern': ['Ames', 'Cork'], 'Cork': []}


def test_ex_6_1_2():
    ames, bern, cork, dover = make_towns()
    assert ames in bern.adjacent and bern in ames.adjacent and dover in bern.adjacent
    ames.add_adjacent(bern)
    assert ames.adjacent.count(bern) == 1


def test_ex_6_1_3():
    ames, *_ = make_towns()
    assert dfs_traverse(ames) == ['Ames', 'Bern', 'Dover', 'Cork']


def test_ex_6_1_4():
    ames, bern, cork, dover = make_towns()
    assert dfs_search(ames, 'Dover') is dover and dfs_search(ames, 'Zed') is None


def test_ex_6_1_5():
    ames, *_ = make_towns()
    assert bfs_traverse(ames) == ['Ames', 'Bern', 'Cork', 'Dover']


def test_ex_6_1_6():
    assert count_components({'a': ['b'], 'b': ['a'], 'c': [], 'd': ['e'], 'e': ['d']}) == 3
