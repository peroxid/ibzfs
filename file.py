#!/usr/bin/python

from threading import Lock

class File():
    def __init__(self):
        self.data = ''
        self.lock = Lock()
        return

    def open(self, filesystem):
        # Open file for i/o
        # TODO
        return

    def read(self, offset, amount):
        # Return amount bytes starting with offset
        if offset < 0 or amount < 0 or amount == 0:
            return False
        self.lock.acquire()
        piece = self.data[offset:offset+amount]
        self.lock.release()
        return piece

    def write(self, offset, data):
        # Write data starting at offset
        self.lock.acquire()
        self.data = ''.join([self.data[:offset], data, self.data[offset:]])
        self.lock.release()
        return

    def flush(self, filesystem):
        # Write data to filesystem
        # TODO
        return


