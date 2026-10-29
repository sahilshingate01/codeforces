t = int(input())

for _ in range(t) :
    a,b,c,d = map(int,input().split())

    ans = 0
    if c < a : ans += 1
    if d < b : ans += 1
    print(ans)