t = int(input())

for _ in range(t):
    a,b,n = map(int,input().split())
    arr = list(map(int,input().split()))

    curr = b
    time = b

    for i in range(n):
        time += min(arr[i],a - 1)
    
    print(time)
            
