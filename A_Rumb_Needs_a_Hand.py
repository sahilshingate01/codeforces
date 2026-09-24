t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    t = []

    for i in range(1,n + 1):
        if arr[i - 1] != i:
            t.append(arr[i - 1])

    f = True
    for i in range(1,len(t)):
        if t[i - 1] < t[i]:
            f = False
            break

    print("YES" if f else "NO")

    