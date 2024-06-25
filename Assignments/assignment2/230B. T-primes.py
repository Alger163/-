def prime():
    flag = [0] * (10 ** 6 + 1)
    for i in range(2):
        flag[i] = 1
    for i in range(2, 10 ** 6 + 1):
        if flag[i] == 0:
            for j in range(i * i, 10 ** 6 + 1, i):  # 原理上可行，可以节省时间
                flag[j] = 1
    return flag


n = int(input())
l = [int(x) for x in input().split()]
flags = prime()
for i in range(n):
    a = l[i] ** (1 / 2)
    if a % 1 != 0:
        print('NO')
    else:
        a = int(a)
        if flags[a] == 0:
            print('YES')
        else:
            print('NO')