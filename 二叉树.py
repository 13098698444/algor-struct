

class BitreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

a = BitreeNode('A')
b = BitreeNode('B')
c = BitreeNode('C')
d = BitreeNode('D')
e = BitreeNode('E')
f = BitreeNode('F')
g = BitreeNode('G')

e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.lchild = d
g.lchild = f

root = e
print(root.lchild.rchild.data)
