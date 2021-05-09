import pytest

from program import find_all_ancestors, find_lowest_common_ancestor


@pytest.mark.unittest
def test_find_all_ancestors_simple() -> None:
    expected = [[5, 2, 1, 0], [12, 6, 3, 1, 0]]
    ancestors = find_all_ancestors([10, 25])
    assert ancestors == expected


@pytest.mark.unittest
def test_find_all_ancestors_far() -> None:
    expected = [
        [11, 5, 2, 1, 0],
        [233777, 116888, 58444, 29222, 14611, 7305, 3652, 1826, 913, 456, 228, 114, 57, 28, 14, 7, 3, 1, 0],
    ]
    ancestors = find_all_ancestors([22, 467555])
    assert ancestors == expected


@pytest.mark.unittest
def test_find_all_ancestors_both_long() -> None:
    expected = [
        [106156, 53078, 26539, 13269, 6634, 3317, 1658, 829, 414, 207, 103, 51, 25, 12, 6, 3, 1, 0],
        [106115, 53057, 26528, 13264, 6632, 3316, 1658, 829, 414, 207, 103, 51, 25, 12, 6, 3, 1, 0],
    ]
    ancestors = find_all_ancestors([212312, 212231])
    assert ancestors == expected


@pytest.mark.unittest
def test_find_all_ancestors_both_border_condition() -> None:
    expected = [[0], [1, 0]]
    ancestors = find_all_ancestors([1, 2])
    assert ancestors == expected


@pytest.mark.unittest
def test_find_all_ancestors_both_border_condition2() -> None:
    expected = [[0], [0]]
    ancestors = find_all_ancestors([1, 1])
    assert ancestors == expected


@pytest.mark.unittest
def test_find_lowest_common_ancestor_simple() -> None:
    expected = 1
    actual = find_lowest_common_ancestor(
        [
            [11, 5, 2, 1, 0],
            [233777, 116888, 58444, 29222, 14611, 7305, 3652, 1826, 913, 456, 228, 114, 57, 28, 14, 7, 3, 1, 0],
        ]
    )
    assert actual == expected


@pytest.mark.unittest
def test_find_lowest_common_ancestor_complicated() -> None:
    expected = 1658
    actual = find_lowest_common_ancestor(
        [
            [106156, 53078, 26539, 13269, 6634, 3317, 1658, 829, 414, 207, 103, 51, 25, 12, 6, 3, 1, 0],
            [106115, 53057, 26528, 13264, 6632, 3316, 1658, 829, 414, 207, 103, 51, 25, 12, 6, 3, 1, 0],
        ]
    )
    assert actual == expected


@pytest.mark.unittest
def test_find_lowest_common_ancestor_border_condition() -> None:
    expected = 0
    actual = find_lowest_common_ancestor(
        [
            [0],
            [0],
        ]
    )
    assert actual == expected
