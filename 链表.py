"""
一系列节点组成的元素集合

"""
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

# a = Node(1)
# b = Node(2)
# c = Node(3)
# a.next = b
# b.next = c
#
# print(a.next.item)

def create_linklist_head(l):  #头插法
    head = Node(l[0])
    for element in l[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

def create_linklist_tail(l):  #尾插法
    head = Node(l[0])
    tail = head
    for element in l[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

def print_linklist(lk):
    while lk:
        print(type(lk.item))
        lk = lk.next


lk = create_linklist_tail([1,2,3,6,8])
print_linklist(lk)