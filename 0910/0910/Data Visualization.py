# 数据可视化

import matplotlib.pyplot as plt

# # 自动计算数据
values = range(1, 21)
squares = [x**2 for x in values]

# values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
#           12, 13, 14, 15, 16, 17, 18, 19, 20]
# squares = [1, 4, 9, 16, 25, 36, 49, 64,
#            81, 100, 121, 144, 169, 196,
#            225, 256, 289, 324, 361, 400]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

# # 绘制折线图
ax.plot(values, squares, linewidth=3, color='pink')

# # 绘制散点图
ax.scatter(values, squares, s=100, color='grey')

# # 设置标题
ax.set_title('Square Numbers', fontsize=30)
ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Square', fontsize=15)
# # 设置刻度大小
ax.tick_params(labelsize=15)
# # 设置每个坐标轴的取值范围
ax.axis([0, 25, 0, 500])

# plt.show()

# # 自动保存绘图
plt.savefig('squares_plot.png', bbox_inches='tight')