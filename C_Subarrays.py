t = int(input())

for _ in range(t) :
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))

    prefix = [0] * (n + 1)
    prefix[0] = arr[0]
    for i in range(n) :
        prefix[i + 1] = prefix[i] + arr[i]

    freq = {}
    ans = 0

    for i in range(k + 1,n + 1) :
        rem = prefix[i - k - 1] % k
        freq[rem] = freq.get(rem,0) + 1

        curr = prefix[i] % k
        ans += freq.get(curr,0)
    
    print(ans)

    