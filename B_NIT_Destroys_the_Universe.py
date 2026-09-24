t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    curr = 0
    op = 0

    for i in range(n) :
        
        if arr[i] != 0 : curr += 1
        else : curr = 0

        if curr == 1 : op += 1
        if op >= 2 : break

    print(min(2,op))