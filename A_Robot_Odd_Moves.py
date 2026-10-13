t = int(input())

for _ in range(t) :
    a,b = map(int,input().split())

    if (a % 2 == b % 2):          
        if b <= a:
            print(a)
        else:
            print(-1)
    else:                          
        if b <= a + 1:
            print(a + 1)
        else:
            print(-1)