import argparse
from typing import Any, Generator, List, Tuple

MIN_VALUE = 1
MAX_VALUE = 1000000
DIVISOR = 2


def find_all_ancestors(node1: int, node2: int) -> Tuple[List[int], List[int]]:
    return list(ancestors(node1)), list(ancestors(node2))


def ancestors(node: int) -> Generator[int, None, None]:
    while node >= MIN_VALUE:
        node //= DIVISOR
        yield node


def find_lowest_common_ancestor(ancestors1: List[int], ancestors2: List[int]) -> int:
    # merge both lists
    merger: List[List[int]] = [ancestors1, ancestors2]
    # find common elements in both lists
    common = list(set.intersection(*map(set, merger)))  # type: ignore
    # sort the list in descending order to find the ancestor
    common.sort(reverse=True)
    # return the top element as the lowest common ancestor
    return int(common[0]) if len(common) else MIN_VALUE  # type: ignore


def input_value(input_value: str) -> int:
    result = int(input_value)
    if result not in range(MIN_VALUE, MAX_VALUE):
        raise argparse.ArgumentTypeError(
            f"input must be a valid integer between {MIN_VALUE} and {MAX_VALUE}, instead got {input_value}"
        )
    return result


def user_input() -> Any:
    parser = argparse.ArgumentParser(description="Find the lowest common ancestor for two binary tree nodes")
    parser.add_argument(
        "integers",
        metavar="node id",
        type=input_value,
        nargs=2,
        help=f"two integer node ids; value {MIN_VALUE} >= N <={MAX_VALUE}",
    )

    args = parser.parse_args()
    return args.integers


def execute() -> None:
    nodes = user_input()
    ancestors1, ancestors2 = find_all_ancestors(nodes[0], nodes[1])
    print(find_lowest_common_ancestor(ancestors1, ancestors2))
