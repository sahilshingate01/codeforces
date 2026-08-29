s,e = map(int,input().split())
count = 0

def f(idx):
    if idx == e:
        return 1
    
    if idx > e:
        return 0

    return f(idx + 1) + f(idx + 2) + f(idx + 3)

print(f(s))