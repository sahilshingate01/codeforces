t = int(input())

for _ in range(t) :
    a,b = map(int,input().split())

    if a - b == 0 :
        print(0)

    else :
        diff = abs(a - b)
        d = diff // 10
        if diff % 10 > 0 :
            d += 1
        print(d)
        
        