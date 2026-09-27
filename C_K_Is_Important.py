t = int(input())

for _ in range(t) :
    n, k = map(int,input().split())
    arr = list(map(int,input().split()))

    score = 0

    while len(arr) >= k:
        m = len(arr)

        left = k - 1
        right = m - k

        if arr[left] >= arr[right]:
            score += arr[left]
            del arr[left]
        else:
            score += arr[right]
            del arr[right]
    
    print(score)