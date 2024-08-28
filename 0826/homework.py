# base work
import random

x, y, z = 'paper', 'scissors', 'rock'

a = ['paper', 'scissors', 'rock']

cp_pose = [0, 0, 0]

for i in range(10):
    # gain input
    player_input = input('请出拳：' + str(a))
    player = a[eval(player_input)]

    # computer
    cp_pose[0] = random.random()
    cp_pose[1] = random.random()
    cp_pose[2] = random.random()

    cp = a[cp_pose.index(max(cp_pose))]

    # output
    if (player == x and cp == y) or (player == y and cp == z) or (player == z and cp == x):
        print("我出: " + player, "电脑出: " + cp, "结果是: win")
    elif player == cp:
        print("我出: " + player, "电脑出: " + cp, "结果是: peace")
    else:
        print("我出: " + player, "电脑出: " + cp, "结果是: lose")