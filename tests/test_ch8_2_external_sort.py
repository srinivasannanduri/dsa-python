import random
from ch8_2_external_sort import (external_sort_ios, k_way_merge, make_runs, multiway_sort, passes_multiway,
                                passes_two_way, sort_file, two_way_sort)


def shuffled(n, seed):
    data = list(range(n))
    random.Random(seed).shuffle(data)
    return data


def test_ex_8_2_1():
    assert make_runs([5, 1, 9, 3, 7, 2, 8], 3) == [[1, 5, 9], [2, 3, 7], [8]] and make_runs([], 3) == []


def test_ex_8_2_2():
    assert two_way_sort(list(range(16, 0, -1)), 2) == (list(range(1, 17)), 4)
    data = shuffled(10000, 1)
    srt, passes = two_way_sort(data, 100)
    assert srt == sorted(data) and passes == 8


def test_ex_8_2_3():
    assert k_way_merge([[1, 4, 9], [2, 3], [0, 10]]) == [0, 1, 2, 3, 4, 9, 10] and k_way_merge([]) == []


def test_ex_8_2_4():
    data = shuffled(10000, 1)
    srt, passes = multiway_sort(data, 100, 10)
    assert srt == sorted(data) and passes == 4


def test_ex_8_2_5():
    assert passes_multiway(10**4, 100, 10) == 4 and passes_two_way(10**4, 100) == 8


def test_ex_8_2_6():
    assert external_sort_ios(10**4, 100, 10) == 8000


def test_ex_8_2_7(tmp_path):
    src, dst = tmp_path / "in.txt", tmp_path / "out.txt"
    src.write_text("\n".join(map(str, shuffled(1000, 2))) + "\n")
    assert sort_file(src, dst, 100) == 10
    assert [int(x) for x in dst.read_text().split()] == list(range(1000))
