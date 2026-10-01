n = int(input())
arr = []

for _ in range(n) :
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort()
curr = 0

for a,b in arr :
    if b >= curr :
        curr = b
    
    else :
        curr = a 

print(curr)