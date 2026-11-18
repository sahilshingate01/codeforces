t = int(input())
for _ in range(t) :
    n,k = map(int,input().split())
    s = input()

    w = 0
    b = 0

    for i in range(k) :
        if s[i] == 'B' : b += 1
        else : w += 1

    ans = w 

    for i in range(k,n) :

        if s[i] == 'B' :
            b += 1
        else : 
            w += 1

        if s[i - k] == 'B' :
            b -= 1
        else :
            w -= 1
        ans = min(ans,w)
        
    print(ans)
