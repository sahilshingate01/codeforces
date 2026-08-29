t = int(input())

def f(n):
    if n == 0:
        return 

    f(n // 2)

    print(n % 2,end="")


for _ in range(t):
    n = int(input())
    f(n)
    print()
