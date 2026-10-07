t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))
    cnt = 0

    for i in range(n) :
        for j in range(i + 1,n) :
            if j + 4 < n :
                x = ((arr[i] + arr[i + 2]) - arr[i + 4])
                y = ((arr[j] + arr[j + 2]) - arr[j + 4])
                
                if x == y : cnt += 1
                
            else :
                pass 
            
    print(cnt)