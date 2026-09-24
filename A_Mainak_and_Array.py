t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    ans = arr[-1] - arr[0]
    #hi
    for i in range(n - 1) :
        ans = max(ans,arr[i] - arr[0])
        ans = max(ans,arr[-1] - arr[i + 1])
        ans = max(ans,arr[i] - arr[i + 1])
    
    print(ans)