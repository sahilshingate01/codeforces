n = int(input())
arr = list(map(int,input().split()))
q = int(input())

arr.sort()

for _ in range(q) :
    days = int(input())

    l = 0
    h = n - 1
    ans = 0

    while l <= h :
        mid = (l + h) // 2
        
        if arr[mid] <= days :
            ans = mid + 1
            l = mid + 1
        
        else :
            h = mid - 1
    
    print(ans)