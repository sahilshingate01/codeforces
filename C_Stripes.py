t = int(input())

for _ in range(t):
    arr = []
    ans = 'B'
    for i in range(9):
        row = input().strip()
        if row == 'RRRRRRRR' :
            ans = 'R'
    
    print(ans)

