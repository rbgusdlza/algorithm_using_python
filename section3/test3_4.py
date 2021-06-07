n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1, p2 = 0, 0
c = []
while True:
    if p1 == n:
        c += b[p2:]
        break
    elif p2 == m:
        c += a[p1:]
        break
        
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
print(*c)