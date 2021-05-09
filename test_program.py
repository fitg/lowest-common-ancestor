import pytest

from program import find_all_ancestors, find_lowest_common_ancestor


@pytest.mark.unittest
def test_find_all_ancestors_simple() -> None:
    expected1 = [5, 2, 1, 0]
    expected2 = [12, 6, 3, 1, 0]
    ancestors1, ancestors2 = find_all_ancestors(10, 25)
    assert ancestors1 == expected1
    assert ancestors2 == expected2


@pytest.mark.unittest
def test_find_all_ancestors_far() -> None:
    expected1 = [11, 5, 2, 1, 0]
    expected2 = [233777, 116888, 58444, 29222, 14611, 7305, 3652, 1826, 913, 456, 228, 114, 57, 28, 14, 7, 3, 1, 0]
    ancestors1, ancestors2 = find_all_ancestors(22, 467555)
    assert ancestors1 == expected1
    assert ancestors2 == expected2


@pytest.mark.unittest
def test_find_all_ancestors_both_long() -> None:
    expected1 = [106156, 53078, 26539, 13269, 6634, 3317, 1658, 829, 414, 207, 103, 51, 25, 12, 6, 3, 1, 0]
    expected2 = [106115, 53057, 26528, 13264, 6632, 3316, 1658, 829, 414, 207, 103, 51, 25, 12, 6, 3, 1, 0]
    ancestors1, ancestors2 = find_all_ancestors(212312, 212231)
    assert ancestors1 == expected1
    assert ancestors2 == expected2


@pytest.mark.unittest
def test_find_lowest_common_ancestor_simple() -> None:
    expected = 1
    actual = find_lowest_common_ancestor(
        [11, 5, 2, 1, 0], [233777, 116888, 58444, 29222, 14611, 7305, 3652, 1826, 913, 456, 228, 114, 57, 28, 14, 7, 3, 1, 0]
    )
    assert actual == expected


@pytest.mark.unittest
def test_find_lowest_common_ancestor_complicated() -> None:
    expected = 1658
    actual = find_lowest_common_ancestor(
        [106156, 53078, 26539, 13269, 6634, 3317, 1658, 829, 414, 207, 103, 51, 25, 12, 6, 3, 1, 0],
        [106115, 53057, 26528, 13264, 6632, 3316, 1658, 829, 414, 207, 103, 51, 25, 12, 6, 3, 1, 0],
    )
    assert actual == expected
