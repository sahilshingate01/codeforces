t = int(input())

for _ in range(t):
    n = int(input())

    if n % 3 != 0:
        print(3 - (n % 3))
    else:
        print(0)
