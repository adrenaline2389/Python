# 循环实现
def iter_logarithm(n):
    count = 0
    while n > 1:
        n = n / 2
        count += 1
    return count

print(iter_logarithm(16))


# 递归实现
def recur_logarithm(n):
    if n <= 1:
        return 0
    return recur_logarithm(n / 2) + 1

print(recur_logarithm(16))


# 线性对数阶（n * log_n)  不理解!!!
def linear_log_recur(n):
    if n <= 1:
        return 1
    count = linear_log_recur(n // 2) + linear_log_recur(n // 2)
    for i in range(n):
        count += 1
    return count