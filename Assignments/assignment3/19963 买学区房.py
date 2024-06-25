def distance_to_school(x, y):
    return abs(x) + abs(y)


def house_worth_buying(houses, prices):
    n = len(houses)
    distances = [distance_to_school(x, y) for x, y in houses]
    ratios = [distances[i] / prices[i] for i in range(n)]

    if n % 2 == 0:
        median_ratio = (sorted(ratios)[n // 2 - 1] + sorted(ratios)[n // 2]) / 2
        median_price = (sorted(prices)[n // 2 - 1] + sorted(prices)[n // 2]) / 2
    else:
        median_ratio = sorted(ratios)[n // 2]
        median_price = sorted(prices)[n // 2]

    worth_buying = 0
    for i in range(n):
        if ratios[i] > median_ratio and prices[i] < median_price:
            worth_buying += 1

    return worth_buying


# 读取输入
n = int(input())
houses = [tuple(map(int, s.strip('()').split(','))) for s in input().split()]
prices = list(map(int, input().split()))

# 计算值得买的房子数目并输出结果
print(house_worth_buying(houses, prices))
