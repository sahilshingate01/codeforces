t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))
    
    if n == 2 :
        print(abs(arr[0] - arr[1]))
    
    else :
        freq = {}
        havedouble = False
        
        for x in arr :
            freq[x] = freq.get(x,0) + 1
            if freq[x] > 1 : 
                havedouble = True
                break
        
        if havedouble : print(0) 
        else :
            mi = 100000000

            for i in range(n) :
                for j in range(i + 1,n) :
                    if abs(arr[i] - arr[j]) < mi :
                        mi = abs(arr[i] - arr[j])
                    
            print(mi)
            
                

        
