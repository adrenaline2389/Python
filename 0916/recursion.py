# 递归：理解起来有点吃力，需要重复
def recursion(n):
    """递归计算1+2+...+n"""
    # 终止条件
    if n == 1:
        return 1
    # 递：递归调用
    res = recursion(n - 1)
    # 归：返回结果
    return n + res

print(recursion(999))   # 最大递归深度：999，超过会导致栈溢出错误


# 尾递归
def tail_recursion(n, res):
    """尾递归"""
    # 终止条件
    if n == 0:
        return res
    # 尾递归调用
    return tail_recursion(n - 1, res + n)

print(tail_recursion(998, 0))   # 最大尾递归深度：998，超过会导致栈溢出错误(Python默认不支持尾递归优化)


# 递归树：斐波那契数列(二叉树)
def fibonacci_sequence(n):
    """计算数列第n位数字"""
    # 终止条件
    if n == 1 or n == 2:
        return n - 1
    # 递归调用
    res = fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)
    # 返回结果
    return res

print(fibonacci_sequence(30))


# 使用迭代模拟递归
def for_loop_recur(n):
    # 使用一个显式的栈来模拟系统调用栈
    stack = []
    res = 0

    # 递：递归调用
    for i in range(n, 0, -1):
        # 通过"入栈操作"来模拟"递"
        stack.append(i)
    # 归：返回结果
    while stack:
        # 通过"出栈操作"来模拟"归"
        res += stack.pop()
    # res = 1+2+3+...+n
    return res

print(for_loop_recur(1000))