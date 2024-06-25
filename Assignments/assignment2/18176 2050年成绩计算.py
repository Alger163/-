def prime():
    flag = [0] * (10 ** 4 + 1)
    for i in range(2):
        flag[i] = 1
    for i in range(2, 10 ** 4 + 1):
        if flag[i] == 0:
            for j in range(i * i, 10 ** 4 + 1, i):  # 原理上可行，可以节省时间
                flag[j] = 1
    return flag

prime_flag = prime()

m, n = map(int, input().split())
for _ in range(m):
    l = list(map(int, input().split()))
    points = 0
    for i in range(len(l)):
        a = l[i] ** (1 / 2)
        if a % 1 == 0:
            a = int(a)
            if prime_flag[a] == 0:
                points += l[i]
    if points == 0:
        print('0')
    else:
        print('%.2f' % (points/len(l)))