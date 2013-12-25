from tree import Tree
t = Tree()
t.makepath('/usr/local/bin')
print t.fs
t.makepath('/opt/local/bin')
print t.fs
#t.move('/usr', '/opt/local')
#print t.fs
