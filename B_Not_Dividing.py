t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(n) : arr[i] += 1
    
    for i in range(1,n) :
        if arr[i] % arr[i - 1] == 0 : arr[i] += 1

    print(*arr)
    

