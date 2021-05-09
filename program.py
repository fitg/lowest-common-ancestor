import argparse
import math
from typing import Any, List, Tuple

MIN_VALUE = 1
MAX_VALUE = 1000000
DIVISOR = 2


def find_all_ancestors(node1: int, node2: int) -> Tuple[List[int], List[int]]:

    x: int = node1
    y: int = node2
    ancestors_node1: List[int] = []
    ancestors_node2: List[int] = []

    while x >= MIN_VALUE:
        x = math.floor(x / DIVISOR)
        ancestors_node1.append(x)

    while y >= MIN_VALUE:
        y = math.floor(y / DIVISOR)
        ancestors_node2.append(y)

    return ancestors_node1, ancestors_node2


def find_lowest_common_ancestor(ancestors1: List[int], ancestors2: List[int]) -> int:
    # merge both lists
    merger: List[List[int]] = [ancestors1, ancestors2]
    # find common elements in both lists
    common = list(set.intersection(*map(set, merger)))  # type: ignore
    # cleanup and sort the list
    common.remove(0)  # type: ignore
    common.sort(reverse=True)
    # return the top element as the lowest common ancestor
    return int(common[0]) if len(common) else 1  # type: ignore


def input(input_value: str) -> str:
    if int(input_value) not in range(MIN_VALUE, MAX_VALUE):
        raise ValueError
    return input_value


def user_input() -> Any:
    parser = argparse.ArgumentParser(description="Find the lowest common ancestor for two binary tree nodes")
    parser.add_argument(
        "integers", metavar="node id", type=input, nargs=2, help=f"two integer node ids; value {MIN_VALUE} >= N <={MAX_VALUE}"
    )

    args = parser.parse_args()
    return args.integers


def execute() -> None:
    nodes = user_input()
    ancestors1, ancestors2 = find_all_ancestors(int(nodes[0]), int(nodes[1]))
    print(find_lowest_common_ancestor(ancestors1, ancestors2))
