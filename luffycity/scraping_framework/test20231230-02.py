### 已知a+b+c=1000且a^2+b^2=c^2(a,b,c都是自然数)，求出符合条件的a,b,c的所有组合。

for a in range(0,1001):
    for b in range(0, 1001):
        c= 1000 - a - b
        #if a+b+c==1000 & a^2+b^2==c^2:这里已经能够保证a+b+c=1000了，所以不用再写。
        if a*a + b*b== c*c:
            print(a,b,c)
