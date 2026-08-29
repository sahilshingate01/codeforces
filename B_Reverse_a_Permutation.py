t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    maxidx = arr.index(max(arr))

    for i in range(n):
        if arr[i] != arr[maxidx]:
            l = min(i, maxidx)
            r = max(i, maxidx)

            arr[i], arr[maxidx] = arr[maxidx], arr[i]
            arr[l:r + 1] = arr[l:r + 1][::-1]
            break

    print(*arr)

