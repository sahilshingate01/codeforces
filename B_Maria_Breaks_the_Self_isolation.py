t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()  
    f = 0

    for i in range(n - 1, -1, -1):
        if arr[i] <= i + 1:
            f = 1
            print(i + 2)
            break

    if f == 0:
        print(1)