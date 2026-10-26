t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    neg = arr.count(-1)

    ans = 0
    while neg > n // 2 or neg % 2 != 0 :
        neg -= 1
        ans += 1
    
    print(ans)