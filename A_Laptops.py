n = int(input())
f = True

while n :
    a,b = map(int,input().split())
    if a > b :
        f = False

    n -= 1

if not f :
    print('Happy Alex')
else : print("Poor Alex")


