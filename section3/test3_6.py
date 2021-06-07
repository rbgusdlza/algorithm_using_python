n = int(input())
board = []
max_sum = 0
for _ in range(n):
    board.append(list(map(int, input().split())))
# row sum
for row in board:
    val_sum = sum(row)
    if max_sum < val_sum:
        max_sum = val_sum
# col sum
for i in range(n):
    val_sum = 0
    for j in range(n):
        val_sum += board[j][i]
    if max_sum < val_sum:
        max_sum = val_sum
# diagonal sum
val_sum = 0
for i in range(n):
    val_sum += board[i][i]
if max_sum < val_sum:
    max_sum = val_sum
print(max_sum)
