t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()

    t = []
    freq = {}
    ans = []

    for i in range(n) :
        freq[arr[i]] = freq.get(arr[i],0) + 1
    
        if freq[arr[i]] > 1 : t.append(arr[i])
        else :
            ans.append(arr[i])

    for i in range(len(t)) :
        ans.append(t[i])
    
    print(*ans)