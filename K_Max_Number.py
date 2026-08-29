n = int(input())
arr = list(map(int,input().split()))

def f(idx,maxele):
    if idx >= len(arr):
        return maxele

    return f(idx + 1,max(arr[idx],maxele))

print(f(0,(arr[0])))