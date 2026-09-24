t = int(input())

for _ in range(t) :
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))

    arr.sort()

    best = 1
    curr = 1

    for i in range(1,n):
        if arr[i] - arr[i - 1] <= k : curr += 1
        else : curr = 1

        best = max(best,curr)
    
    print(n - best)

