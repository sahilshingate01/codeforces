t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))


    l = -1
    r = -1
    cnt = 0

    for i in range(n) :
        if arr[i] == 1 :
            l = i
            break
        
    for i in range(n - 1,-1,-1) :
        if arr[i] == 1:
            r = i
            break
        
    for i in range(l , r + 1) :
        if arr[i] == 0 :
            cnt += 1

    print(cnt)