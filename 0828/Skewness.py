# g = {n / [(n-1)*(n-2)*s^3]} * sigma(i=1,n)(xi - X)^3
import numpy as np
from numpy.ma.extras import average
from scipy.stats import kurtosis, skew
import pandas as pd
data = pd.read_excel('data/2.xlsx')


# nums = [1, 2, 3, 4,2,3,4,1,1,3,34,34,2,23,4,5]
nums = np.array(data)
n = len(nums)
X = average(nums)

# 循环没有用上i
# sum对集合求和, 不能对单独一个数求和
# for 里也是局部变量

a = 0
b = 0
c = 0
for i in range(n):
    a = a + (nums[i] - X) ** 2
    b = b + (nums[i] - X) ** 3
    c = c + (nums[i] - X) ** 4

s = (a / (n - 1))**0.5
g1 = n / (n - 1) / (n - 2) / s ** 3 * b
print(g1)
print(skew(np.array(nums)))

g2 = (n * (n + 1) * c) / ((n - 1) * (n - 2) * (n - 3)  * s ** 4) - (3 * (n - 1) ** 2) / ((n - 2) * (n - 3))
print(g2)




