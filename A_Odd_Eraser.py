from math import gcd

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    #this is checking is this wroking or not
    print(gcd(arr[0],arr[-1]))
            