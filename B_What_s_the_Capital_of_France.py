t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    if len(set(arr)) == 1:
        print(arr[0])
    
    else :
        print(max(arr) + 1)