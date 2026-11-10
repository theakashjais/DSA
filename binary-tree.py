import pydot

from enum import Enum

class Order(Enum):
    PRE = 'pre-order'
    IN = 'in-order'
    POST = 'post-order'
    LEVEL = 'level-order'

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def print(self, node, order):
        if order == Order.PRE:
            print(f'{node.key}', end='-')
            if node.left:
                self.print(node.left, order)
            if node.right:
                self.print(node.right, order)
        elif order == Order.IN:
            if node.left:
                self.print(node.left, order)
            print(f'{node.key}', end='-')
            if node.right:
                self.print(node.right, order)
        elif order == Order.POST:
            if node.left:
                self.print(node.left, order)
            if node.right:
                self.print(node.right, order)
            print(f'{node.key}', end='-')
        elif order == Order.LEVEL:
            queue = [node]
            while queue:
                node = queue.pop(0)
                print(f'{node.key}', end='-')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

    def pretty_print(self, order):
        print(f'{order.value}: ', end='')
        if self.root:
            self.print(self.root, order)
        print('')

    def write_tree(self, name):
        tree = pydot.Dot(graph_type='graph')

        def traverse(node):
            if node:
                tree.add_node(pydot.Node(node.key))
                if node.left:
                    tree.add_edge(pydot.Edge(node.key, node.left.key))
                    traverse(node.left)
                if node.right:
                    tree.add_edge(pydot.Edge(node.key, node.right.key))
                    traverse(node.right)

        traverse(self.root)
        tree.write_pdf(name)


class BinarySearchTree(BinaryTree):
    # __init__ gets inherited from BinaryTree
    #def __init__(self):
    #    BinaryTree.__init__(self)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            node = Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else: # key == node.key: no duplicates
            pass
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        # recursively rebuild the tree, descending to the left or right subtree
        if key < node.key:
            node.left = self._delete(node.left, key)
            return node
        elif key > node.key:
            node.right = self._delete(node.right, key)
            return node
        else: # key == node.key:
            if node.left == None:
                # delete node with 0 or 1 child
                return node.right
            elif node.right == None:
                # delete node with 1 child
                return node.left
            else:
                # delete node with 2 children
                # replace the node with its inorder successor
                successor = node.right
                while successor.left:
                    successor = successor.left

                node.key = successor.key
                node.right = self._delete(node.right, successor.key)
                return node


#a = Node('a')
#b = Node('b')
#c = Node('c')
#d = Node('d')
#e = Node('e')
#f = Node('f')
#g = Node('g')
#a.left = b
#a.right = c
#b.right = d
#c.left = e
#c.right = f
#f.left = g
#
#tree = BinaryTree()
#tree.root = a
#tree.pretty_print(Order.PRE)
#tree.pretty_print(Order.IN)
#tree.pretty_print(Order.POST)
#tree.pretty_print(Order.LEVEL)

tree = BinarySearchTree()
tree.insert('d')
tree.insert('f')
tree.insert('b')
tree.insert('c')
tree.insert('a')
tree.insert('e')
tree.insert('d')
tree.insert('h')
tree.insert('g')
tree.write_tree('binary-tree.pdf')
tree.pretty_print(Order.PRE)
tree.pretty_print(Order.IN)
tree.pretty_print(Order.POST)
tree.pretty_print(Order.LEVEL)
tree.delete('h')
tree.write_tree('binary-tree-del.pdf')
