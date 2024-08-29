#   *
#  ***
# *****
#  ***
#   *

n = eval(input("请输入星星最大长度n"))
# for i in range(n // 2 + 1):
#     a = (2 * (i+1) - 1)
#     print(' ' * int((n // 2 + 1) - i), end="")
#     print('*' * a)
#
# for i in range(n // 2):
#     a = (2 * (i+1) - 1)
#     print(' ' * (i - (n // 2 + 1)),  end="")
#     print('*' * a)

for i in range(-(n // 2), n // 2 + 1):
    print(" " * abs(i))
    print("*" * (n - abs(i) * 2))

i = -(n // 2)

while i < n // 2 + 1:
    i = i + 1




m, n = 10, 10
for i in range(0, m):
    a = "*"
    if i == 0 or i == m - 1:
        for j in range(1, n):
            a = a + "*"
    else:
        for j in range(1, n - 1):
            a = a + " "
        a = a + "*"
        # 法二
        # a = " " * (n - 2)
        # a = a + "*"
    print(a)

    # for i in range(1, m - 1):
    #     print(a.replace('*' * n, '*' + ' ' * (n - 2) + '*'))

for i in range(3):
    for j in range(3):
        print(f"i = {i}, j = {j}")


a = "*"
for i in range(10):
    a = a + "*"
    print(a)

for i in range(3):
    for j in range(7 - i * 3, 10 - i * 3):
        print(j, end=" ")
    print()

    # a = 0
    # for j in range(1, 4):
    #     a = j
    #     print(a, end=" ")
    # print()
    # for j in range(4, 7):
    #     a = j
    #     print(a, end=" ")
    # print()
    # for j in range(7,10):
    #     a = j
    #     print(a,end=" ")
    # print()
