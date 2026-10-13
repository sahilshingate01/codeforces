t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    cnt = [0] * (n + 2)
    for x in arr:
        cnt[x] += 1

    ans = "NO"
    for x in range(n + 1):          
        if cnt[x] == 2 * k - 1:     
            ans = "YES"
            break
        if cnt[x] < 2 * k - 1:      
            break

    print(ans)