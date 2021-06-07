n = int(input())
score_li = list(map(int, input().split()))
mean = int(sum(score_li)/n + 0.5)
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

# another answer
'''
n = int(input())
a = list(map(int, input().split()))
ave = int(sum(a)/n + 0.5)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)
'''