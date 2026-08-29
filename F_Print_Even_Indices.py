n = int(input())
arr = list(map(int,input().split()))

def f(idx):
    if idx >= len(arr):
        return
    
    f(idx + 2)

    if idx % 2 == 0:
        print(arr[idx],end=" ")

f(0)
