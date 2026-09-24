t = int(input())

for _ in range(t) :
    n, q = map(int,input().split())
    arr = list(map(int,input().split()))

    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1,n) :
        prefix[i] = prefix[i - 1] + arr[i]
    
    for _ in range(q) :
        l, r, k = map(int,input().split())

        k_sum = (r - l + 1) * k
        orginal_sum = prefix[r - 1] - (prefix[l - 2] if l > 1 else 0) 

        if ((prefix[-1]) - (orginal_sum) + k_sum) % 2 != 0 : print("YES")
        else : print("NO")
