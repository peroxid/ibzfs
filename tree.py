#!/usr/bin/python -tt

from threading import Lock

class Tree():
    #    makepath(path)   # mkdir of filesystem implementation
    #    move(path)       # mv filesystem implementation
    #    list(path)       # ls filesystem implementation
    #    get(path)        # save filesystem implementation
    #    set(path)        # open filesystem implementation
    def __init__(self, separator='/'):
        # Initiate root node
        self.root = { }
        self.lock = Lock()
        self.separator = separator
        return None

    def makepath(path):
        # If path does not exist, initialize
        try:
            self.root[path]
        except KeyError:
            self.lock.acquire()
            self.root[path] = []
            self.lock.release()
        return True

    def mv(src_path, tgt_path):
        # Move path or node
        # TODO
        return

    def ls(path):
        # Return list of files in path node
        return [ _file.name for _file in self.root[path] ]

    def get(path):
        # Return file found at path
        dir_path = self.separator.join(path.split(self.separator)[:-1])
        file_name = path.split(self.separator[-1])
        for _file in self.root[dir_path]:
            if _file.name == file_name:
                return _file
        raise ValueError('Requested node does not exist')

    def set(path, _new_file):
        # Insert file at path
        dir_path = self.separator.join(path.split(self.separator)[:-1])
        file_name = path.split(self.separator[-1])
        try:
            _dir = self.root[dir_path]
        except KeyError:
            raise ValueError('Directory does not exist')
        for _file in _dir:
            if _file.name == _new_file.name:
                raise ValueError('Node with same name already exists')
        self.lock.acquire()
        _dir.append(_new_file)
        self.root[dir_path] = _dir
        self.lock.release()
        return True

