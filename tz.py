class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse_print_list(self):
        stack = []
        current = self.head
        while current:
            stack.append(current.data)
            current = current.next
        stack.append('None')
        while stack:
            print(stack.pop(), end=" ")




linked_list = LinkedList()
linked_list.append("A")
linked_list.append("B")
linked_list.append("C")
linked_list.append("D")
linked_list.append("E")
linked_list.reverse_print_list()

