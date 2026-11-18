t = int(input())

for _ in range(t):
    n = int(input())
    arr = sorted(map(int, input().split()))

    l = []
    r = []

    for i in range(n):
        if i == 0 or arr[i] != arr[i - 1]:
            l.append(arr[i])
        else:
            r.append(arr[i])

    r.sort(reverse=True)

    print(len(l) + len(set(r)))
    print(*(l + r))