
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    lo = arr[0]
    hi = arr[0]
    ans = arr[0]

    for i in range(1,n) :
        x = arr[i]
        ans = max(ans,x + abs(lo), x + abs(hi))

        lo = min(x, lo + x, 2 * lo + x)
        hi = max(x, hi + x, 2 * hi + x)

    print(ans)