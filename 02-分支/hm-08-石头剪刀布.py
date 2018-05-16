import random

player = int(input("请输入石头（1）剪刀（2）布（3）"))

computer = random.randint(1, 3)

if player == computer:
    print("player %d computer %d" % (player, computer))
    print("平局")
elif ((player == 1 and computer == 2)
      or (player == 2 and computer == 3)
      or (player == 3 and computer == 1)):
    print("player %d computer %d" % (player, computer))
    print("电脑弱爆了！")
else:
    print("player %d computer %d" % (player, computer))
    print("你个弱鸡！")
