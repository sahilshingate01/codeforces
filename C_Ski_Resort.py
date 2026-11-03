t = int(input())

for _ in range(t) :
    n,k,q = map(int,input().split())
    arr = list(map(int,input().split()))

    cnt = 0
    ans = 0

    for i in range(n) :
        if arr[i] <= q :
            cnt += 1
        else :
            cnt = 0
        
        if cnt >= k :
            ans += cnt - k + 1

    print(ans)
