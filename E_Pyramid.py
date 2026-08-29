n = int(input())

def f(i,j):
    if i == n:
        return 
    
    f(i + 1,j - 1)
    print(i * " ",end="")
    print(j * "*",end="")
    print((j - 1) * "*",end="")
    print()

f(0,n)