# 第四章

# # 循环
A = ['alpha','beta','gamma','delta','epsilon']
for i in A:
    print(i)

# # range()函数
B = list(range(1, 6))
print(B)

# # 简单统计计算
C = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sum(C))
print(max(C))
print(min(C))

# # 切片 slice
D = ['alpha','beta','gamma','delta','epsilon']
print(D[0:5])
print(D[0:])
print(D[:5])
print(D[-5:-1])
print(D[-5:])
print(D[:-1])

# # 遍历切片
E = ['alpha','beta','gamma','delta','epsilon']
for i in E[:3]:
    print(i.title())

# # 复制列表
F = ['alpha','beta','gamma','delta','epsilon']
G = F[:]   # 不等于"G = F"
print(E)
print(F)
F.append('omega')
G.append('sigma')
print(F)
print(G)

# # 元组（不可变的）
H = ('alpha','beta','gamma','delta','epsilon')
print(H[0])
for i in H:
    print(i)
H = ('alpha','beta','gamma')
print(H)

# # range()函数指定步长
odd_nums = list(range(1,10,2))
even_nums = list(range(2,11,2))
print(odd_nums)
print(even_nums)

# # 列表推导式
squares1 = []
for i in range(1, 11):
    squares1.append(i ** 2)
print(squares1)

squares2 = [i ** 2 for i in range(1, 11)]
print(squares2)