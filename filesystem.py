#!/usr/bin/python -tt

from tree import Node
from file import File

class Filesystem():
    def __init__(self):
        self.index = {}
        self.tree = Node('')

    def add_to_index(self, key, value):
        self.index[key] = value

    def del_from_index(self, key):
        del self.index[key]

    def get_from_index(self, key):
        return self.index[key]

    def is_in_index(self, key):
        try:
            self.index[key]
            return True
        except KeyError:
            return False

    def write(self, path, _file):
        # write _file to path in filesystem and update index
        _file.name = path.split('/')[-1]
        dirpath = '/'.join(path.split('/')[:-1])
        dirnode = self.get_from_index(dirpath)
        dirnode.add_child(_file)
        self.add_to_index(path, _file)

    def read(self, path):
        return self.get_from_index(path)

    def move(self, src, tgt):
        pass

    def delete(self, path):
        dirpath = '/'.join(path.split('/')[:-1])
        parent = self.get_from_index(dirpath)
        child = self.get_from_index(path)
        self.del_from_index(path)
        parent.del_child(child)

    def delete_recursive(self, path):
        dirpath = '/'.join(path.split('/')[:-1])
        parent = self.get_from_index(dirpath)
        for child in parent:
            if isinstance(child, File):
                self.del_from_index(child.get_path())
                parent.del_child(child)
            if isinstance(child, Node):
                if child.is_leaf():
                    self.del_from_index(child.get_path())
                    parent.del_child(child)
                else:
                    self.delete_recursive(child.get_path())
            else:
                raise RuntimeError("attempted to delete unknown object")

    def ls(self, path):
        pass

    def __repr__(self):
        pass

    def copy(self, src, tgt):
        pass

    def mkdir(self, path):
        pass
