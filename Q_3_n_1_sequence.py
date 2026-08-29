n = int(input())
ans = []

def f(n):
    if n == 1:
        ans.append(1)
        return 
    if n % 2 != 0:
        ans.append((3 * n) + 1)
        f((n * 3) + 1)
    else:
        ans.append(n // 2)
        f(n // 2)
        
f(n) 
print(len(ans))