t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()

    t = []
    freq = {}
    ans = []

    for x in arr :
        freq[x] = freq.get(x,0) + 1
    
        if freq[x] > 1 : t.append(x)
        else :
            ans.append(x)

    ans.extend(t)
    
    print(*ans)