n = int(input())

def prime_or_not():
    L = []
    for num in range(1,5000):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                L.append(num)
    return L

if n % 2 == 1:
    print('2 '+str(n-2))
else:
    for x in prime_or_not():
        if n-x in prime_or_not():
            print(str(x)+' '+str(n-x))
            break
