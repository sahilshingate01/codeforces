t = int(input())

for _ in range(t) :
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))

    mi = (sum(arr) + x - 1) // x
    mx = 0

    for v in arr :
        mx += (v + x - 1) // x
    
    print(mi,mx)
