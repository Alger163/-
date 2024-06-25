n = int(input())
T=[0,1,1]
if n > 2:
    for i in range(3,n+1):
        T.append(int(T[i-1]+T[i-2]+T[i-3]))
print(T[-1])