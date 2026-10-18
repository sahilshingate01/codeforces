t = int(input())

for _ in range(t) :
    n = int(input())

    t = n 
    a = 0
    while n % 2 == 0 :
        n //= 2
        a += 1
    
    b = 0
    while n % 3 == 0 :
        n //= 3
        b += 1

    if n != 1 :
        print(-1)
    
    elif a <= b :
        print((b - a) + b)
    
    else :
        print(-1)
