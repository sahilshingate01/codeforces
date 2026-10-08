t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    v = []
    freq = {}

    for i in range(n - 4) :
        c = arr[i] + arr[i + 2] - arr[i + 4]
        v.append(c)
        freq[c] = freq.get(c,0) + 1
    
    