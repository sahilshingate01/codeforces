t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    op = 0
    isPossiable = True

    for i in range(n - 2, -1, -1) :
        
        while arr[i] >= arr[i + 1] :

            if arr[i] == 0 :
                isPossiable = False
                break
            
            arr[i] //= 2
            op += 1
        
        if not isPossiable :
            break
    
    if isPossiable : print(op)
    else : print(-1)