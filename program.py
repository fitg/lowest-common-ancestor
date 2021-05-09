import argparse
import functools
from typing import cast, Generator, List

MIN_VALUE = 1
MAX_VALUE = 1000000
DIVISOR = 2


def find_all_ancestors(nodes: List[int]) -> List[List[int]]:
    return [list(ancestors(node)) for node in nodes]


def ancestors(node: int) -> Generator[int, None, None]:
    while node >= MIN_VALUE:
        node //= DIVISOR
        yield node


def find_lowest_common_ancestor(ancestor_groups: List[List[int]]) -> int:
    groups = iter(ancestor_groups)
    first_group = next(groups)
    intersection = functools.reduce(set.intersection, groups, set(first_group))
    return max(intersection, default=MIN_VALUE)


def input_value(input_value: str) -> int:
    try:
        result = int(input_value)
        if result not in range(MIN_VALUE, MAX_VALUE):
            raise ValueError
    except ValueError:
        raise argparse.ArgumentTypeError(
            f"input must be a valid integer between {MIN_VALUE} and {MAX_VALUE}, instead got {input_value}"
        )
    return result


def user_input() -> List[int]:
    parser = argparse.ArgumentParser(description="Find the lowest common ancestor for two binary tree nodes")
    parser.add_argument(
        "integers",
        metavar="node id",
        type=input_value,
        nargs=2,
        help=f"two integer node ids; value {MIN_VALUE} >= N <={MAX_VALUE}",
    )

    args = parser.parse_args()
    return cast(List[int],args.integers)


def execute() -> None:
    print(find_lowest_common_ancestor(find_all_ancestors(user_input())))
