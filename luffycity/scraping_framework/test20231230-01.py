#写一个程序，输出100以内的所有偶数，直到累加和大于1000停止程序。

sum = 0
for i in range(0, 101):
    if i%2 ==0:
        if sum > 1000:
            break
        sum+=i
        print("输出偶数：" + str(i))
print("输出总和：" + str(sum))