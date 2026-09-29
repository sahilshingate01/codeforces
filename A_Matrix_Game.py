t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    arr = []

    for i in range(n):
        arr.append(list(map(int, input().split())))

    row = {}
    col = {}
    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                row[i] = 1
                col[j] = 1
            
            
    for i in range(n) :
        for j in range(m) :
            if row.get(i,0) == 0 and col.get(j,0) == 0 :
                arr[i][j] = 1
                row[i] = 1
                col[j] = 1
                cnt += 1
            
    if cnt % 2 == 0 : print("Vivek")
    else : print("Ashish")

    