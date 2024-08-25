#先给出3个变量，再获得用户的输入，电脑再从三个变量中随机选择一个
x,y,z="石头","剪刀","布"
player=input("请输入:")
computer=z

if player!=computer:
    if player == x:
        if computer == y:
            print("赢")
        if computer == z:
            print("输")
    elif player == y:
        if computer == x:
            print("输")
        if computer == z:
            print("赢")
    else:
        if computer == x:
            print("赢")
        if computer == y:
            print("输")
else :
    print('平')


