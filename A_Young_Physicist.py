n = int(input())

x = 0
y = 0
z = 0

for _ in range(n) :
    t1,t2,t3 = map(int,input().split())
    x += t1
    y += t2
    z += t3

if x == 0 and y == 0 and z == 0 :
    print("YES")

else :
    print("NO")

