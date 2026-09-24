t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    freq = {}
    mx = 0
    op = 0

    for x in arr : 
        freq[x] = freq.get(x,0) + 1

        if freq[x] > mx :
            mx = freq[x]
    
