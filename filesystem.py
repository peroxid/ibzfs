#!/usr/bin/python -tt

from tree import Node
from myfile import _File

class Filesystem():
    def __init__(self):
        self.index = {}
        self.tree = Node('/')
        self.add_to_index('/', self.tree)

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

    def write(self, _file, path):
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
            if isinstance(child, _File):
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
        cur_path = []
        for _dir in path.split('/'):
            # If the directory name is empty, we've go nothing to do
            if _dir == '':
                continue
            else:
                # Prepend a / to the directory name to work around the '/'.join problem
                cur_path.append(''.join(['/', _dir]))

            # If the current directory node does not exist, create it
            if not self.is_in_index(''.join(cur_path)):
                _dir = ''.join(['/', _dir])
                new_node = Node(_dir)
                # If we are unable to find the parent, that means we're
                # a child of / itself
                if not self.is_in_index(''.join(cur_path[:-1])):
                    parent = self.get_from_index('/')
                else:
                    parent = self.get_from_index(''.join(cur_path[:-1]))
                parent.add_child(new_node)
                self.add_to_index(''.join(cur_path), new_node)
            else:
                # If the directory is found, make sure it is a directory and not
                # a file or something crazy
                obj = self.get_from_index(''.join(cur_path))
                if not isinstance(obj, Node):
                    raise RuntimeError("attempted to overwrite existing file")

