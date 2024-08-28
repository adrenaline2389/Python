class Node:
    # val = 0
    # next = None
    def __init__(self, e, f):
        self.a = e
        self.b = f
# 创建头和cur
head = Node(-1, None)
d = head

# 创建一个Node对象，里面初始为i，下一个结点（门牌号）是None
# cur下一个结点是刚创建的结点
# cur转到下一个结点
for i in range(10):
    c = Node(i,None)
    d.b = c
    d = d.b

d = head
for i in range(11):
    print(d.a)
    d = d.b

# c = Node(0,None)
# cur.nextNode = new_node
# new_node = Node(1,None)
# cur.nextNode.nextNode = new_node
# new_node = Node(2,None)
# cur.nextNode.nextNode.nextNode  = new_node
# new_node = Node(3,None)
# cur.nextNode.nextNode.nextNode .nextNode  = new_node
# new_node = Node(4,None)
# cur.nextNode.nextNode.nextNode.nextNode.nextNode  = new_node

cur = head
for i in range(11):
    print(cur.val)
    cur = cur.nextNode

class Person:
    height = 0
    weight = 0

person1 = Person()
print(person1)

class Cube:
    length = 0
    square = 0
    volumn = 0
    def __init__(self, len = 2, squ = 24):
        self.length = len
        self.square = squ

box = Cube()
print(box.length, box.square, box.volumn)
box.length = 1
print(box.length)

class A:
    def __init__(self,X = 0,Y = 0):
        self.X = X
        self.Y = Y

P = A(1,2)
Q = A()
Q.X = P
Q.X.X = P
print(Q.X.X)


class BinaryTreeNode:
    val = 0
    left = None
    right = None
    def __init__(self, v = 0, l = None, r = None):
        self.val = v
        self.left = l
        self.right = r


class TreeNode:
    children = []

# 峰度，偏度，数组，链表， 栈，队列， 类，循环，sum(), rgb