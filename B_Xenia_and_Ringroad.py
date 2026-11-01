n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
curr = 1

for x in arr :
    if x >= curr :
        ans += x - curr
    else :
        ans += n - curr + x
    
    curr = x
    
print(ans)