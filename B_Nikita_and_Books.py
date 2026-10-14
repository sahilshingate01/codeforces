t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    for i in range(1,n) :
        if arr[i - 1] >= arr[i] :
            while arr[i - 1] >= arr[i] and arr[i - 1] != 1 and arr[i] != 1: 
                arr[i - 1] -= 1
                arr[i] += 1
    
    if arr == sorted(arr) :
        print("YES")
    else : print("NO")

