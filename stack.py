# Programmer & userID = Niyam Acharya & nka42
# Program Date = 11/29/2023
# Description:
# Implements NewStack using LinkedList as its underlying data structure.
# NewStack provides stack functionalities: push, pop, isEmpty, and size tracking.
# Uses a linked list to manage elements and maintain Last-In-First-Out (LIFO) order.

from linkedList import LinkedList  # Importing the provided LinkedList class

class NewStack:
    def __init__(self):
        self.linked_list = LinkedList()

    def put(self, item):
        self.linked_list.append(item)

    def get(self):
        if self.isEmpty():
            return None
        last_node = self.linked_list.getHead()
        prev_node = None
        while last_node.getNext():
            prev_node = last_node
            last_node = last_node.getNext()
        if prev_node:
            prev_node.setNext(None)
        else:
            self.linked_list.setHead(None)
        return last_node.getData()

    def isEmpty(self):
        return self.linked_list.getHead() is None

    def __str__(self):
        if self.isEmpty():
            return 'Empty Stack'
        stack_str = ""
        current = self.linked_list.getHead()
        while current:
            stack_str += str(current.getData()) + "\n"
            current = current.getNext()
        return stack_str.strip()

    def __len__(self):
        count = 0
        current = self.linked_list.getHead()
        while current:
            count += 1
            current = current.getNext()
        return count
