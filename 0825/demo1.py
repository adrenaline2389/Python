# 伪代码：先给出3个变量，再获得用户的输入，电脑再从三个变量中随机选择一个

# 任务
# 1. 设计一个石头剪刀布游戏
# 2. input， if， 循环 break continue， = ==， and or的用法，字典和列表
# 3. if的优化（代码的重构）程序的健壮性 非法输入的处理
# 4. 自己想的优化点 电脑随机出拳（advantage：等概率直接取整，可以直接取数。

# 课后作业
# 电脑跟据我出拳的招式优化自己的策略

# 总结
# 杨猛的优点
# 快速找到自己的问题，能找到优化的点，随机出拳，策略出拳。
# 不要给自己设限制。

# 一些习惯可以去培养
# 1. 版本管理，记录自己每个版本的代码，方便回溯
# 2. 思考方式：正着思考想不通，试着反（从目标往前推）着思考

# 增删查改
import random

DEFEND = 0.6
FORGET = 0.1

x,y,z="石头","剪刀","布"
# 字典 键值对
# a = {
#     "1":"石头",
#     "2":"剪刀",
#     "3":"布",
#     "4":"exit",
# }
a = ["石头","剪刀","布","exit"]

# history = [0, 0, 0]
history = []
for _ in range(3):
    history.append(1e-8)
print(history)
print(history[1] / sum(history))

journal = []
for _ in range(3):
    journal.append(1e-8)
print(journal)

computer_posture = [0, 0, 0]

last_posture = -1

# for i in range(10):
i = 0
while i <= 10:
    # input 预处理
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

            # f(x)
            # 三个随机数
            # 玩家某个招式出的次数越多，电脑就越会克制
            computer_posture[0] = random.random() + DEFEND * history[1] / sum(history)
            computer_posture[1] = random.random() + DEFEND * history[2] / sum(history)
            computer_posture[2] = random.random() + DEFEND * history[0] / sum(history)

            print(computer_posture)
            print(max(computer_posture), computer_posture.index(max(computer_posture)))

            # # 玩家连续出
            if last_posture != -1:
                if last_posture == 0:
                    computer_posture[2] = computer_posture[2] - FORGET
                else:
                    computer_posture[last_posture - 1] -= FORGET

            # 电脑出拳概率
            print(computer_posture)
            computer = a[computer_posture.index(max(computer_posture))]

            # output 结果
            if (player == x and computer == y) or (player == y and computer == z) or (
                    player == z and computer == x):
                print("我出: " + player, "电脑出: " + computer, "结果是: win")
                journal[0] += 1
            elif player == computer:
                print("我出: " + player, "电脑出: " + computer, "结果是: peace")
                journal[1] += 1
            else:
                print("我出: " + player, "电脑出: " + computer, "结果是: lose")
                journal[2] += 1

            i += 1
            last_posture = player_input
        else :
            print('ERROR')

    # 把三种招式的input次数填进列表
    history[player_input] += 1
    print("玩家出拳历史记录", history)
    print('玩家胜负记录：赢，平，输',journal)
