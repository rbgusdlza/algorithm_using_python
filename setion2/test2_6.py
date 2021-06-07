def digit_sum(x):
    x_sep = list(str(x))
    x_sum = 0
    for i in x_sep:
        x_sum += int(i)
    return x_sum
    
n = int(input())
num_li = list(map(int, input().split()))
max_sum = -1
for num in num_li:
    k = digit_sum(num)
    if max_sum < k:
        max_sum = k
        answer = num
print(answer)

# another answer
'''
a = list(map(int, input().split()))
def digit_sum(x):
    sum = 0
    while x > 0:
        sum += x % 10
        x = x // 10
    return sum
max = -2147000000
for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)
'''
