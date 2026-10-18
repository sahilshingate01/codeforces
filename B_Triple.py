t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    freq = {}
    ans = -1

    for x in arr :
        freq[x] = freq.get(x,0) + 1

        if freq[x] >= 3 :
            ans = x
            break
    
    print(ans)