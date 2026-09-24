t = int(input())

for _ in range(t):
    s = input()
    op = 1000000

    for i in range(len(s) - 3):
        chnages = 0
        if s[i] != 'O':
            chnages += 1
        if s[i + 1] != 'D':
            chnages += 1
        if s[i + 2] != 'O':
            chnages += 1
        if s[i + 3] != 'O':
            chnages += 1

        op = min(op,chnages)

    print(op + (len(s) - 4))