k,n,w = map(int,input().split())
ans = 0

for i in range(1,w+1):
    ans += k * i

print("0" if (ans - n) < 0 else (ans - n))