import math

t = int(input())

for _ in range(t) :
    a,b = map(int,input().split())

    d = abs(a - b)
    
    if d == 0 :
        print(0,0)
        continue
    
    move = min(a % d, (d - a % d))

    print(d,move)