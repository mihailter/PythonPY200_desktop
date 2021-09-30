from collections.abc import MutableSequence

from  typing import Optional, Any
from  node import Node


class LinkedList(MutableSequence):
    def __init__(self, value: Any, next_: Optional["LinkedList"] = None):
        self.len = 0
        self.head: Optional[Node] = None


class DoubleLinkedList(LinkedList):
    ...


if __name__ == "__main__":
    ll = LinkedList([1])
