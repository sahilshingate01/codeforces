n = int(input())
arr = list(map(int,input().split()))
temp = arr.copy()

def f(i,j):
    if i >= j:
        if temp == arr:
            return True
        return False
    arr[i],arr[j] = arr[j],arr[i]
    return f(i + 1,j - 1)


print("YES" if f(0,n - 1) else "NO")