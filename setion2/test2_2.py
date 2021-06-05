import sys
#sys.stdin = open("input.txt", "rt")

t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    num_li = list(map(int, input().split()))
    l = num_li[s-1:e]
    l.sort()
    print('#' + str(i+1) + ' ' + str(l[k-1]))
