# iteration

def iteration(n):
    res = ''
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f'({i}, {j})\n'
    return res

print(iteration(6))


def plus_1(n):
    res = 0
    for i in range(n + 1):
        res += i
    return res

print(plus_1(6))


def plus_2(n):
    res = 0
    i = 1
    while i <= n:
        res += i
        i += 1
    return res

print(plus_2(6))

# recursion

def recursion(n):
    if n == 1:
        return n
    res = recursion(n - 1)
    return res + n

print(recursion(6))


def tail_recursion(n, res=0):
    if n == 0:
        return res
    return tail_recursion(n - 1, res + n)

print((tail_recursion(6)))