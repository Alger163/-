l = input().split()
l.sort()
times = {}
nums = []

for i in l:
    if i not in times:
        times[i] = 0
    nums.append(i)
    times[i] += 1


sorted_times = sorted(times.items(), reverse=True, key=lambda x:x[1])


output = []
for x in range(len(sorted_times)):
    if sorted_times[x][1] >= sorted_times[x-1][1]:
        output.append(int(sorted_times[x][0]))
    else:
        break

output.sort()
print(' '.join(str(x) for x in output))