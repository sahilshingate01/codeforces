a,b,c,d = map(int,input().split())

st = max(a,c)
end = min(b,d)

if st <= end:
    print(st,end)
else:
    print(-1)