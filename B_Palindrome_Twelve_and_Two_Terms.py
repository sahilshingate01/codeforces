pal = [0,1,2,3,4,5,6,7,8,9,22,11]

t = int(input())

for _ in range(t):
    n = int(input())

    a = pal[n % 12]

    if a > n:
        print(-1)
    else:
        print(a, n - a)