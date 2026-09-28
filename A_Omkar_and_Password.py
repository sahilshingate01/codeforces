t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))
    flag = True

    for i in range(1, n) :
        if arr[i - 1] != arr[i] :
            flag = False
            break

    if flag :
        print(n)
    
    else :
        print(1)