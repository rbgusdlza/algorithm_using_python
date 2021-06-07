import sys
#sys.stdin = open("input.txt", "rt")

t = int(input())
for i in range(t):
    n, s, e, k = map(int, input().split())
    num_li = list(map(int, input().split()))
    l = num_li[s-1:e]
    l.sort()
    print('#%d %d' % (i+1, l[k-1]))
