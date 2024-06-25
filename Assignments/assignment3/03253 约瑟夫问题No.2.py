def josephus(n, p, m):
    children = list(range(1, n + 1))
    result = []

    idx = p - 1  # 初始化起始位置
    while children:
        idx = (idx + m - 1) % len(children)  # 计算当前报数位置
        result.append(children.pop(idx))     # 移除当前位置的小孩并记录编号

    return result

output = []
while True:
    n, p, m = map(int, input().split())
    if n == 0 and p == 0 and m == 0:
        break
    output.append(josephus(n, p, m))

for i in output:
    print(",".join(map(str, i)))
