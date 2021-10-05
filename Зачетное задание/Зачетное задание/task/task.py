from collections.abc import MutableSequence

from  typing import Optional, Any, Iterator
from  node import Node
# collections.abc- Абстрактные базовые классы для контейнеров
# MutableSequence абстрактный класс для реализации __getitem__,
# __setitem__, __delitem__, __len__, insert

class LinkedList(MutableSequence):
    def __init__(self, data = None):
        """Конструктор связного списка"""
        self.len = 0 #создаем список
        self.head: Optional[Node] = None # голова 0
        self.tail = self.head # хвост равен голове

        if data is not None:
            for value in data:
                self.append(value)

    # Ревлизация функции append
    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node # перемещаем хвост

        self.len += 1 # добавляем в хвост

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    # реализация функции __getitem__
    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    # реализация функции __setitem__
    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    # реализация функции __delitem__, удаление элемента
    def __delitem__(self, index: int):
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        if index == 0:
            self.head = self.head.next
        elif index == self.len - 1:
            tail = self.step_by_step_on_nodes(index-1)
            tail.next = None
        else:
            prev_node = self.step_by_step_on_nodes(index-1)
            del_node = prev_node.next
            next_node = del_node.next

            self.linked_nodes(prev_node, next_node)

        self.len -= 1

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    def nodes_iterator(self) -> Iterator[Node]:
        current_node = self.head
        for _ in range(self.len):
            yield current_node
            current_node = current_node.next

   # реализация метода __insert__
    def insert(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError()

        insert_node = Node(value)

        if index == 0:
            insert_node.next = self.head
            self.head = insert_node
            self.len += 1
        elif index >= self.len - 1:
            self.append(value)
        else:
            prev_node = self.step_by_step_on_nodes(index - 1)
            next_node = prev_node.next

            self.linked_nodes(prev_node, insert_node)
            self.linked_nodes(insert_node, next_node)

            self.len += 1

    def count(self, data):
        start = self.head
        count1 = 0
        while start:
            if start.getData() == data:
                count1 += 1
            start = start.getNextNode()
        return count1

if __name__ == "__main__":
  #  list_ = [1, 2, 3]

  #  ll = LinkedList(list_)
  #  print(ll.head)
   # print(ll.tail)


#class DoubleLinkedList(LinkedList):
#    def __init__(self, data = None):
      #  super().__init__(data)  # вызвать конструктор базового класса

# count метод возвращает количество элементов с указанным значением.
# list.count(value)
# fruits = ["apple", "banana", "cherry"]
# x = fruits.count("banana")
# print(x)

#class LinkedList:
    # метод возвращает количество полученных элементов
 #   def __init__(self):
#        self.head = None
