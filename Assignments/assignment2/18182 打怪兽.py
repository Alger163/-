nCases = int(input())
ans = []

for i in range(nCases):
    n, m, b = map(int, input().split())
    skills = {}
    for j in range(n):
        t, x = map(int, input().split())
        if t not in skills.keys():
            skills[t] = [x]
        else:
            skills[t].append(x)
    skills_time = sorted(skills)

    for j in skills_time:
        skills[j].sort(reverse=True)
        if m >= len(skills[j]):
            b -= sum(skills[j])
        else:
            b -= sum(skills[j][0:m])

        if b <= 0:
            ans.append(str(j))
            break

    if b > 0:
        ans.append('alive')
print('\n'.join(ans))