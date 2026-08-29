t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(n - 1):
        t = arr[i]
        if arr[i] > arr[i + 1]:
            arr[i] = arr[i + 1]
            arr[i + 1] = t + arr[i + 1]

    print(arr[-1])
