t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    cnt = 0
    mi = min(arr)

    for i in range(n) :
        if arr[i] == mi : cnt += 1
    
    print(n - cnt)
