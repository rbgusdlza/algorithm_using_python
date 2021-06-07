a = [list(map(int, input().split())) for _ in range(9)]
# check row
flag1 = False
check = list(range(1, 10))
for i in range(9):
    if sorted(a[i]) != check:
        break
else:
    flag1 = True
# check col
flag2 = False
if flag1:
    flag2 = True
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(a[j][i])
        if sorted(temp[:]) != check:
            flag2 = False
            break
# check box
flag3 = False
if flag2:
    flag3 = True
    crd = [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]
    steps = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (0, 0)]
    for x, y in crd:
        temp = []
        for dx, dy in steps:
            temp.append(a[x+dx][y+dy])
        if sorted(temp[:]) != check:
            flag3 = False
            break
if flag3:
    print('YES')
else:
    print('NO')
