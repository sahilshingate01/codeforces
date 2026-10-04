t = int(input())

for _ in range(t) :
    n = int(input())
    arr = []
    for _ in range(n) :
        arr.append(input())
    
    ans = []
    for i in reversed(arr) :
        col = i.index('#')
        ans.append(col + 1)
    
    print(*ans)

        