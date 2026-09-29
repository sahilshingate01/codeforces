t = int(input())

for _ in range(t) :
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    b.sort(reverse=True)

    for i in range(k) :
        mi = min(a)
        miidx = a.index(mi)

        if b[i] > mi :
            a[miidx],b[i] = b[i],a[miidx]
    
    print(sum(a))