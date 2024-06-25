def longest_non_divisible_subarray(n, x, a):
    if sum(a) % x != 0:
        return n

    left = right = -1
    for i in range(n):
        if a[i] % x != 0:
            left = i
            break

    for i in range(n-1, -1, -1):
        if a[i] % x != 0:
            right = i
            break

    if left == -1 or right == -1:
        return -1

    return max(n - left - 1, right)



t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(longest_non_divisible_subarray(n, x, a))