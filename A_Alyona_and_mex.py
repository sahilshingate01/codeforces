n ,m = map(int,input().split())
diff = float('inf')

for i in range(m) :
    l,r = map(int,input().split())
    diff = min(diff,r - l + 1)
    
print(diff)
cnt = 0
for i in range(n) :
    print(cnt,end=" ")

    cnt += 1
    if cnt == diff :
        cnt = 0


    
