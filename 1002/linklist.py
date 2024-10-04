class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create():
    head = None
    pre = None

    # 读入第一个节点数据
    data = int(input())

    while data != 0:
        cur = Node(data)  # 创建新节点

        if head is None:
            head = cur  # 第一个节点作为头节点
        else:
            pre.next = cur  # 链接前驱节点与当前节点

        pre = cur  # 更新前驱节点
        data = int(input())  # 继续输入数据

    return head


def print_list(n):
    while n:
        print(n.data, end=" ")  # 打印当前节点数据
        n = n.next  # 移动到下一个节点
    print()


# 主函数
if __name__ == "__main__":
    head = create()  # 创建链表
    print_list(head)  # 打印链表