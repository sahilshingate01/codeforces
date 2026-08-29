t = int(input())

def f(n):

    if n == 1:
        return True
    
    ans1 = False
    ans2 = False

    if n % 10 == 0:
        ans1 = f(n // 10)
    
    if n % 20 == 0:
        ans2 = f(n // 20)

    return ans1 or ans2

for _ in range(t):
    n = int(input())
    if f(n):
        print("YES")
    else:
        print("NO")

