n = int(input())

def f(idx):
    if idx < 1:
        return
    if idx == 1:
        print(1)
        return
    print(idx,end=" ")
    return f(idx - 1)

f(n)