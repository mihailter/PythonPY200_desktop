from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """
    def __init__(self, value: Any, next_: Optional["Node"] = None):

        self.value = value
        self.next = next_

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def get_value(self) -> Any:
        return self.value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self._next = next_

    def __repr__(self) -> str:

    def __str__(self) -> str:

class DoubleLinkedNode(Node):

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev = None):
        super().__init__(value, next_) # вызвать конструктор базового класса
        self.prev = prev




if __name__ == "__main__":
    ...
