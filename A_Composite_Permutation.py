
def solve():
    n = int(input())

    if n < 4 :
        print(-1)
    else:
        print(4, 2, 3, 1, end=" ")
        for i in range(5, n + 1):
            print(i, end=" ")
        print()


t = int(input())

for _ in range(t):
    solve()
