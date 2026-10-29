t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # cnt = [0] * (n + 2)

    # for x in arr:
    #     cnt[x] += 1

    # ans = 0
    # prefix = 0
    
    # for v in range(n + 1):
    #     prefix += cnt[v]
    #     if cnt[v] >= 1 and prefix >= k * (v + 1):
    #         ans = v + 1
    #     else:
    #         break
    # print(ans)


