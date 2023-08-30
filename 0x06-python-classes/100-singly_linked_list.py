#!/usr/bin/python3
"""Defines the node of a singly linked list"""


class Node:
    """Singly linked list"""

    def __init__(self, data, next_node=None):
        '''instantiates a node with data and next'''
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        '''retrieves a node's data'''
        return self.__data

    @data.setter
    def data(self, value):
        '''sets/updates a node's data'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        '''retrieves a node's next_node'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''sets/updates the current node's next node'''
        if not isinstance(value, self.__class__):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a singly linked list"""


class SinglyLinkedList:
    '''a list of nodes pointing to each other'''

    def __init__(self):
        '''instantiates the list'''
        self.__head = None

    def sorted_insert(self, value):
        '''inserts a new node in correct sorted ascending order position'''
        new_node = Node(value)

        # insert at head
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr = self.__head
            while curr.next_node and curr.next_node.data < value:
                curr = curr.next_node
            if curr.next_node:
                new_node.next_node = curr.next_node
            curr.next_node = new_node

    def __str__(self):
        '''prints the entire list to stdout 1 node's data per line'''
        current = self.__head
        string = []
        while current:
            string.append(str(current.data))
            current = current.next_node
        return "\n".join(string)


"""
sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
"""
