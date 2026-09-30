t = int(input())

for _ in range(t):
    a, b, x, y, n = map(int, input().split())

    da = min(n, a - x)
    new_a = a - da

    remaining = n - da
    db = min(remaining, b - y)
    new_b = b - db

    ans1 = new_a * new_b

    db = min(n, b - y)
    new_b = b - db

    remaining = n - db
    da = min(remaining, a - x)
    new_a = a - da

    ans2 = new_a * new_b

    print(min(ans1, ans2))