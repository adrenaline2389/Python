# 嵌套循环
def nested_for_loop(n):
    res = ""
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            res += f"({i}, {j}), "
    return res

print(nested_for_loop(6))