t = int(input())
ans = 0

for _ in range(t):
    arr = list(map(int,input().split()))
    c = 0

    for x in arr:
        if x == 1:
            c += 1
    
    if c >= 2:
        ans += 1
    
print(ans)
