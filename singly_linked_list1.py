class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# first = Node(10)

# print(first.value)
# print(first.next)

class LinkedList:
    def __init__(self):
        self.head = None # empty list to start

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while(temp.next is not None):
            temp = temp.next

        temp.next = new_node

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next

        print("None")






n1 = LinkedList()
n1.append(50)
n1.append(60)
n1.append(70)
n1.append(80)
n1.append(90)

n1.print_list()