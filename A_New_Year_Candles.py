a,b = map(int,input().split())

ans = a
empty = a

while empty >= b :
    new = empty // b
    empty = empty % b
    empty += new
    ans += new

print(ans)