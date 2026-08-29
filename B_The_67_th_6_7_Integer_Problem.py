t = int(input())

for _ in range(t):
    arr = list(map(int,input().split()))
    dupmax = False
    total = 0
    for i in range(7):
        if arr[i] == max(arr) and not dupmax:
            total += arr[i]
            dupmax = True
        else:
            total += -1 * (arr[i])
    print(total)