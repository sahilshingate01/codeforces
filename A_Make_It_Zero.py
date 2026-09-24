t = int(input())
for _ in range(t):
    n = int(input())
    input()  # input mat lena hulala
    if n % 2 == 0:
        print(2)
        print(1, n)
        print(1, n)
    else:
        print(4)
        print(1, n)
        print(1, n - 1)
        print(n - 1, n)
        print(1, n)