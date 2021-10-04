#if __name__ == "__main__":

#class LinkedList:
 #   a = [5, 10, 15, 20, 25]

  #  count = a.count(15)

   # count = a.count(20)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def add(self, data):
        new_list = list(data)
        if (self.head is None):
            self.head = self.tail = new_list
        else:
            self.tail.set_next(new_list)
            self.tail = new_list

    def count_nodes(biscuit_list):
        count = 0
        # PLEASE HELP ME IN THIS CODE TO GET SUITABLE OUTPUT....
        temp = list.get_data(biscuit_list.get_head())
        while (temp is not None):
            count += 1
            temp = list(temp).get_next()
        return count

biscuit_list = LinkedList()
biscuit_list.add("Goodday")
biscuit_list.add("Bourbon")
biscuit_list.add("Hide&Seek")
biscuit_list.add("Nutrichoice")

print(count_nodes(biscuit_list))

    # Write your solution here
   # pass
