from itertools import combinations
n, k = map(int, input().split())
l = list(map(int, input().split()))
sum_li = list(map(sum, combinations(l, 3)))
sum_li = list(set(sum_li))
sum_li.sort(reverse=True)
print(sum_li[k-1])