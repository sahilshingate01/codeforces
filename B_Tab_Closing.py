t = int(input())

while t :
    a,b,n = map(int,input().split())

    if b * n <= a or a == b :
        print(1)
    else :
        print(2)
    t -= 1
