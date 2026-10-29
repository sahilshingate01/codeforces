t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    # p = n - k + 1
    # s = set(a[:p])
    # m = 0

    # while m in s:
    #     m += 1
    # if m == p:
    #     print(-1)
    # else:
    #     pos = a.index(m) + 1
    #     for i in range(p):
    #         if a[i] >= p:
    #             print(i + 1, pos)
    #             break