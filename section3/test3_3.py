row = list(range(1, 21))
for _ in range(10):
    a, b = list(map(int, input().split()))
    if a != 1:
        row[a-1:b] = row[b-1:a-2:-1]
    else:
        row[a-1:b] = row[b-1::-1]
print(*row)

# another answer
'''
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
print(*a)
'''