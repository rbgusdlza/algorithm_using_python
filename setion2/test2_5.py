from collections import Counter
n, m = map(int, input().split())
n_num = list(range(1, n+1))
m_num = list(range(1, m+1))
sum_set = []
answer = []
for i in n_num:
    for j in m_num:
        sum_set.append(i+j)
cnt_li = Counter(sum_set).most_common()
num = cnt_li[0][1]
for i, j in cnt_li:
    if j == num:
        answer.append(i)
answer.sort()
print(*answer)

# another answer
'''
n, m = map(int, input().split())
cnt = [0] * (n+m+3)
max = -2147000000
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end = ' ')
'''