n = int(input())
arr = list(map(int,input().split()))

def f(idx,total):
    if idx == n:
        return total 
    
    return f(idx + 1,total + arr[idx])
v = f(0,0)
print(f"{v / n:.6f}")
