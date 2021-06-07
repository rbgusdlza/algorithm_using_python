n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
command = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    row, course, cnt = command[i]
    temp = [0] * n
    for j in range(n):
        if course == 0:
            temp[j-(cnt%n)] = a[row-1][j]
        else:
            temp[(j+cnt)%n] = a[row-1][j]
    a[row-1][:] = temp[:]

val_sum = 0
s = 0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        val_sum += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(val_sum)
