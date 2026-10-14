t = int(input())
while t :
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    ans = "YES"
    for i in range(1,n) :
        if arr[i - 1] == arr[i] :
            ans = 'NO'
            break
    print(ans)
    t -= 1