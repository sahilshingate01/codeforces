t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    total = sum(a)

    if total % 4 == 0:
        print("YES")
    else:
        print("NO")