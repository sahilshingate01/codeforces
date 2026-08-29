n = int(input())
arr = list(map(int,input().split()))

def f(idx,total):
    if idx >= len(arr):
        return total
    return f(idx + 1,total + arr[idx])
    #return value
print(f(0,0))