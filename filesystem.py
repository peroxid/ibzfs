#!/usr/bin/python -tt

class Filesystem():
    def __init__(self):
        self.index = {}

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

    def write(self, _file):
        pass

    def read(self, path):
        pass

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
