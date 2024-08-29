import pandas as pd
from numpy.ma.extras import average

data = pd.read_excel('data/副本2.xlsx')
data = data.fillna(0.0)
print(data)
# 打印列表
for i in data:
    print(i, end=" ")
print()

# 取data列表中的s1
# for i in data['s1']:
#     print(i, end=" ")
# print()

# for i in data['s2']:
#     print(i, end=" ")
# print()

data['s1'] = 1
print(data['s1'])
# print(average(data))
print(sum(data['s1']))
print(average(data['s1']))
data.to_excel("data/change2.xlsx")

