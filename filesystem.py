#!/usr/bin/python -tt

from tree import Node

class Filesystem():
    def __init__(self):
        self.index = {}
        self.tree = Node("root")

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

    def delete(self, _file):
        pass

    def ls(self, path):
        pass

    def print(self, tree):
        pass

    def copy(self, src, tgt):
        pass

    def mkdir(self, path):
        pass
