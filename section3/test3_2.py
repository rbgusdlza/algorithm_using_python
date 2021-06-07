s = input()
num = ''
cnt = 0
for c in s:
    if c in '0123456789':
        num += c
num = int(num)
for i in range(1, num+1):
    if num % i == 0:
        cnt += 1
print(num)
print(cnt)

# another answer
'''
s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res*10 + int(x)
print(res)
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)
'''