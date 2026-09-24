t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    cnt = 0
    m = min(arr)
    for x in arr:
        cnt += abs(m - x)

    print(cnt)