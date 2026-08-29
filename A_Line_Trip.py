t = int(input())

for _ in range(t):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))

    max_diff = arr[0]

    if n == 1:
        max_diff = arr[0]

    else:
        for i in range(1,n):
            if (arr[i] - arr[i - 1]) > max_diff:
                max_diff = (arr[i] - arr[i - 1])

    if max_diff < ((x - arr[-1]) * 2):
        print(((x - arr[-1]) * 2))
    
    else:
        print(max_diff)

    


        
        