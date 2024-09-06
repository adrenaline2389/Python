# 第八章 函数

# # 定义函数
def favorite_book(title):
    """最喜欢的书之一"""
    print(f'One of my favorite books is {title.title()}')

favorite_book("alice in wonderland")

# # 传递实参：位置实参
def money(rmb, dollar):
    print(f'You have {rmb} yuan and {dollar} dollars.')

money(100,1000)

# # 传递实参：关键字实参
money(rmb = 100, dollar = 1000)

# # 默认值(要把有默认值的形参放最后)
def money(rmb, dollar=1):
    print(f'You have {rmb} yuan and {dollar} dollars.')

money(rmb = 1)

# # 返回值
def get_formatted_name(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return full_name.title()

musician = get_formatted_name('michael', 'jackson')
print(musician)

# # 让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name = ''):
    full_name = f'{first_name} {middle_name} {last_name}'
    return full_name.title()

musician = get_formatted_name('michael', 'jackson')
print(musician)

# # 返回字典
def name(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

artist = name('Hideto', 'Matsumoto')
print(artist)

# # 传递列表
def alphabet(a, b):
    while a:
        cur = a.pop()
        b.append(cur)
        print(b)

A = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
B = []
alphabet(A[:], B)  # 把A列表的副本丢给函数，便不会影响原件A。

# # 传递任意数量的实参
def pizza(size, *toppings):
    print(f'\nMaking a {size}-inch pizza with the following toppings:')
    for topping in toppings:
        print(f'- {topping}')

pizza(8, 'cheese', 'salmon', 'tuna')

# # 使用任意数量的关键字实参
def profile(first, last, **info):
    info['first_name'] = first
    info['last_name'] = last
    return info

Michael_Jackson = profile('Michael', 'Jackson', tanlent = 'dancing', nationality = 'America')
print(Michael_Jackson)

# # 将函数储存在模块中(module_name.py)

    # 导入整个模块
    # # import module_name
    # # module_name.function_name()

    # 导入特定的函数
    # # from module_name import function_0, function_1, function_2

    # 使用as函数指定别名
    # # from module_name import function_name as fn
    # # import module_name as mn

    # 导入模块中所有函数
    # # from module_name import *