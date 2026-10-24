t = int(input())

for _ in range(t) :
    q = int(input())

    ans = 0
    for _ in range(q) :
        n = int(input())
        arr = list(map(int,input().split()))

        ans += min(arr)
    
    print(ans)
