t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    isCont = False

    for i in range(1,n) :
        if arr[i - 1] != arr[i] :
            isCont = True
            break

    if isCont : print(sum(arr))
    else : 
        if n == 1 : print(arr[0])
        else : print(arr[0] * 2)
    