#!/usr/bin/env python3

import pydot
import sys

class MaxHeap:
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.heap = [None] * (maxsize + 1)
        self.heap[0] = sys.maxsize
        self.ROOT = 1

    def __str__(self):
        return str(self.heap[self.ROOT:self.size+1])

    def parent(self, pos):
        return pos // 2

    def left_child(self, pos):
        return 2 * pos

    def right_child(self, pos):
        return 2 * pos + 1

    def is_leaf(self, pos):
        if pos > self.size // 2 and pos <= self.size:
            return True
        return False

    def swap(self, pos_a, pos_b):
        self.heap[pos_a], self.heap[pos_b] = (self.heap[pos_b], self.heap[pos_a])

    def upheap(self, pos):
        if self.heap[pos] > self.heap[self.parent(pos)]:
            self.swap(pos, self.parent(pos))
            self.upheap(self.parent(pos))

    def insert(self, key):
        if self.size >= self.maxsize:
            print("Error: heap is full")
        else:
            self.size += 1
            self.heap[self.size] = key
            self.upheap(self.size)

    def downheap(self, pos):
        if not self.is_leaf(pos):
            key = self.heap[pos]
            left_pos = self.left_child(pos)
            left_key = self.heap[left_pos]
            right_pos = self.right_child(pos)
            right_key = self.heap[right_pos]
            if key < left_key or key < right_key:
                if left_key < right_key:
                    # swap with the right child and heapify the right child
                    self.swap(pos, right_pos)
                    self.downheap(right_pos)
                else:
                    # swap with the left child and heapify the left child
                    self.swap(pos, left_pos)
                    self.downheap(left_pos)

    def extract(self):
        if self.size == 0:
            print("Error: heap is empty")
        else:
            max_val = self.heap[self.ROOT]
            self.heap[self.ROOT] = self.heap[self.size]
            self.size -= 1
            self.downheap(self.ROOT)
            return max_val

    def write_graph(self, name):
        graph = pydot.Dot(graph_type='graph')

        def traverse(pos):
            if pos <= self.size:
                graph.add_node(pydot.Node(self.heap[pos]))
                left = self.left_child(pos)
                right = self.right_child(pos)
                if left <= self.size:
                    graph.add_node(pydot.Node(self.heap[left]))
                    graph.add_edge(pydot.Edge(self.heap[pos], self.heap[left]))
                    traverse(left)
                if right <= self.size:
                    graph.add_node(pydot.Node(self.heap[right]))
                    graph.add_edge(pydot.Edge(self.heap[pos], self.heap[right]))
                    traverse(right)

        traverse(self.ROOT)
        graph.write_pdf(name + '.pdf')


heap = MaxHeap(42)
heap.insert(4)
heap.insert(1)
heap.insert(5)
heap.insert(10)
heap.insert(7)
heap.insert(8)
heap.insert(3)
print(heap)

heap.write_graph('maxheap_1')
print(f"extracted max value: {heap.extract()}")
heap.write_graph('maxheap_2')
print(f"extracted max value: {heap.extract()}")
heap.write_graph('maxheap_3')
