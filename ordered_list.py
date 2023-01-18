# Ordered List [Data Structures]
# Joshua Estrada

class Node:
    # Node with next and prev attributes
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class OrderedList:
    # A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head
        self.head.prev = self.head
    # Linked List uses ONE dummy node

    def is_empty(self):
        return self.head.next == self.head
        # returns True if OrderedList is empty (O(1) performance)

    def add(self, item):
        if self.is_empty():
            n = Node(item)
            n.next = self.head
            n.prev = self.head
            self.head.next = n
            self.head.prev = n
            return True
        n = Node(item)
        node = self.head
        while True:
            if node.next.item == item:
                return False
            if node.next == self.head or n.item < node.next.item:
                n.next = node.next
                n.prev = node
                node.next.prev = n
                node.next = n
                return True
            else:
                node = node.next
        # adds item to OrderedList based on Order -> return True
        # if item already in list -> return False
        # items added to list is assumed to be comparable using < operator
        # algorithm has 0(n) performance

    def remove(self, item):
        node = self.head.next
        while node != self.head:
            if node.item == item:
                node.prev.next = node.next
                node.next.prev = node.prev
                return True
            else:
                node = node.next
        return False
        # removes first occurrence of an item
        # if target item in list -> return True
        # if target item not in list -> return False
        # algorithm has 0(n) performance

    def index(self, item):
        node = self.head.next
        idx = 0
        while node != self.head:
            if node.item == item:
                return idx
            else:
                node = node.next
                idx += 1
        return None
        # returns index of first occurrence of an item
        # if item is not in list -> return None
        # algorithm has 0(n) performance

    def pop(self, index):
        if index < 0:
            raise IndexError
        node = self.head.next
        idx = 0
        while node != self.head:
            if idx == index:
                node.prev.next = node.next
                node.next.prev = node.prev
                return node.item
            else:
                idx += 1
                node = node.next
        raise IndexError
        # removes and returns item at given index
        # if index is negative or >= size of list raise IndexError
        # algorithm performance is 0(n)

    def search(self, item):
        return self.search_help(self.head.next, item)

    def search_help(self, node, item):
        if node == self.head:
            return False
        if node.item == item:
            return True
        return self.search_help(node.next, item)
        # return if item is found -> True/False
        # searches OrderedList for item
        # algorithm performance is 0(n)

    def python_list(self):
        if self.is_empty(): return []
        node = self.head.next
        if node.next == self.head: return [node.item]
        lst = []
        while True:
            lst.append(node.item)
            node = node.next
            if node.next == self.head:
                lst.append(node.item)
                break
        return lst
        # return list representation of Ordered List [head to tail]
        # algorithm performance is 0(n)

    def python_list_reversed(self):
        if self.is_empty(): return []
        return self.python_list_reversed_help(self.head.next, [])

    def python_list_reversed_help(self, node, lst):
        if node.next == self.head:
            return [node.item]
        else:
            return self.python_list_reversed_help(node.next, lst) + [node.item]
        # return list representation of Ordered List [tail to head]
        # must call recursive method
        # must be reversed list
        # algorithm performance is 0(n)

    def size(self):
        return self.size_help(self.head.next)

    def size_help(self, node):
        if node == self.head:
            return 0
        return 1 + self.size_help(node.next)
        # return number of items in OrderedList
        # must call recursive method
        # function must count and return num of items in list
        # algorithm performance is 0(n)

    '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
