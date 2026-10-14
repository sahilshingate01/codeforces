import math
t = int(input())

while t :
    n = int(input())
    arr = list(map(int,input().split()))

    last = [0] * 1001
    for i in range(n) :
        last[arr[i]] = i + 1
    
    ans = -1
    for x in range(1,1001) :
        for y in range(1,1001) :
            if last[x] != 0 and last[y] != 0 :
                if math.gcd(x,y) == 1 :
                    ans = max(ans,last[x] + last[y])

    print(ans)
    t -= 1