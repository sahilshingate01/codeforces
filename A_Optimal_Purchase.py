t = int(input())

for _ in range(t):
    n,a,b = map(int,input().split())

    if n <= 3:
        if n * a < b:
            print(n * a)
        else:
            print(b)
    else:

        if (n // 3) * b + (n % 3) * b < n * a:
            print((n // 3) * b + (n % 3) * b)

        elif (n // 3) * b + (n % 3) * a > (n * a):
            print((n * a))

        else:
            print((n // 3) * b + (n % 3) * a)
    


