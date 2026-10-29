t = int(input())

for _ in range(t) :
    a,b,c = map(int,input().split())

    ans = 'NO'
    if a + b >= 10 :
        ans = "YES"
    
    elif b + c >= 10 :
        ans = "YES"
    
    elif a + c >= 10 :
        ans = "YES"
    
    print(ans)

    

    