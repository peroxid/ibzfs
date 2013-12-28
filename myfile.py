#!/usr/bin/python -tt


class _File():
    def __init__(self):
        self.data = ''
        return

    def open(self, filesystem):
        # Open file for i/o
        # TODO
        return

    def read(self, offset, amount):
        # Return amount bytes starting with offset
        if offset < 0 or amount < 0 or amount == 0:
            return False
        piece = self.data[offset:offset+amount]
        return piece

    def write(self, offset, data):
        # Write data starting at offset
        self.data = ''.join([self.data[:offset], data, self.data[offset:]])
        return

    def flush(self, filesystem):
        # Write data to filesystem
        # TODO
        return


