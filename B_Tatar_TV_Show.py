t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    s = input()
    possiabe = True

    for start in range(k):
        cnt = 0
        for i in range(start,n,k):
            if s[i] == "1":
                cnt += 1
            
        if cnt % 2 == 1:
            possiabe = False
            break

    print("YES" if possiabe else "NO")