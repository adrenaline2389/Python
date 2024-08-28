import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    data = pd.read_excel('data/1.xlsx', header=None, sheet_name='Sheet2')
    # data = data.fillna(0)
    # data = data.dropna()

    data = np.array(data).flatten()
    print(data)
    print(sum(data))
    # 均值,中位数,上,下四分位数,三均值
    print(data.mean())

    n = len(data)
    sum_data = 0
    for i in range(n):
        sum_data += data[i]
    average = sum_data / n
    print(average)
    # data.sort()
    # print(data)
    data_copy = sorted(data)
    print(data_copy)
    if n % 2 == 0:
        print(n / 2)
        median = (data_copy[int(n / 2 - 1)] + data_copy[int(n / 2)]) / 2
        quarter1 = (data_copy[int(n /4 - 1)] + data_copy[int(n / 4)]) / 2
        quarter3 = (data_copy[int(3 * n / 4 - 1)] + data_copy[int(3 * n / 4)]) / 2
    else:
        median = data_copy[int(n / 2)]
        quarter1 = data_copy[int(n / 4)]
        quarter3 = data_copy[int(3 * n / 4)]
    trimean = 0.25 * quarter1 + 0.5 * median + 0.25 * quarter3

    print(median)
    print(quarter1)
    print(quarter3)
    print(trimean)

    sns.boxplot(data=data)
    plt.show()

