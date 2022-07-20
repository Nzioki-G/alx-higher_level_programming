#!/usr/bin/python3
"""A Node object"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets data from given args"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the next node and returns it"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the next_node, returns nothing"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""A SIngly Linked List object"""


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """inserts a node into the list with value as Node's data
            Args:
                @value(int): the data value of Node to insert"""
        new_node = Node(value)

        if (self.__head is None):
            new_node.next_node = None
            self.__head = new_node

        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node

        else:
            current = self.__head
            while current.next_node is not None and
            current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """to string func
            Returns:
                printable list"""
        my_list = []
        current = self.__head

        while current is not None:
            my_list.append(str(current.data))
            current = current.next_node

        return "\n".join(my_list)


"""A Singly linked list object"""


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        The node is inserted into the list at the correct
        ordered numerical position.
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
