n = int(input())
arr = list(map(int,input().split()))

def f(l,h,x):
    mid = (l + h) // 2

    if l > h:
        return -1
        
    if arr[mid] == x:
        return mid + 1
    
    if arr[mid] < x:
        return f(mid + 1,h,x)
    
    elif arr[mid] > x:
        return f(l,mid - 1,x)
    

t = int(input())

for i in range(t):
    x = int(input())
    print(f(0,n - 1,x))

    