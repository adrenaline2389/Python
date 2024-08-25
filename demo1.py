#先给出3个变量，再获得用户的输入，电脑再从三个变量中随机选择一个
x,y,z="石头","剪刀","布"
# for i in range(3):
i = 0
while i <=2:


    player=input("请输入:")
    computer=z

    if (player == x and computer == y) or (player == y and computer == z) or (player == z and computer == x):
        print('win')
    elif player==computer:
        print('peace')
    else :
        print('lose')

    i = i + 1