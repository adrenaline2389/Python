# 第三章

A = []

# # 增
A.append('alpha')
A.append('gamma')
print(A)

A.insert(1,'beta')
A.insert(3,'delta')
A.insert(4,'epsilon')
print(A)


# # 删
del A[4]
print(A)

A.pop()
print(A)

A.remove('gamma')
print(A)


# # 查
print(len(A))


# # 改
A.sort(reverse = True)
print(A)

A = sorted(A,reverse=True)
print(A)

