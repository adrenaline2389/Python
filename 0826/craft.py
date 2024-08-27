# 1.base work
w,x,y,z = 'exit','paper','scissors','rock'

import random

DEFEND = 0.6
FORGET = 0.1

a = [x,y,z,w]

history = []
for i in range(3):
    history.append(1e-8)
print(history)

journal = []
for i in range(3):
    journal.append(1e-8)
print(journal)

cp_pose = []
for i in range(3):
    cp_pose.append(0)

last_pose = -1

# 2.main task
for i in range(10):

    # 2.1 gain input
    player_input = input(str(a) + '请出招' + ':\n')

    # 2.2 distinguish between 'ERROR' and valid values
    if not player_input.isdigit():
        print('ERROR!!!')
        continue
    else :
        player_pose = eval(player_input)
        player = a[player_pose]
        if 0 <= player_pose <= 3:

            # 2.3 build an 'exit'
            if player == w:
                print('END')
                break

            # 2.4 function construction
            # # 2.4.1 introduce 'history' factor
            cp_pose[0] = random.random() + DEFEND * history[2] / sum(history)
            cp_pose[1] = random.random() + DEFEND * history[0] / sum(history)
            cp_pose[2] = random.random() + DEFEND * history[1] / sum(history)

            print(cp_pose)
            print(max(cp_pose),cp_pose.index(max(cp_pose)))

            # # 2.4.2 introduce 'FORGET' factor
            if last_pose != -1:
                if last_pose == 2:
                    cp_pose[0] -= FORGET
                else:
                    cp_pose[last_pose + 1] -= FORGET

            # 2.5 cp_pose probability
            print(cp_pose)
            cp = a[cp_pose.index(max(cp_pose))]

            # 3.1 output
            if (player == x and cp == z) or (player == y and cp == x) or (player == z and cp == y):
                print("我出: " + player, "电脑出: " + cp, "结果是: win")
                journal[0] += 1
            elif player == cp:
                print("我出: " + player, "电脑出: " + cp, "结果是:peace")
                journal[1] += 1
            else :
                print("我出: " + player, "电脑出: " + cp, "结果是:lose")
                journal[2] += 1
        else :
            print('ERROR!!!')

    # 3.2 result record
    history[player_pose - 1] += 1
    print("玩家出拳历史记录", history)
    print('玩家胜负记录：赢，平，输', journal)


# homework: 从最简单的版本开始默写