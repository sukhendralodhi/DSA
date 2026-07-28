class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


first = Node(10)
# print(first.data)
# print(first.next)
second = Node(20)

first.next = second # this is the whole track

# print(first.data)
# print(first.next.data)

third = Node(30)

second.next = third

# print(first.data)
# print(first.next.data)
# print(first.next.next.data)

fourth = Node(40)

third.next = fourth

# print(first.data)
# print(first.next.data)
# print(first.next.next.data)
# print(first.next.next.next.data)

temp = first
howmany_node = 0

while temp is not None:
    howmany_node = howmany_node + 1
    temp = temp.next

print(howmany_node)