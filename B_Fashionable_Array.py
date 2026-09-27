t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    cnt = {}
    for x in a:
        cnt[x] = cnt.get(x,0) + 1

    maxc = 0
    for x in cnt:
        if cnt[x] > maxc:
            maxc = cnt[x]

    result = []
    k = 1
    
    while k <= maxc:
        layer = []
        for x in cnt:
            if cnt[x] >= k:
                layer.append(x)
        layer.sort(reverse=True)
        result += layer
        k += 1

    print(*result)