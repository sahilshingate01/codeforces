import math

t = int(input())

while t :
    n = int(input())
    arr = list(map(int,input().split()))

    ans = -1

    for i in range(n) :
        for j in range(i,n) :
            if math.gcd(arr[i],arr[j]) == 1 :
                ans = max(ans,i + j + 2)
    print(ans)

    t -= 1