n = int(input())

def f(i,j):
    if i > n:
        return
    
    f(i + 1,j - 1)
    print(j * " ",end="")
    print(((i * 2) - 1) * "*",end="")
    print()

f(0,n)