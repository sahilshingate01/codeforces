n,m = map(int,input().split())
arr = list(map(int,input().split()))

sufix = [0] * n 
s = set()

for i in range(n - 1,-1,-1) :
    s.add(arr[i])
    sufix[i] = len(s)

for _ in range(m) :
    l = int(input())
    print(sufix[l - 1])
    