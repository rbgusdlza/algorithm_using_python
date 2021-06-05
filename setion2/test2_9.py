from collections import Counter
n = int(input())
max_score = -1
for _ in range(n):
    dice = list(map(int, input().split()))
    cnt = Counter(dice).most_common(1)
    if cnt[0][1] == 1:
        score = max(dice) * 100
    elif cnt[0][1] == 2:
        score = cnt[0][0] * 100 + 1000
    elif cnt[0][1] == 3:
        score = cnt[0][0] * 1000 + 10000
    if score > max_score:
        max_score = score
print(max_score)
