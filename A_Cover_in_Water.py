t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    cnt = 0
    total = 0

    for water in s:
        if water == '.':
            cnt += 1
            total += 1
            
        else:
            cnt = 0

        if cnt > 2:
            total = 2
            break
        
    print(total)