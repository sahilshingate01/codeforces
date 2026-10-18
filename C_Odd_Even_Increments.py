t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    odd_parity = a[0] % 2
    even_parity = a[1] % 2

    possible = True

    for i in range(n):
        if i % 2 == 0 and a[i] % 2 != odd_parity:
            possible = False
        if i % 2 == 1 and a[i] % 2 != even_parity:
            possible = False

    print("YES" if possible else "NO")
