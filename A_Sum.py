t = int(input())
for _ in range(t) :
    a,b,c = map(int,input().split())
    ans = 'YES'
    if a + b == c :
        print(ans)
    elif b + c == a :
        print(ans)
    elif a + c == b :
        print(ans)
    else :
        print("NO")