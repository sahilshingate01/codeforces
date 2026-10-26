t = int(input())

for _ in range(t):
    s = input().strip()
    r = ''.join(sorted(s))

    if r == s:
        r = r[::-1]

    if r == s:
        print("NO")
    else:
        print("YES")
        print(r)