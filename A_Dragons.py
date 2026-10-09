s ,n = map(int,input().split())

arr = []
f = True

for _ in range(n) : 
    x ,y = map(int,input().split())
    arr.append([x,y])

arr.sort()
for i in range(len(arr)) :
    if s > arr[i][0] :
        s += arr[i][1]
    else :
        f = False
        break


if f : print("YES")
else : print("NO")
