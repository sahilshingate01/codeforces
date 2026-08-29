t = int(input())

def f(n):
    if n == 0:
        return

    f(n // 10)
    
    print(n % 10,end=" ")

for _ in range(t):
    n = int(input())
    if n == 0:
        print(0)
    else:
        f(n)
        print()
