n = int(input())
for i in range(1, n+1):
    string = input().lower()
    if string == string[::-1]:
        answer = 'YES'
    else:
        answer = 'NO'
    print('#%d %s'%(i, answer))

# another answer
'''
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" % (i+1))
'''
