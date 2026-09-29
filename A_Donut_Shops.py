t = int(input())

for _ in range(t) :
    a,b,c = map(int,input().split())

    shopA = -1
    shopB = -1

    if a < c : shopA = 1
    if (a * b) > c : shopB = b

    print(shopA,shopB)