n = int(input())

def f(idx,c):

    if idx == 1:
        return c
    
    if idx % 2 == 0:
        c += 1
        return f(idx // 2,c)
    
    else:
        c += 1
        return f(3 * idx + 1,c)

print(f(n,1))
    