t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    f = False
    for i in range(n - 2) :
        if arr[i] < arr[i + 1] and arr[i + 1] > arr[i + 2] :
            f = True
            print("YES")
            print(i + 1,i + 2,i + 3)
            break
    
    if not f :
        print("NO")