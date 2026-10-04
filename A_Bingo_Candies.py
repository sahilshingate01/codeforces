t = int(input())
 
for _ in range(t) :
    n = int(input())
    arr = []
 
    for _ in range(n) :
        arr.append(list(map(int,input().split())))
    
    freq = {}
    f = True
 
    for i in range(n) :
        for j in range(n) :
            x = arr[i][j]
            freq[x] = freq.get(x,0) + 1
 
            if freq[x] > (n * n) - n :
                f = False
                break
    
    if f : print("YES")
    else : print("NO")