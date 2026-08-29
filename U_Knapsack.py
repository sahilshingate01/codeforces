n,w = map(int,input().split())

weight = []
value = []

for i in range(n):
    a,b = map(int,input().split())
    weight.append(a)
    value.append(b)

def f(i,curw):
    if i == n:
        return 0

    if curw + weight[i] <= w:
        take = value[i] + f(i + 1,curw + weight[i])
    
    else:
        take = 0

    skip = f(i + 1,curw)

    return max(take,skip)

print(f(0,0))