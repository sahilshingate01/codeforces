t = int(input())

for _ in range(t) :
    n ,m = map(int,input().split())
    arr = []

    for _ in range(n):
        arr.append(list(input()))
        
    cnt = 0

    for i in range(n) :
        for j in range(m) :
            if i == n - 1 :
                if arr[i][j] == 'D' :
                    cnt += 1
            
            if j == m - 1 :
                if arr[i][j] == 'R' :
                    cnt += 1
                
    print(cnt)
