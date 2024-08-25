#先给出3个变量，再获得用户的输入，电脑再从三个变量中随机选择一个
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

# 设计电脑出的招式是等概率的
p = random.random()*3
q = int(p)
# for i in range(3):
i = 0
while i <= 10:
    player_input = input("请输入  " + str(a) + ":\n")
    if not player_input.isdigit():
        print('ERROR')
        continue
    else:
        player_input = int(player_input)
        if player_input <= 3 and player_input >= 0:
            if a[player_input] == "exit":
                print("end")
                break

            player = a[player_input]
            p = random.random() * 3
            q = int(p)
            if q == 0:
                computer = x
            if q == 1:
                computer = y
            if q == 2:
                computer = z

            if (player == x and computer == y) or (player == y and computer == z) or (
                    player == z and computer == x):
                print("我出: " + player, "电脑出: " + computer, "结果是: win")
            elif player == computer:
                print("我出: " + player, "电脑出: " + computer, "结果是: peace")
            else:
                print("我出: " + player, "电脑出: " + computer, "结果是: lose")

            i = i + 1
        else:
            print('ERROR')