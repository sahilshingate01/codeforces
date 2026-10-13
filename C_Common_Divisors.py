import math

n = int(input())
arr = list(map(int, input().split()))

g = 0
for x in arr:
    g = math.gcd(g, x)

cnt = 0
i = 1
while i * i <= g:
    if g % i == 0:
        cnt += 1
        if i != g // i:
            cnt += 1
    i += 1

print(cnt)