ibzfs
=====
- File class
    Instantiate to get a file
    open()               # To enable reading the file
    read(offset, amount) # Read amount bytes starting with offset
    write(offset, data)  # Write data starting with offset
    close()              # Flush and close the file 

- Filesystem class
    Instantiate to get a filesystem
    Directory tree implemented as tree of dicts
    What about indexes for ls()?
    What about journaling? Perhaps an additional journaling tree?
    Perhaps a table as index with pointers to the tree
    What about keeping references to open files?
        init(path)         # Create a new filesystem, optionally loading it from disk
        close(path)        # Close filesystem, optionally saving it to disk
        save(path/to/file) # writes a File() instance
        open(path/to/file) # returns a File() instance
        ls(path)           # returns a list of files and directories
        mkdir(path)        # creates a directory path
        mv(path)           # moves a directory path or path to file


    

- Tree class
    Not really a tree, but a key-value store
    dict { 
           path:  [list of File()s] 
           path2: [list of File()s]
         }
    Methods:
        makepath(path)   # mkdir of filesystem implementation
        move(path)       # mv filesystem implementation
        list(path)       # ls filesystem implementation
        set(path)        # save filesystem implementation
        get(path)        # open filesystem implementation




