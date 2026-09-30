t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    if x == 0 and y == 0 :
        print(0) 
    
    elif (2 * a) <= b :
        print((x + y) * a)
    
    else :
        common = min(x,y)
        remaining = abs(x - y)

        print((common * b) + (remaining * a))