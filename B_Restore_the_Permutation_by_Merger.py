t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    arr = list(set(arr))
    print(*arr)