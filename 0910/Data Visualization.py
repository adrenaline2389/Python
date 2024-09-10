# 数据可视化

# # 绘制折线图
import matplotlib.pyplot as plt

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
          12, 13, 14, 15, 16, 17, 18, 19, 20]
squares = [1, 4, 9, 16, 25, 36, 49, 64,
           81, 100, 121, 144, 169, 196,
           225, 256, 289, 324, 361, 400]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(values, squares, linewidth=3)

ax.set_title('Square Numbers', fontsize=30)
ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Square', fontsize=15)

ax.tick_params(labelsize=15)

plt.show()