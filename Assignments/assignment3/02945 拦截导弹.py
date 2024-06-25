def max_interception(k, heights):
    dp = [1] * k
    for i in range(1, k):
        for j in range(i):
            if heights[i] <= heights[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

k = int(input())
l = list(map(int, input().split()))
print(max_interception(k, l))