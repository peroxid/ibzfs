#!/usr/bin/python -tt


def main():
    print 'Import Filesystem and _File'
    from filesystem import Filesystem
    from myfile import _File

    print 'Creating filesystem'
    fs = Filesystem()
    print 'Creating directory /usr'
    fs.mkdir('/usr')
    print 'Creating directory /usr/local/bin'
    fs.mkdir('/usr/local/bin')
    print 'Creating file'
    _file = _File()
    print 'Writing to file'
    _file.write(0, 'blah blah blah')
    print 'Saving file to /usr/local/bin/file'
    fs.write(_file, '/usr/local/bin/file')
    print 'Deleting /usr/local/bin/file'
    fs.delete('/usr/local/bin/file')
    print 'Deleting /usr recursively'
    fs.delete_recursive('/usr')
    print 'All done'



if __name__ == '__main__':
    main()


