t = int(input())

for _ in range(t) :
    n ,p = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    ans = 0
    idx = a.index(max(a))
    