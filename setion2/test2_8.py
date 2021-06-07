def reverse(x):
    num = str(x)[::-1]
    num = int(num)
    return num

def isPrime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int((x**0.5)+1)):
            if x % i == 0:
                return False
        return True

n = int(input())
num_li = list(map(int, input().split()))
answer = []
for num in num_li:
    temp = isPrime(reverse(num))
    if temp == True:
        answer.append(reverse(num))
print(*answer)

# another answer about reverse func
'''
def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x = x // 10
    return res
'''