n = int(input())

def f(idx):
    if idx > n:
        return 
    print(idx)
    return f(idx + 1)

f(1)

