n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
mid = n//2
val_sum = 0
for i in range(mid+1):
    val_sum += sum(board[i][mid-i:mid+i+1])
lt = 1
rt = n-2
for i in range(mid+1, n):
    val_sum += sum(board[i][lt:rt+1])
    lt += 1
    rt -= 1
print(val_sum)

'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = e = n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)
'''