#!/usr/bin/env python3

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        string = "[ "
        current = self.head
        while current:
            if current != self.head:
                string += " -> "
            string += str(current)
            current = current.next
        string += " ]"
        return string

    def prepend(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert(self, data):
        node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        return None

    def delete(self, data):
        previous = None
        current = self.head
        while current:
            if current.data == data:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                # terminate while loop
                # help garbage collector
                current = None
            else:
                previous = current
                current = current.next

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_tmp = current.next
            current.next = previous
            previous = current
            current = next_tmp
        self.head = previous

    def new_reversed_list(self):
        llist = LinkedList()
        current = self.head
        while current:
            llist.prepend(current.data)
            current = current.next
        return llist

    def append_list(self, llist):
        current = llist.head
        while current:
            self.insert(current.data)
            current = current.next


ll = LinkedList()
ll.insert('l')
ll.insert('e')
ll.insert('g')
ll.insert('o')
#print(ll)
#ll.delete('e')
#ll.prepend('a')
print(ll)

# new_reversed_list()
ll_rev = ll.new_reversed_list()
print("new reversed list: ", end='')
print(ll_rev)
ll_rev_rev = ll_rev.new_reversed_list()
ll_rev_rev.delete('e')
ll_rev_rev.prepend('a')
print("new reversed list reversed: ", end='')
print(ll_rev_rev)

# append_list()
ll.append_list(ll_rev_rev)
print("reversed + new reversed list: ", end='')
print(ll)

# append list to itself: doesn't terminate!
# ll.append_list(ll)
