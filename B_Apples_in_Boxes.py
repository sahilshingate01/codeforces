def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    arr.sort()

    if max(arr[n - 2], arr[n - 1] - 1) - arr[0] > k:
        print("Jerry")
        return

    total = sum(arr)

    if total % 2 == 1:
        print("Tom")
    else:
        print("Jerry")


t = int(input())
for _ in range(t):
    solve()