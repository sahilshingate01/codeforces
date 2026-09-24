t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    cnt = 0
    max_cnt = 0
    for i in range(n):
        if s[i] == '#':
            cnt += 1
        else:
            cnt = 0
        max_cnt = max(max_cnt,cnt)

    print((max_cnt + 1) // 2)