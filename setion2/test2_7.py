n = int(input())
ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i+i, n+1, i):
            ch[j] = 1
print(cnt)

#if we should find the prime 'number' between 0 and N, then
'''
n = int(input())
ch = [0] * (n+1)
res = []
for i in range(2, n+1):
    if ch[i] == 0:
        res.append(i)
        for j in range(i, n+1, i):
            ch[j] = 1
print(*res)
'''

# if we should figure out that given N is prime number or not, then
n = int(input())
flag = False
if n != 1:
    for i in range(2, int(n**(0.5)+1)):
        if n % i == 0:
            break
    else:
        flag = True
print(flag)
