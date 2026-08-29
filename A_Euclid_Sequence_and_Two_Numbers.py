t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort(reverse=True)

    if n == 2:
        if arr[0] >= arr[1]:
            print(*arr)
        else:
            print(-1)
    
    else:
        found = True
        for i in range(n - 2):
            if arr[i] % arr[i + 1] != arr[i + 2]:
                found = False
                break
        if found:
            print(arr[0],arr[1])
        else:
            print(-1)
        
    
