t = int(input())

for _ in range(t):
    n = int(input())
    ans = []

    for i in range(n):
        ans.append((n * 2) - i)

    print(*ans)