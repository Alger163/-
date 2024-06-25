def arrange_experiment(n, durations):
    # 将学生按照实验时长从短到长进行排序
    sorted_durations = sorted(enumerate(durations, start=1), key=lambda x: x[1])
    order = [student[0] for student in sorted_durations]  # 学生的实验顺序
    total_wait_time = 0
    for i in range(len(durations)):
        total_wait_time += sorted_durations[i][1] * (n - i - 1)  # 计算总等待时间
    avg_wait_time = total_wait_time / n  # 计算平均等待时间
    return order, avg_wait_time

n = int(input())
durations = list(map(int, input().split()))

order, avg_wait_time = arrange_experiment(n, durations)
print(" ".join(map(str, order)))
print("%.2f" % avg_wait_time)
