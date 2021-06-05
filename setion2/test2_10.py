n = int(input())
score_li = list(map(int, input().split()))
cnt = 0
total = 0
for score in score_li:
    if score == 1:
        cnt += 1
        total += cnt
    else:
        cnt = 0
print(total)
