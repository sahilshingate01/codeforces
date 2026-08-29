n = int(input())

def f(count,n):
    if (n // 2) <= 0:
        return count
    return f(count + 1,n // 2)

print(f(0,n))

    