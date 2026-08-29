t = int(input())

def solve(arr,ans,idx,n,ds):
    if idx == n:
        total = 0
        for i in range(len(ds)):
            total *= ds[i]
        
        if total % 6 == 0:
            for i in range(len(ds)):
                ans.append(ds[i])
        
        return
    ds.append(arr[idx])
    solve(arr,ans,idx + 1,n,ds)

    ds.pop()
    solve(arr,ans,idx + 1,n,ds)



for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = []
    solve(arr,ans,0,n,[])
    ans = list(set(ans))
    print(*ans)