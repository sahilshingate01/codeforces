n = int(input())

def f(idx,count):
    if idx > n:
        return count
    return f(idx + 1,count * idx)

print(f(1,1))
