t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort(reverse=True)
    ans = 0
    cnt = 0

    for a in arr :
        cnt += 1

        if a * cnt >= x :
            ans += 1
            cnt = 0
    
    print(ans)