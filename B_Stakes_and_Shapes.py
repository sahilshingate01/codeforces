t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    n = a + b + c
    k = (n + 1) // 2

    ans = ['R'] * n

    wins = 0

    x = min(a, k)
    for i in range(x):
        ans[i] = 'P'
    wins += x

    x = min(b, k - wins)
    for i in range(wins, wins + x):
        ans[i] = 'R'
    wins += x

    x = min(c, k - wins)
    for i in range(wins, wins + x):
        ans[i] = 'S'

    print(''.join(ans))