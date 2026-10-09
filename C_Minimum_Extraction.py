t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = arr[0]
    for i in range(1,n) :
        ans = max(ans,arr[i] - arr[i - 1])
    
    print(ans)