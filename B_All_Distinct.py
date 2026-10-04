t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    arr = set(arr)

    if n % 2 != 0 : print(len(arr) - 1)
    else : print(len(arr))

