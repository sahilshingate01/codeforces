t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    cnt = 0
    g = 0

    for x in arr :
        cnt += 1

        if cnt >= x :
            g += 1
            cnt = 0

    print(g)