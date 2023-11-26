"""Main module."""
from collections import namedtuple, deque
from typing import Tuple


def generate_a_tuple() -> Tuple[int, str, float]:
    return 1, "a", 3.14


def print_a_named_tuple() -> None:
    abc_tuple = namedtuple("MyTuple", ["a", "b", "c"])(1, "a", 3.14)
    print(f"named tuple is : {abc_tuple.a}, {abc_tuple.b}, {abc_tuple.c}")


def compare_stack_and_queue() -> None:
    stack = deque()
    queue = deque()

    stack.append("a")
    stack.append("b")
    stack.append("c")

    queue.append("a")
    queue.append("b")
    queue.append("c")

    stack.append("d")
    stack.pop()

    queue.append("d")
    queue.popleft()

    print(f"stack is {stack}")
    print(f"queue is {queue}")
