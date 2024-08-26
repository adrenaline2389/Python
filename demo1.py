# 伪代码：先给出3个变量，再获得用户的输入，电脑再从三个变量中随机选择一个

# 任务
# 1. 设计一个石头剪刀布游戏
# 2. input， if， 循环 break continue， = ==， and or的用法，字典和列表
# 3. if的优化（代码的重构）程序的健壮性 非法输入的处理
# 4. 自己想的优化点 电脑随机出拳（advantage：等概率直接取整，可以直接取数。

# 课后作业
# 电脑根据我出拳的招式优化自己的策略
# 三个随机数
# 石头 random + 剪刀的概率 * alpha
# 石头 random + 剪刀的概率 * alpha
# 石头 random + 剪刀的概率 * alpha

# # 总结
# 快速找到自己的问题，能找到优化的点，随机出拳，策略出拳。
# 不要给自己设限制。

# 增删查改
import random


x,y,z="石头","剪刀","布"
# 字典 键值对
# a = {
#     "1":"石头",
#     "2":"剪刀",
#     "3":"布",
#     "4":"exit",
# }
a =["石头","剪刀","布","exit"]

# history = [0, 0, 0]
history = []
for _ in range(3):
    history.append(0)
print(history)


p = random.random() * 3
q = int(p)

# for i in range(10):
i = 0
while i <= 10:
    player_input = input("请输入  " + str(a) + ":\n")
    if not player_input.isdigit():
        print('ERROR')
        continue
    else:
        player_input = int(player_input)
        if 0 <= player_input <= 3:
            if a[player_input] == "exit":
                print("end")
                break

            player = a[player_input]
            p = random.random() * 3
            q = int(p)
            computer = a[q]

            if (player == x and computer == y) or (player == y and computer == z) or (
                    player == z and computer == x):
                print("我出: " + player, "电脑出: " + computer, "结果是: win")
            elif player == computer:
                print("我出: " + player, "电脑出: " + computer, "结果是: peace")
            else:
                print("我出: " + player, "电脑出: " + computer, "结果是: lose")

            i += 1
        else :
            print('ERROR')

    # 把三种招式的input次数填进列表
    history[player_input] += 1
    print("玩家出拳历史记录", history)
