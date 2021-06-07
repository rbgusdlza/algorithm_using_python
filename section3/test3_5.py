n, m = map(int, input().split())
a = list(map(int, input().split()))
i = 0
cnt = 0
while i < n:
    val_sum = 0
    for j in range(i, n):
        val_sum += a[j]
        if val_sum == m:
            cnt += 1
            break
        elif val_sum > m:
            break
    i += 1
print(cnt)

# another answer using 'two pointer' (O(N) algorithm)
'''
n, m = map(int, input().split())
a = list(map(int, input().split()))
lt = 0
rt = 1
tot = a[0]
cnt = 0
while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
'''