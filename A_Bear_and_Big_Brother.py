a,b = map(int,input().split())
found = True
cnt = 1

while found:
    if (a * 3) <= (b * 2):
        cnt += 1
    a = a * 3
    b = b * 2
    
    if a > b:
        found = False
    
print(cnt)