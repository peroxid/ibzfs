#!/usr/bin/python -tt

from threading import Lock

class Node():
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        self.root = self

    def add_child(self, child):
        # Add a child node
        child.parent = self
        child.root = self.root
        self.children.append(child)

    def del_child(self, child):
        # Delete a child node
        self.children.remove(child)

    def is_leaf(self):
        # Returns true if there are no children
        if len(self.children) == 0:
            return True
        else:
            return False

    def is_root(self):
        # Returns true if this is the root node
        if self.root == self:
            return True
        else:
            return False

    def get_root(self):
        # Returns the top level node
        return self.root

    def up(self):
        # Returns parent node
        if self.parent == None:
            return self
        else:
            return self.parent

    def get_children(self):
        # Returns a list of children
        return self.children

    def get_sisters(self):
        # Returns a list of nodes on the same level
        if self.is_root():
            return []
        else:
            return [ child for child in self.parent if child != self ]

    def __iter__(self):
        # For iterating over the node
        for child in self.children:
            yield child
