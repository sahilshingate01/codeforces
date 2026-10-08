t = int(input())

for _ in range(t) :
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort(reverse=True)

    ans = arr[0]
    for i in range(1,k + 1) :
        ans += arr[i]
        arr[i] = 0
    
    print(ans)