t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = int(input())

    prev = -10**18

    for x in a:
        y = b - x

        if x >= prev and y >= prev:
            prev = min(x, y)

        elif x >= prev:
            prev = x

        elif y >= prev:
            prev = y

        else:
            print("NO")
            break
    else:
        print("YES")