t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    maxele = max(arr)
    minele = min(arr)

    print((maxele - minele) + 1)