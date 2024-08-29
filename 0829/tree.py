class TreeNode:
    def __init__(self, val, l, r):
        self.value = val
        self.left = l
        self.right = r

cur3 = TreeNode(3, None, None)
cur2 = TreeNode(2, None, None)
cur1 = TreeNode(1, cur3, None)
cur0 = TreeNode(0, cur1, cur2)

print(cur0.value, cur0.left.value, cur0.right.value)

# 递归就是栈 前序遍历 中序遍历 后序遍历
def prevSort(cur):
    if cur == None:
        return
    else:
        prevSort(cur.left)
        prevSort(cur.right)
        print(cur.value)

# 层序遍历
def levelSort(root):
   queue = [root]
   while len(queue) != 0:
       val = queue.pop(0)
       print(val.value)
       if val.left is not None:
           queue.append(val.left)
       if val.right is not None:
           queue.append(val.right)

# prevSort(cur0)
levelSort(cur0)
