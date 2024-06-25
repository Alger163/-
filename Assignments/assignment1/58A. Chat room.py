s = input()
L = []
for i in s:
    if i == 'h':
        if 1 not in L:
            L.append(1)
    elif i == 'e' and L == [1]:
        if 2 not in L:
            L.append(2)
    elif i == 'l' and 1 in L and 2 in L:
        if 3 not in L:
            L.append(3)
        elif 4 not in L:
            L.append(4)
    elif i == 'o' and L == [1, 2, 3, 4]:
        if 5 not in L:
            L.append(5)

if L == [1,2,3,4,5]:
    print('YES')
else:
    print('NO')