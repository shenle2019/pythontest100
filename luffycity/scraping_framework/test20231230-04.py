### 猜数字游戏设计：可以不间断的进行猜数字游戏环节，找到猜对了，结束程序，猜不对，可以不断的进行游戏，并且需要提示用户猜打了还是猜小了。
### - 最后需要统计出，用户猜了多少次才猜对。
### - 每一个用户的初始分数为100，每猜错一次扣5分，最后程序结束，统计用户的得分

import random
guess_num = random.randint(0, 10)
count_num = 0
score = 100
while True:
    num = int(input("请输入数字："))
    count_num +=1
    if num == guess_num:
        print('猜对了')
        break
    elif num < guess_num:
        print('猜小了')
        score-=5
    else:
        print('猜大了')
        score-=5

    if score==0:
        print('分数等于0')
        break

print('猜测次数：' + str(count_num))
print('猜测分数：' + str(score))