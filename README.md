# Lowest common ancestor

## About this project

Fun playground that is to be used to test out various scenarios in python.

## Installing dependencies

You are given two nodes in a symmetrical binary tree.
The tree is numbered incrementally from left to right.
Each node can only have one parent and two children.
Without creating a tree structure in memory
try to find the lowest common ancestor.
https://en.wikipedia.org/wiki/Lowest_common_ancestor.
Nodes start from 1.

Examples:
6, 5 -> lowest common ancestor: 1
18, 5 -> lowest common ancestor: 2
Conditions
1 >= node1 <= 1000000
1 >= node2 <= 1000000
the program takes 2 ints as an input and returns 1 int

```sh
# install python version
pyenv install 3.8.0
# set/activate local python version
pyenv local 3.8.0
# install poetry
pip install poetry
# install poetry settings using pyproject.toml file
poetry install
```

## Format checks

make lint - execute flake8

make black - run black and format files

## Testing

```sh
make unit-test
```

## Running

```sh
make all
```

After completing project installation, you can also run it with:

```sh
poetry run execute <node1 id> <node2 id>
```

For help use:

```sh
poetry run execute --help
```
