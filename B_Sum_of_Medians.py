t = int(input())

for _ in range(t) :
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    ans = 0
    i = n * k 

    while k :
        i -= (n // 2) + 1
        ans += arr[i]
        k -= 1
    
    print(ans)