import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    file = open('data/drinkbrands.txt')
    data = []
    raw = file.readlines()
    for i in range(len(raw)):
        data.append(raw[i].strip())

    print(data)

    # 进阶用法
    # brands_set = set(data)
    # brands = []
    # brands_count = []
    # for brand in brands_set:
    #     brands.append(brand)
    #     brands_count.append(data.count(brand))
    #
    # plt.bar(brands, brands_count)
    # plt.show()

    a = data.count('百事可乐')
    b = data.count('旭日升冰茶')
    c = data.count('可口可乐')
    d = data.count('露露')
    e = data.count('汇源果汁')

    x = ['百事可乐', '旭日升冰茶', '可口可乐', '露露', '汇源果汁']
    y = [a, b, c, d, e]
    plt.rcParams['font.sans-serif'] = ['simHei']
    plt.rcParams['axes.unicode_minus'] = False


    plt.bar(x = x, height = y)
    plt.show()
    plt.pie(x=y,labels=x,colors=['red', "green", "#000000",])
    plt.show()