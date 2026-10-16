t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    s = set()

    def f(idx,ds) :
        if idx == n :
            s.add(tuple(ds))
            return
        
        ds.append(arr[idx])
        f(idx + 1,ds)
        ds.pop()
        f(idx + 1,ds)
    
    f(0,[])
    print(len(s))


    #this was not completed qestion 