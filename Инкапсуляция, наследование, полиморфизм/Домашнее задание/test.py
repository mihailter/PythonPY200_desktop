class LinkedList:
    # метод возвращает количество полученных элементов
    def __init__(self):
        self.head = None

    def count(self, element):
        start = self.head
        count1 = 0
        while start:
            if start.getData() == element:
                count1 += 1
            start = start.getNextNode()
        return count1