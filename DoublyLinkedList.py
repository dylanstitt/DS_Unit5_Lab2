# Dylan Stitt
# Unit 5 Lab 2
# Doubly Linked List

class DoublyLinkedList:

    class DoublyNode:
        # Nested Doubly Node Class

        def __init__(self, val):
            """Doubly Node Constructor"""
            self.value = val
            self.next = None
            self.prev = None

        def __str__(self):
            """Doubly Node String Method"""
            return f"|{self.value}|"

        def set_next(self, node):
            """Sets next to a new node"""
            if type(node) == type(self) or node is None:
                self.next = node
            else:
                raise TypeError('Node is not type DoublyNode or None')
            
        def set_prev(self, node):
            if type(node) == type(self) or node is None:
                self.prev = node
            else:
                raise TypeError('Node is not type DoublyNode or None')

    def __init__(self):
        """Doubly Linked List Constructor"""
        self.head = None
        self.tail = None
        self.__size = 0

    def __str__(self):
        """Doubly Linked List String Method"""
        out = "HEAD > "

        walk = self.head
        for i in range(self.__size):
            out += f"{walk} "
            walk = walk.next
            if walk is not None:
                out += "-> "

        out += "< TAIL"
        return out

    def __len__(self):
        """Returns the length of the doubly linked list"""
        return self.__size

    def __is_empty(self):
        """Returns if the doubly linked list is empty"""
        return self.__size == 0

    def head_insert(self, val):
        """Insert a node at the head of the doubly linked list"""
        node = self.DoublyNode(val)
        node.set_next(self.head)
        self.head.set_prev(node)

        if self.__is_empty():
            self.head = node
            self.tail = node
        else:
            self.head = node

        self.__size += 1

    def head_remove(self):
        """Remove and return the head of the doubly linked list"""
        if self.__is_empty():
            raise ValueError("Doubly Linked List is empty")
        else:
            h = self.head
            self.head = self.head.next
            self.head.set_prev(None)
            self.__size -= 1

            if self.__is_empty():
                self.head = None
                self.tail = None
            return h.value

    def tail_insert(self, val):
        """Insert a node at the tail of the doubly linked list"""
        node = self.DoublyNode(val)
        self.tail.set_next(node)
        t = self.tail

        if self.__is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail = node

        self.tail.set_prev(t)
        self.__size += 1

    def tail_remove(self):
        """Remove and return the tail of the doubly linked list"""
        if self.__is_empty():
            raise ValueError("Doubly Linked List is empty")
        else:
            t = self.tail
            self.tail = self.tail.prev
            self.tail.set_next(None)
            self.__size -= 1

            if self.__is_empty():
                self.head = None
                self.tail = None
            return t.value
