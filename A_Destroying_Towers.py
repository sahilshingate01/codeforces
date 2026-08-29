t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    total = 0

    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            arr[i + 1] = arr[i]
        total += arr[i]
    
    print(total + arr[-1])
