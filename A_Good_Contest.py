t = int(input())

for _ in range(t):
    n = int(input())
    e,m,h = map(int,input().split())

    print(n - min(e,m,h))