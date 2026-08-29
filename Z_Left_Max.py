import sys
sys.setrecursionlimit(200000)

n = int(input())
arr = list(map(int,input().split()))

def f(i,maxele):
    if i == n:
        return 
    maxele = max(maxele,arr[i])
    print(maxele,end=" ")

    f(i + 1,maxele)
f(0,arr[0])