import math

t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    ans = [1] * n 
    idx = arr.index(max(arr))
    ans[idx] = 2 
    
    if len(set(arr)) == 1 :
        print("NO")
    
    else :
        print("YES")
        print(*ans)