from typing import Any, Optional

class Node:
    """Класс, который описывает узел связного списка"""
    def __init__(self, value: Any, next_: Optional["Node"] = None):

        self.value = value # Любое значение, которое помещено в узел
        self.__next = next_ # следующий узел, если он есть

    def is_valid(self, node: Any) -> None: # метод проверки корректности связываемого узла
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def get_value(self) -> Any:
        return self.value

    @property # определением geteer
    def next(self):
        return self.__next

    @next.setter # определение setter
    def next(self, next_: Optional["Node"]):
        self.is_valid(next_)
        self.__next = next_

    def __repr__(self) -> str: # определение метода __repr__
        return f"Node({self.value}, {self.next})"

    def __str__(self) -> str: # определение метода __str__
        return str(self.value)

class DoubleLinkedNode(Node): # в () наследуем от класса Node

    def __init__(self, value: Any, next_: Optional["Node"] = None, prev = None):
        super().__init__(value, next_) # вызвать конструктор базового класса
        self.prev = prev # определяем дополнительный атрибут

    @property  # определением geteer
    def prev(self):
        return self._prev

    @prev.setter  # определение setter
    def prev(self, prev: Optional["Node"]):
        self.is_valid(prev)
        self._prev = prev

    #  наследование, инкапсуляция, полиморфизм
    #  protected метод с _ подчеркиванием
    #  private метод с __ подчеркиваниями
    def __repr__(self) -> str:
        next_prev = None if self.prev is None else f"DoubleLinkedNode({self._prev})"
        next_repr = None if self.next is None else f"DoubleLinkedNode({self.next})"

        return f"DoubleLinkedNode({self.value}, {next_prev}, {next_repr})"
        #return f"DoubleLinkedNode({self.value}, {None})" if self.next is None else f"DoubleLinkedNode({self.value}, DoubleLinkedNode({self.next}))"

if __name__ == "__main__":

        first_node = DoubleLinkedNode("1", None)
        second_node = DoubleLinkedNode("2", None)
        last_node = DoubleLinkedNode('3', first_node, second_node)

        print(repr(last_node))
