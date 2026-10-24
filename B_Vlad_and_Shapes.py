t = int(input())

for _ in range(t) :
    n = int(input())

    arr = []
    for _ in range(n) :
        arr.append(list(map(int, input().strip())))

    ans = []
    for i in range(n) :
        cnt = 0
        for j in range(n) :
            if arr[i][j] == 1 :
                cnt += 1
        
        ans.append(cnt)

    if len(set(ans)) == 1 or len(set(ans)) == 2 :
        print('SQUARE')
    
    else :
        print('TRIANGLE')

