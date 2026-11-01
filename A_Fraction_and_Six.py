from collections import Counter

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    s1 = input()
    s2 = input()

    c1 = Counter(s1)
    c2 = Counter(s2)

    flag = True

    for ch in c1:
        if ch not in "six":
            if c1[ch] != c2[ch]:
                flag = False

    for ch in c2:
        if ch not in "six" and c2[ch] != c1[ch]:
            flag = False

    if c1['s'] - c2['s'] != 1:
        flag = False

    if c1['i'] - c2['i'] != 1:
        flag = False

    if c1['x'] - c2['x'] != 1:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")