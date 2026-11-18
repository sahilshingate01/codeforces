t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    att = []
    for i in range(n):
        rem = arr[i] % k
        if rem == 0:
            rem = k

        att.append((rem, i + 1))

    att.sort(key=lambda x: (-x[0], x[1]))

    print(*(idx for rem, idx in att))