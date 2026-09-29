t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))
    


    arr.sort()
    possable = True

    for i in range(1,n) :
        if abs(arr[i - 1] - arr[i]) > 1 :
            possable = False
            break
    
    if possable : print("YES")
    else : print("NO")