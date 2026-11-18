t = int(input())

for _ in range(t) :
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1,n) :
        prefix[i] = (prefix[i - 1] + arr[i]) // (i + 1)
    
    cnt = 0
    pleasnt = []
    temp = []

    for i in range(n) :
        if arr[i] <= prefix[i] :
            cnt += 1
            pleasnt.append(arr[i])
        else :
            temp.append(arr[i])
        
    if k == cnt :
        print("YES")
        print(*pleasnt + temp)
    else :
        print("NO")
    # print(cnt)
