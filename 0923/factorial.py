# 递归实现  不理解!!!
def factorial(n):
    if n == 0:
        return 1
    count = 0
    for i in range(n):
        count += factorial(n - 1)
    return count

print(factorial(6))