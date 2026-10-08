t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(input())

    res = []

    for i in range(n):
        j = i

        if i % 2 == 0:
            while s[j] != '(':
                j += 1
        else:
            while s[j] != ')':
                j += 1

        if i != j:
            res.append([i, j])

            s[i], s[j] = s[j], s[i]

    ans = n // 2
    i = 1

    while ans != k:
        res.append([i, i + 1])
        i += 2
        ans -= 1

    print(len(res))

    for op in res:
        print(op[0] + 1, op[1] + 1)