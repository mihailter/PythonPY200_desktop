from collections.abc import MutableSequence

from  typing import Optional, Any
from  node import Node
# collections.abc- Абстрактные базовые классы для контейнеров
# MutableSequence абстрактный класс для реализации __getitem__,
# __setitem__, __delitem__, __len__, insert

class LinkedList(MutableSequence):
    # Создаем конструктор связанного списка
    def __init__(self, value: MutableSequence = None):
        self.len = 0
        self.head: Optional[Node] = None # Голова первый элемент
        self.tail: Optional[Node] = None # Хвост последний элемент

        self.list_nodes = []
        if value is not None:
            self.init_linked_list(value)

    # Создаем метод, который создает вспомогательный список
    # и связывает в нем узлы
    def init_linked_list(self, value: MutableSequence):
        self.list_nodes = [Node(value) for value in value]
        self.head = self.list_nodes[0] # указатель на первый элемент

        for i in range(len(self.list_nodes) - 1):
            current_node = self.list_nodes[i]
            next_node = self.list_nodes[i + 1]
            self.linked_nodes(current_node, next_node)

    # Создаем функцию, которая связывает между собой два узла.
    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        # left_node: Левый или предыдущий узел
        # right_node: Правый или следующий узел
        left_node.set_next(right_node)
   
    def __repr__(self) -> str:
        return str(self.list_nodes)

    # Создаем функцию, которая выполняет перемещение по узлам
    # до указанного индекса. И возвращает узел
    def step_by_step_on_nodes(self, index: int) -> Node:
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    # Реализаия метода __getitem__
    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    # Реализация метода __setitem__
    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    # реализиция метода __delitem__
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

    # реализиция метода __len__
    def __len__(self) -> int:
        return self.len

    #  Реализация метода __repr__ через to_list
    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"
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

    # еализация метода append
    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)
        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.Linled_nodes(self.tail, append_node)
            self.tail = append_node

class DoubleLinkedList(LinkedList):
    def __init__(self, value: Any, next_: Optional["LinkedList"] = None):
        super().__init__(value, next_)  # вызвать конструктор базового класса
        pass

if __name__ == '__main__':

    list_ = [1, 2, 3]

    ll = LinkedList(list_)
    print(ll)

    ll.append(200)
    print(ll)

    # Дополнительное задание, раелизация функции count

#class Glass:
    # создаем стаканы
    # использовали атрибут класса count, чтобы инициализировать
    # атрибут экземпляра класса count.
 #   count = 0  # количество созданных стаканов

  #  def __init__(self):
 #       cls = self.__class__  # type(self)
  #      cls.count += 1

    #создаем стакан №1
#glass_1 = Glass()
#print(Glass.count)  # проверяем количество созданных стаканов

    #создаем стакан №2
#glass_2 = Glass()
#print(Glass.count)  # проверяем количество созданных стаканов