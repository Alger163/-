def find_min_integer(n, k, sequence):
    # 对序列进行排序
    sequence.sort()

    # 如果第 k 个元素存在且不是序列中的最后一个元素，则返回第 k 个元素
    if k > 0 and k <= n:
        if k+1 <=n and sequence[k] > n:
            return sequence[k - 1]
    # 如果第 k 个元素不存在，则返回 -1
        else:
            return -1


# 读取输入
n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# 调用函数并输出结果
print(find_min_integer(n, k, sequence))
