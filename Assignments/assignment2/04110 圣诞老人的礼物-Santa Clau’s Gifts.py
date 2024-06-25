N, W = map(int, input().split())
l = []

for i in range(N):
    l.append(list(map(int, input().split())))

for j in range(N):
    l[j].append(l[j][0]/l[j][1])

l_sorted = sorted(l,key=(lambda x:x[2]),reverse=True)

ans = 0

for i in range(N):
    if W >= l_sorted[i][1]:
        ans += l_sorted[i][0]
        W -= l_sorted[i][1]
    else:
        ans += l_sorted[i][2] * W
        break

print('%.1f' % ans)
