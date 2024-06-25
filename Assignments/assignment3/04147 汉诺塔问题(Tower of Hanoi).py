def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"{n}:{source}->{target}")
    else:
        hanoi(n-1, source, target, auxiliary)
        print(f"{n}:{source}->{target}")
        hanoi(n-1, auxiliary, source, target)

n, A, B, C = input().split()
n = int(n)
hanoi(n, A, B, C)
