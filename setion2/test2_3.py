from itertools import combinations
n, k = map(int, input().split())
l = list(map(int, input().split()))
sum_li = list(map(sum, combinations(l, 3)))
sum_li = list(set(sum_li))
sum_li.sort(reverse=True)
print(sum_li[k-1])

# another answer
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])
'''