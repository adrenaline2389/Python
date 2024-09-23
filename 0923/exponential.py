# 指数阶（循环实现）
def iter_exponential(n):
    count = 0
    base = 1
    for i in range(n):
        for j in range(base):
            count += 1
        base *= 2
    # count = 1 + 2 + 4 + 8 ...
    return count, base

print(iter_exponential(3))


# 指数阶（递归实现）
def recur_exponential(n):
    if n == 1:
        return 1
    return recur_exponential(n - 1) + recur_exponential(n - 1) + 1

print(recur_exponential(3))