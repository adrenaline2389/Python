# 数据可视化

# # 绘制折线图
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]

fig, ax = plt.subplots()
ax.plot(squares)

plt.show()