n = int(input())
score_li = list(map(int, input().split()))
mean = round(sum(score_li)/n)
gap = float('inf')
answer_idx = 0
for idx, score in enumerate(score_li):
    if abs(gap) >= abs(score - mean):
        if abs(gap) == abs(score - mean) and gap >= score - mean:
            continue
        else:
            gap = score - mean
            answer_idx = idx
print(mean, answer_idx+1)
