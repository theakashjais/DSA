#!/usr/bin/env python3

class ArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.head = 0
        self.tail = 0

    def __str__(self):
        # https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
        string = "\033[94m["
        for i in range(self.size()):
            string += str(self.array[(self.head + i) % self.capacity])
            if i != self.size() - 1:
                string += ", "
        string += "]\033[0m"
        return string

    def size(self):
        if self.tail < self.head:
            return self.capacity - (self.head - self.tail)
        else:
            return self.tail - self.head

    def is_empty(self):
        return self.tail == self.head

    def is_full(self):
        return self.size() == self.capacity - 1

    def enqueue(self, elem):
        if self.is_full():
            print("Error: queue is full")
        else:
            self.array[self.tail] = elem
            self.tail = (self.tail + 1) % self.capacity

    def dequeue(self):
        if self.is_empty():
            print("Error: queue is empty")
            return None
        elem = self.array[self.head]
        self.head = (self.head + 1) % self.capacity
        return elem


queue = ArrayQueue(10)
for i in range(0, 10):
    queue.enqueue(i)
print("queue:", queue)
print("dequeue:", queue.dequeue())
print("dequeue:", queue.dequeue())
print("queue:", queue)
