n,m = map(int,input().split())

ans = -1
mi = (n + 1) // 2

for i in range(mi,n + 1) :
    if i % m == 0 :
        ans = i
        break

print(ans)
