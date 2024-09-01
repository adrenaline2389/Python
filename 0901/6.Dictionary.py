# 第六章

A = {
    '1' : 'alpha',
     '2' : 'beta',
     '3' : 'gamma',
     '4' : 'delta',
     }

# # 查
print(A['1'])

# # 增
A['5'] = 'epsilon'
print(A)
# # 改
A['5'] = 'omega'
print(A)
# # 删
del A['5']
print(A)

# # get() 函数来访问值
a = A.get('5', 'no fifth')
b = A.get('4', 'no fourth')
print(a, b)

# # 遍历所有键值对
print(A.items())
for key, value in A.items():
    print(f'\nKey: {key}')
    print(f'\nValue: {value}')

# # 遍历所有键
print(A.keys())
for i in A.keys():
    print(i)
for i in A:
    print(i)

# # 按特定顺序遍历所有键
for i in sorted(A, reverse = True):
    print(i)

# # 遍历所有值
for i in A.values():
    print(i)

# # 用集合剔除重复项
A['5'] = 'delta'
for i in set(A.values()):
    print(i)

