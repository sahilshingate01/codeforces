t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    odd = 0

    for count in freq.values():
        if count % 2 != 0:
            odd += 1

    if odd <= k + 1:
        print("YES")
    else:
        print("NO")