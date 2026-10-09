t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    arr.sort()
    stack = []
    mid = n // 2

    stack.append(arr[mid])
    left = mid - 1
    right = mid + 1

    while left >= 0 or right < n :
        if left >= 0 :
            stack.append(arr[left])
            left -= 1
        
        if right < n :
            stack.append(arr[right])
            right += 1
        
    print(*stack)