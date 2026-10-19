from ch3_3_linear_sorts import bucket_sort, counting_sort, radix_sort, sort_by_order


def test_ex_3_3_1():
    assert counting_sort([3, 0, 2, 3, 1], 3) == [0, 1, 2, 3, 3] and counting_sort([], 5) == []
    assert counting_sort([4, 4, 4], 4) == [4, 4, 4] and counting_sort([9, 0, 5, 0], 9) == [0, 0, 5, 9]


def test_ex_3_3_2():
    assert sort_by_order([2, 0, 1, 2, 0], [2, 0, 1]) == [2, 2, 0, 0, 1] and sort_by_order([], [1, 2]) == []
    assert sort_by_order([5, 5, 7], [7, 5, 9]) == [7, 5, 5] and sort_by_order([3, 1, 3], [1, 3]) == [1, 3, 3]


def test_ex_3_3_3():
    assert radix_sort([329, 57, 640, 4, 1000, 72]) == [4, 57, 72, 329, 640, 1000] and radix_sort([]) == []
    assert radix_sort([0, 0, 1]) == [0, 0, 1] and radix_sort([21, 12, 11, 22]) == [11, 12, 21, 22]


def test_ex_3_3_4():
    assert bucket_sort([0.42, 0.07, 0.93, 0.5, 0.31]) == [0.07, 0.31, 0.42, 0.5, 0.93] and bucket_sort([]) == []
    assert bucket_sort([0.25, 0.2, 0.21, 0.0]) == [0.0, 0.2, 0.21, 0.25] and bucket_sort([0.99]) == [0.99]
