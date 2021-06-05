def reverse(x):
    num = str(x)[::-1]
    idx = 0
    for i, val in enumerate(num):
        if val == '0':
            continue
        else:
            idx = i
            break
    return int(num[idx:])

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