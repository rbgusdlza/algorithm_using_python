a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        temp_row = ''
        temp_col = ''
        for k in range(5):
            temp_row += str(a[i][j+k])
            temp_col += str(a[j+k][i])
        if temp_row == temp_row[::-1]:
            cnt += 1
        if temp_col == temp_col[::-1]:
            cnt += 1
print(cnt)