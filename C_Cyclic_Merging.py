t = int(input())

for _ in range(t) :
    n = int(input())
    arr = list(map(int,input().split()))

    cost = 0
    for i in range(n) :
        cost += max(arr[i],arr[(i + 1) % n])

    print(cost - max(arr))

