# 第八章 函数

# # 定义函数
def favorite_book(title):
    """最喜欢的书之一"""
    print(f'One of my favorite books is {title.title()}')

favorite_book("alice in wonderland")

# # 传递实参：位置实参
def money(RMB, Dollar):
    print(f'You have {RMB} yuan and {Dollar} dollars.')

money(100,1000)

# # 传递实参：关键字实参
money(RMB = 100, Dollar = 1000)

# # 默认值
def money(rmb = 100, dollar = 1):
    print(f'You have {rmb} yuan and {dollar} dollars.')

money(dollar = 1000)

