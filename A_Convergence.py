t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    ans = n

    for i in range(n):
        x = arr[i]

        left = 0
        right = 0

        for j in range(n):
            if arr[j] < x:
                left += 1
            elif arr[j] > x:
                right += 1

        ans = min(ans,max(left,right))

    print(ans)