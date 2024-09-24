# 递归&迭代实现
def factorial_1(n):
    if n == 0:
        return 1
    count = 0
    for i in range(n):
        count += factorial_1(n - 1)
    return count

print(factorial_1(6))


# ChatGPT方法(recursion only）
def factorial_2(n):
    if n == 0:
        return 1
    return n * factorial_2(n - 1)

print(factorial_2(6))